from pathlib import Path
import numpy as np
from LSA import LSA

corpus = []

documents_path = Path("./documents/")

for file_path in documents_path.glob("*.txt"):
    print(f"reading file {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as file:
        corpus.append(file.read())

model = LSA()

value = model.strip(corpus)

print(corpus)
print(value)