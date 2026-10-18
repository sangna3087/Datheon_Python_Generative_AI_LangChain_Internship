import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# 1. Sample Document (Aap yahan apni koi bhi PDF ya text file load kar sakte hain)
sample_text = """
M.S. Ramaiah University of Applied Sciences (MSRUAS) is located in Bengaluru, Karnataka. 
It offers various undergraduate and postgraduate programs including Computer Science and Engineering. 
The university focuses heavily on applied sciences, technology, research, and innovation. 
Students engage in hardware projects, full-stack web development, and AI/ML engineering.
Campus facilities include advanced computer labs, incubation centers, and libraries.
"""

def run_rag_pipeline():
    print("Step 1: Loading and splitting document text...")
    
    # Wrap text into a LangChain Document object
    docs = [Document(page_content=sample_text)]
    
    # 2. Recursive Character Text Splitter (Chunking)
    # Yeh bade text ko 150 characters ke chote chunks mein todta hai taaki AI easily samajh sake
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150, 
        chunk_overlap=30
    )
    splits = text_splitter.split_documents(docs)
    print(f"-> Total chunks created: {len(splits)}")

    print("\nStep 2: Generating Vector Embeddings & Storing in ChromaDB...")
    # 3. Initialize Local Embeddings (Runs entirely on your PC, no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Store chunks into ChromaDB vector store locally
    vectorstore = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    print("-> Vector embeddings successfully stored in ChromaDB!")

    print("\nStep 3: Querying the RAG Pipeline...")
    # 5. Create a retriever to search relevant context based on user queries
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    
    query = "What programs and focus areas does MSRUAS have?"
    print(f"User Query: {query}")
    
    # Retrieve relevant document chunks
    relevant_docs = retriever.invoke(query)
    
    print("\n--- Retrieved Relevant Context ---")
    for i, doc in enumerate(relevant_docs):
        print(f"[Chunk {i+1}]: {doc.page_content}")

if __name__ == "__main__":
    run_rag_pipeline()