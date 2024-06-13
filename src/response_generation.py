from transformers import pipeline
from src.query_processing import process_query

# Function to generate response
def generate_response(query, context):
    summarizer = pipeline('summarization')
    summary = summarizer(context, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to respond to query
def respond_to_query(query):
    processed_query = process_query(query)
    # Placeholder for retrieving relevant context from embeddings
    context = "This is a sample context from the lecture notes."
    response = generate_response(processed_query, context)
    return response
