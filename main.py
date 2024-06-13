from src.data_preparation import download_lecture_notes, preprocess_lecture_notes, download_llm_architectures_table
from src.embedding_generation import process_and_save_embeddings
from src.response_generation import respond_to_query

def main():
    lecture_urls = [
        "https://stanford-cs324.github.io/winter2022/lectures/introduction.html",
        "https://stanford-cs324.github.io/winter2022/lectures/transformers.html",
        "https://stanford-cs324.github.io/winter2022/lectures/attention.html",
        "https://stanford-cs324.github.io/winter2022/lectures/pretraining.html"
    ]
    
    # Define the output directory for lecture notes
    output_dir = "data/lecture_notes/"

    # Call functions to download and preprocess lecture notes
    download_lecture_notes(lecture_urls, output_dir)
    preprocess_lecture_notes(output_dir, "data/preprocessed_notes/")
    
    # Download LLM architectures table
    llm_architectures_url = "https://raw.githubusercontent.com/Hannibal046/Awesome-LLM/master/README.md#milestone-papers"
    download_llm_architectures_table(llm_architectures_url, "data/llm_architectures_table.txt")
    
    # Process and save embeddings
    process_and_save_embeddings(lecture_urls)
    
    # Example query to test response generation
    sample_query = "What are some milestone model architectures and papers in the last few years?"
    response = respond_to_query(sample_query)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
