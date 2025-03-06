# GenAI
# AWS Code and Workshop Links:

- AWS BedRock Samples : https://github.com/aws-samples/amazon-bedrock-samples/
- AWS BedRock Agent Samples :  https://github.com/awslabs/amazon-bedrock-agent-samples
- Amazon Bedrock Workshop : https://catalog.us-east-1.prod.workshops.aws/workshops/a4bdb007-5600-4368-81c5-ff5b4154f518/en-US
- Amazon Bedrock Agents Workshop : https://catalog.workshops.aws/agents-for-amazon-bedrock/en-US
- bedrock-multi-agents-collaboration-workshop : https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop

AWS BedRock-  https://github.com/aws-samples/amazon-bedrock-workshop   
Agents - https://catalog.workshops.aws/agents-for-amazon-bedrock/en-US   
Agents Workshop - https://github.com/aws-samples/amazon-bedrock-samples/tree/main/agents-and-function-calling/bedrock-agents/features-examples


                ┌──────────────────────────────────────────┐
                │          🌐 User Interface (UI)          │
                │     (React-based search interface)      │
                └──────────────────────────────────────────┘
                                │  
                      User Query (Natural Language)
                                │  
            ┌────────────────────────────────────┐
            │        🤖 Query Processing Layer   │
            │ - User Query Agent (Intent detection) │
            │ - Reformulates queries for better search │
            └────────────────────────────────────┘
                                │  
      ┌──────────────────────────────────────────┐
      │        🔍 Metadata Retrieval Layer       │
      │ - Metadata Retrieval Agent               │
      │ - Hybrid Search (Lexical + Semantic)     │
      │ - Queries Collibra, Elasticsearch, FAISS │
      └──────────────────────────────────────────┘
                                │  
         ┌──────────────────────────────────────┐
         │   📊 Ranking & Personalization Layer │
         │ - Ranks results based on past searches │
         │ - Uses LLM-based re-ranking           │
         └──────────────────────────────────────┘
                                │  
            ┌────────────────────────────────────┐
            │        📝 Response Agent           │
            │ - Converts search results into     │
            │   user-friendly explanations       │
            └────────────────────────────────────┘
                                │  
                ┌──────────────────────────────────┐
                │        🌎 Search API Layer       │
                │ - FastAPI/Flask for search API   │
                └──────────────────────────────────┘
                                │  
    ┌─────────────────────────────────────────────────────┐
    │         🏛️ Data Storage & Indexing Layer            │
    │ ┌──────────────────────────────┐  ┌───────────────┐ │
    │ │ 📂 Collibra (Metadata API)    │  │ 🔍 Elasticsearch │ │
    │ │ - Business & Technical Meta  │  │ - Lexical Search │ │
    │ └──────────────────────────────┘  └───────────────┘ │
    │ ┌──────────────────────────────┐  ┌───────────────┐ │
    │ │ 🧠 FAISS/Pinecone (Vector DB) │  │ 📜 Redis/PostgreSQL │ │
    │ │ - Embeddings for similarity  │  │ - Stores user search │ │
    │ └──────────────────────────────┘  └───────────────┘ │
    └─────────────────────────────────────────────────────┘
