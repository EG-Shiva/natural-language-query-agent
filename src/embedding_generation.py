# src/embedding_generation.py

import os
import numpy as np
from sentence_transformers import SentenceTransformer

def process_and_save_embeddings(lecture_urls):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    preprocessed_dir = 'data/preprocessed_lecture_notes'
    embeddings_dir = 'data/embeddings'

    os.makedirs(embeddings_dir, exist_ok=True)

    for i in range(len(lecture_urls)):
        text_file = os.path.join(preprocessed_dir, f"preprocessed_lecture_{i}.txt")
        if not os.path.exists(text_file):
            print(f"File not found: {text_file}")
            continue
        
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        embeddings = model.encode([text])
        np.save(os.path.join(embeddings_dir, f"embedding_{i}.npy"), embeddings)

    print("Embeddings generated and saved.")
