from langchain.text_splitter import RecursiveCharacterTextSplitter

# STEP 1: Load your document
with open("docs/doc1.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# STEP 2: Split into chunks (for embedding)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
documents = text_splitter.create_documents([raw_text])

# Optional: Check your chunks
for doc in documents:
    print(doc.page_content)
