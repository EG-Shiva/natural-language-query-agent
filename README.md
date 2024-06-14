# Natural Language Query Agent

This project implements a Natural Language Query Agent that can answer questions based on a set of lecture notes and a table of LLM architectures.

## Project Structure

- `data/`: Directory to store downloaded and processed data.
- `src/`: Directory containing source code.
- `src/__init__.py`: Makes `src` a Python package.
- `src/data_preparation.py`: Scripts for downloading and preprocessing data.
- `src/embedding_generation.py`: Scripts for generating embeddings.
- `src/query_processing.py`: Query processing logic.
- `src/response_generation.py`: Response generation logic.
- `src/advanced_features.py`: Advanced features such as citing references and conversational memory.
- `main.py`: Main script to run the project.
- `requirements.txt`: List of dependencies.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/natural-language-query-agent.git
    cd natural-language-query-agent
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:
    ```bash
    python main.py
    ```


