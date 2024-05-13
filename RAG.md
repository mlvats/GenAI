## Language Models
- In a language modeling task, a model is trained to predict a missing word in a sequence of words.
- there are two types of language models:
  - Auto-regressive
  - Auto-encoding
 ------------
 ![image](https://github.com/mlvats/GenAI/assets/32443900/d743028b-a21f-4adc-8b81-7d98d9275a90)
 --
![image](https://github.com/mlvats/GenAI/assets/32443900/a819987d-9be9-4588-9278-cb3035057f3d)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/2c6519cb-484f-46ca-8ef4-147cde9600dc)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/27c95a30-b0b9-44f3-83e5-30036ee980a5)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/04f52834-9458-4d5f-9dbf-06bc5d74765b)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/b09891c9-419d-407e-8802-2c98b98b47e5)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/2d1c27bc-9af2-433e-bad5-0f834479788a)
--
![image](https://github.com/mlvats/GenAI/assets/32443900/c54ace85-93cf-4220-a433-d804956d3bb8)
---
# Components of a RAG- 
- A RAG system generally has three parts:
1. An indexer - A mechanism to compress raw text data into vectors and stored in a database
2. A retriever - Closely tied to the indexer, something to retrieve data from that database given a query.
3. A generator - an LLM to reason through the user’s query and the retrieved knowledge to provide an inline conversational response. This will be GPT-4

## Semantic Search System
 - The Indexer and the Retriever - Semantic Search
 - A system that  understands the meaning and context of a search query and matches it against the meaning and context of available documents for retrieval.
 - It can find  relevant results without having to rely on exact keyword or n-gram matching, often using a pre-trained
 - large language model (LLM) to understand the nuances of the query and the documents.
## Semantic Search
- Retrieving relevant documents from a natural language query
- ![image](https://github.com/mlvats/GenAI/assets/32443900/c4b1971b-7505-4ebc-852a-46f5c698ddfa)
---
# Types of Search
## Asymmetric Search 
- A search scenario where there is an imbalance in the semantic information (or size) of the input query and the documents or information that the search  system has to retrieve.
- This typically refers to situations where one (usually the search query) is much shorter than the other.
- Matching a user’s eBay item query with paragraph descriptions of the item

## Symmetric Search 
- The input query and the documents or information that the search system has to retrieve are of comparable semantic complexity or size.
- Similar to its asymmetric counterpart, symmetric search may also use advanced techniques like semantic understanding rather than relying solely on exact keyword or n-gram matches.
- Matching a Google query with the titles of websites

## Text Embeddings
- A way to represent words or phrases as machine-readable numerical vectors in a multi-dimensional space,
- typically based on their contextual meaning.
- The principle is that similarphrases (in terms of semantic meaning) will have vectors that are close together by some measure (likeEuclidean distance), and vice versa.
- We will start by using OpenAI’s embedding feature and then work our way to using some open-source LLMs.

## Chunking
- Turning large documents into smaller “chunks”
- Max token method with overlap
- Natural Whitespace Chunking with no overlap
- Grouping natural chunks by semeantic similarty
- 
 
## Prompt Engineering 
– The process of carefully designing inputs for massively large language models such as Claude or ChatGPT to guide them to produce relevant and coherent outputs.
- Many AI researchers consider prompt engineering a “bug” in AI and that it will go away in the next few years.

## Ask First, Shoot Later
- LLMs generate one token at a time.
- That means that order matters–put your instruction FIRST and context SECOND so that when the LLM reads the context,
- it has already read the instruction and is “thinking” about the task the whole time.
- Think of LLMs as “reasoning machines” vs  “thinking machines”.
- LLMs excel at tasks that require reasoning - using context and input information in conjunction to produce a nuanced answer
## Why real-time data matters
- Grounding” an LLM with real-time factual data is one way to prevent hallucinations.
- Giving an LLM access to real-time data grounds the AI to use the given context more often (not always - see the evaluation slides)

## Few-shot Learning / In-context Learning
- Few-shot learning – Giving an LLM examples of a task being solved to teach the LLM how to reason through a problem and also to format the answer in a desired format
- These examples can be as detailed as you’d like (at the cost of.. well money)
- 
## Chain of Thought Prompting
- Chain of Thought Prompting forces an LLM to  generate reasoning for an answer alongside an answer. This usually leads to better/more actionable results.
[image](https://github.com/mlvats/GenAI/assets/32443900/ea221e98-e9c8-463c-9f06-29ccd815833b)
![image](https://github.com/mlvats/GenAI/assets/32443900/ace3a32f-cf57-456f-8bcc-b2ce9d8aea97)
---
## Prompt Injection
- Addressing malicious attacks on LLMs
- Prompt Injection – Feeding a prompt to an LLM to guide an unintended output
- Input/output validation is an easy way to prevent against this.
- For example, check for the semantic similarity between your LLM’s output and your prompt

# Validating LLM Inputs and Outputs

## Input Validation 
– Checking the integrity and correctness of data input before the data is processed by a system or used by a machine learning model. 
The goal is to prevent incorrectly formed or improper data from entering and potentially corrupting the system. 
It may involve checking for format consistency, logical errors, security risks, or other criteria defined as necessary for the input.

## Output Validation 
– Examining the output or results generated by a system or a machine learning model to ensure they meet certain criteria or expectations. 
- This could involve checking for logical correctness, adherence to certain rules or constraints, or other context-specific factors
![image](https://github.com/mlvats/GenAI/assets/32443900/62bd0ef8-649c-4ae9-99ac-a0afb0952480)

## Using NLI to Perform Output Validation

