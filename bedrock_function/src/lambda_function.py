# Import necessary libraries
import json
import boto3
import os
import re
import logging

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from template import generate_code_template, generate_translate_template, generate_analyze_code_template, ask_question_template


# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Create a Bedrock Runtime client
bedrock_client = boto3.client('bedrock-runtime')


# Define Lambda function
def lambda_handler(event, context):
    # Log the incoming event in JSON format
    logger.info('Event: %s', json.dumps(event))

    request_body = json.loads(event['body'])
    prefix = request_body.get('prefix')
    content  = request_body.get('content')
        
    # Generate the prompt based on the prefix
    if prefix == 'generate_code':
        template_generator = generate_code_template
    elif prefix == 'translate_code':
        template_generator = generate_translate_template
    elif prefix == 'analyze_code':
        template_generator = generate_analyze_code_template
    elif prefix == 'ask_question':
        template_generator = ask_question_template

    template = template_generator(context=content)
    
    prompt_template = ChatPromptTemplate(
        messages=[HumanMessagePromptTemplate.from_template(template)],
        input_variables=["context"],
    )
    
    prompt = prompt_template.format(context=content)
    
    # Prepare the input data for the model
    input_data = {
        "inputText": prompt,
        "textGenerationConfig": {
            "temperature": 0.7,
            "topP": 0.95,
            "maxTokenCount": 1000,
            "stopSequences": []
        }
    }
    
    # Log the input data
    logger.info('Input data: %s', json.dumps(input_data))

    # Invoke the Bedrock Runtime with the cleaned body as payload
    response = bedrock_client.invoke_model(
        modelId=os.environ['BEDROCK_MODEL_ID'],
        body=json.dumps(input_data).encode("utf-8"),
        accept='application/json',
        contentType='application/json'
    )

    # Load the response body and decode it
    result = json.loads(response["body"].read().decode())
    
    # Log the response payload
    logger.info('Response payload: %s', json.dumps(result))
    
    # Extract the generated text from the response
    generated_text = ""
    if "results" in result and result["results"]:
        generated_text = result["results"][0].get("outputText", "").replace("\\n", "\n")
    
    # Return the result with status code 200 and the necessary headers
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': generated_text
    }
