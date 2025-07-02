import os
from typing import List

def load_documents_from_folder(folder_path: str) -> List[str]:
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                docs.append(f.read())
    return docs

# Load your doc(s)
documents = load_documents_from_folder("docs/")

# Simple chunking (every 500 characters)
chunks = []
for doc in documents:
    chunks.extend([doc[i:i+500] for i in range(0, len(doc), 500)])

# Show some output
print(f"Loaded {len(documents)} document(s).")
print(f"Created {len(chunks)} chunks.")
print("Sample chunk:", chunks[0][:200], "...")
