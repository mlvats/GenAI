## LLMs- Large Language Models : 
- A large language model is a model trained on a large amount of  text data that is capable of understanding human text and/or generating human-like text.

## Generative AI
- A generative model is one that can create new content based on data it's been trained on
  - Image generation
  - Video generation
  - Music generation
  - Text generation
 
## Input for a Language Model
- For the purposes of modern language modeling, the  smallest units of meaning in language are considered to be words (or parts of words)
- Where do words draw their meaning from? - You shall know a word by the company it keeps!
-----
Tokenization -> Embedding -> Language Modeling Task -> Large Language Model
---
![image](https://github.com/mlvats/GenAI/assets/32443900/34477409-c729-4fb5-a5df-57c873d9e4a5)

![image](https://github.com/mlvats/GenAI/assets/32443900/64c704a4-fd2d-4a04-bab9-e2e190ef9171)
----

## Tokenization 
- Tokenization is the process of breaking down a piece of text into smaller units, typically words or sentences, called tokens.
- These tokens are the basic building blocks for further analysis in natural language processing tasks.
- Here's an example of tokenization:
-  Input Text: "Tokenization is the process of breaking down a piece of text into smaller units, typically words or sentences, called tokens."
- Tokenized Output (Word Tokenization):
- ["Tokenization", "is", "the", "process", "of", "breaking", "down", "a", "piece", "of", "text", "into", "smaller", "units", ",", "typically", "words", "or", "sentences", ",", "called", "tokens", "."]
- In this example, the input text is tokenized into individual words, and each word becomes a token.
- Punctuation marks like commas and periods are also treated as separate tokens.
- You can perform tokenization using various techniques and libraries in Python, such as the split() method for simple tokenization by whitespace or punctuation,
- or more advanced tokenizers like those provided by the Natural Language Toolkit (NLTK) or SpaCy.
- Link - https://platform.openai.com/tokenizer  (openAI Tokenizer)

## Word embeddings
- Word embeddings are a type of word representation in natural language processing (NLP) that allows computers to understand and process language more effectively by converting words into dense vectors of real numbers.
- These vectors capture semantic relationships between words, enabling algorithms to understand similarities, context, and meaning.
- Create a Python script (e.g., `word2vec_example.py`) and copy the following code:

```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Sample sentences
sentences = [
    "The cat sat on the mat.",
    "The dog chased the cat.",
    "The cat and the dog are friends."
]

# Tokenize the sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train Word2Vec model
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Test the model
word = "cat"
similar_words = model.wv.most_similar(word)
print(f"Words similar to '{word}': {similar_words}")
----------------
```
- https://platform.openai.com/tokenizer

------------
![image](https://github.com/mlvats/GenAI/assets/32443900/a0a9595b-e89e-4f95-aee6-10c0539c9291)
-------

![image](https://github.com/mlvats/GenAI/assets/32443900/db2978be-1bf1-4e3f-a826-75ab0edaa816)

![image](https://github.com/mlvats/GenAI/assets/32443900/94226d0c-18ad-4a51-ba71-39c982eda8d0)
--------------
![image](https://github.com/mlvats/GenAI/assets/32443900/b69b515b-4ad6-4fe7-92c4-0c15067f8cc1)
![image](https://github.com/mlvats/GenAI/assets/32443900/441139fa-a171-42c7-a6bf-03c0580662e5)
------------
![image](https://github.com/mlvats/GenAI/assets/32443900/e531440a-d05d-4913-9bc9-009b272f3680)

------------
![image](https://github.com/mlvats/GenAI/assets/32443900/befcf866-4cab-4fe3-91fd-b61bcbb8c9d1)

## Vector Storage
- Store embeddings (words, documents, etc) for fast  retrieval and similarity search
- Embeddings can also be called “vectors”
- Computer = [-0.1, 2.4, 3.005, …, 0.07, 100.04]   ----> vector
- 
## Vector Storage System Pipeline
 - Indexing
   - Text splitting / chunking method
   - Embedding model
     
## Vector Indexing: Chunking
- The gpt-4-turbo context window is 128,000 tokens 
- That means the model can handle approximately 100,000 words, or 200 pages of input 
- Rule of thumb: 1 token to 0.75 words
 
## Vector Indexing: Chunking Approaches
- Text: She owned a dog. She and the dog ran a marathon, and they were both extremely wappered by the end
- Chunk 1: She owned a dog. She and the dog ran a marathon, and they were both
- Chunk 2: extremely wappered by the end. 
----
 ![image](https://github.com/mlvats/GenAI/assets/32443900/03ed981c-3e04-4019-bee1-ceacfd9511f1)

---
![image](https://github.com/mlvats/GenAI/assets/32443900/5649eb78-4d68-4a84-957a-be397cecb29a)
---
![image](https://github.com/mlvats/GenAI/assets/32443900/719d85e6-b071-4357-947d-3b88d7525a42)
--------
![image](https://github.com/mlvats/GenAI/assets/32443900/bb6a9a34-904d-4086-b760-39cd93c0ff64)
-------
![image](https://github.com/mlvats/GenAI/assets/32443900/dad622ca-5377-483f-9368-f4cc07aacf1b)
















