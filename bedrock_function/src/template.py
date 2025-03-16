def generate_code_template(context):
    template = f"""
    Anime Island AI has a database with a table named `content_library` containing information about their anime content. The table has the following columns:
    - `release_date` (YYYY-MM-DD)
    - `content_id`
    - `episode_count`
    - `view_count`

    Generate SQL queries based on the following context: {{context}}
    """
    return template 

def generate_translate_template(context):
    template = f"""
    You are a highly skilled software engineer tasked with translating the following legacy Java code to Python.
    1. Please provide the translated Python code, ensuring that it maintains the same functionality and behavior as the original Java code.
    2. Include comments explaining any significant changes, optimizations, or improvements made during the translation process.
    3. Your translation should follow best practices and modern coding standards for Python.
    
    Review the provided legacy code snippet in context: {{context}}
    """
    return template

def generate_analyze_code_template(context):
    template = f"""
    Please provide a detailed explanation and interpretation for the following code snippet. Your explanation should cover:
    1. The purpose and functionality of the code
    2. How the code works, step-by-step
    3. Any important data structures, algorithms, or design patterns used
    4. Potential improvements, optimizations, or alternative approaches
    5. Any external dependencies or libraries used, and their roles
    6. Any potential challenges, gotchas, or pitfalls to be aware of
    
    Review the provided code snippet in context: {{context}}
    """
    return template

def ask_question_template(context):
    template = f"""
    Your task is to answer the question as asked.
    Review the provided request in context: {{context}}
    """
    return template
    