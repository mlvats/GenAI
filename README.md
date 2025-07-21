Thank you for sharing your transcript, Moti. Here’s a reviewed and cleaned-up version of your GraphQL API presentation transcript, making it more coherent, grammatically correct, and professional while retaining your original ideas and flow.

⸻

✅ Revised Transcript:

Recording in progress

Good morning everyone. My name is Moti Vats. Thank you for giving us the opportunity to present our idea. Today, we are proposing a unified GraphQL API to enable automated governance across the enterprise.

Currently, our governance data—including AI governance, model governance, and data governance—are managed by multiple teams on multiple platforms. Integration today is largely done through REST APIs, which we believe can be significantly optimized by moving to GraphQL.

A unified GraphQL API will consolidate all governance-related data in one place. It will be accessible to internal consumers via a single endpoint. This allows users to fetch exactly what they need from one or more sources in a single call, enabling more efficient automation.

This will also support real-time dashboards and allow AI agents to dynamically retrieve governance context as needed.

Let me quickly highlight some advantages of GraphQL over REST:
	•	REST requires a fixed endpoint per resource. Each request and response has a fixed schema.
	•	Any changes, like adding a new field, require modifying the endpoint, which can introduce breaking changes.
	•	In contrast, GraphQL uses a single endpoint to fetch data from multiple sources.
	•	Fields can be added without breaking existing consumers, and users can request only the data they need.
	•	This opens up many innovative use cases.

In our internal prototype, codenamed HEATON, we have integrated:
	•	Model governance inventory data
	•	Traditional model inventory use cases
	•	Selected Highlander data
	•	Project metadata from the CGI team
	•	Data from GPT-related projects, such as project names and subscription details

All of this is now accessible through a unified GraphQL layer.

🛠️ Automation & Write Capabilities:

We’ve enabled both read and write capabilities for most of this data.

For example, in MLOps today, a model is marked as approved via an STTP call before deployment. If the deployment doesn’t happen, someone must manually update the model inventory in MGM to indicate it wasn’t deployed.

Now, using our API, the MLOps pipeline can update the deployment status automatically, removing the need for manual updates.

Similarly, the AI governance platform can access project metadata (e.g., from CGI or Highlander) directly. AI agents can also query this data dynamically, enabling advanced search, debugging, or validation workflows.

We’ve seen teams like TOD building AI agents that can now access project-level data from multiple sources via GraphQL, which helps in debugging and issue resolution.

📊 Dashboards and Automation:

Real-time dashboards can be built using this API. Routine tasks such as model attestations, monitoring, and validation can now be automated.

With this infrastructure, we expect several benefits:
	•	Standardized, queryable governance data
	•	Improved automation and monitoring in model deployments
	•	Real-time insights
	•	Performance improvements (GraphQL has shown better interaction speeds with DynamoDB compared to REST)
	•	Modernization of legacy APIs (like ECS Java-based Highlander services)

✅ Conclusion:

We believe this unified GraphQL approach will not only modernize our API infrastructure but also provide the flexibility, performance, and automation capabilities needed to scale governance across our AI and data systems.

Thank you.

⸻

Would you like help converting this into a polished slide deck or speaker notes as well?




## Vector database compariso
- https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/vector-db-comparison.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/use-cases-talent-mgmt.html  (knowledge graph)

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
