# test_docarray.py

from docarray import BaseDoc
from docarray.typing import NdArray
import numpy as np


# Define a custom document schema
class MyDoc(BaseDoc):
    embedding: NdArray[128]


# Create a document with a random 128-dimensional embedding
doc = MyDoc(embedding=np.random.rand(128))

# Print the document
print("Single Document:")
print(doc)

# Create a list of documents
from docarray import DocList

docs = DocList[MyDoc]([MyDoc(embedding=np.random.rand(128)) for _ in range(3)])

print("\nDocList of Documents:")
for i, d in enumerate(docs):
    print(f"Doc {i+1}: {d}")
