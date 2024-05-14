# Baymax Virtual Assistant

Baymax Virtual Assistant is an AI-powered virtual assistant that emulates Baymax, the friendly and caring healthcare companion from the movie Big Hero 6. This assistant is designed to interact with users, provide information, and engage in conversations, ensuring a comforting and helpful experience.

## Features

- **Natural Language Understanding**: Interacts with users through natural language.
- **Speech Recognition**: Converts spoken language into text using speech-to-text functionality.
- **Text-to-Speech**: Responds to users with synthesized speech.
- **Healthcare Emulation**: Provides responses and interactions similar to Baymax, focusing on care and comfort.
- **Customizable Responses**: Tailors responses to user needs and context.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/baymax-virtual-assistant.git
    cd baymax-virtual-assistant
    ```

2. **Create and Activate a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    or

    conda create -n baymax python=3.9
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file in the project root directory and add your API keys. Also, add in the `.env` into the `.gitignore` file.
    ```
    OPENAI_API_KEY=your_openai_api_key
    ELEVENLABS_API_KEY=elevenlabs_api_key
    ```

## Usage

1. **Run the Virtual Assistant**:
    ```bash
    python main.py
    ```

2. **Interaction**:
    - The assistant will start listening for your input.
    - Speak to Baymax and wait for the response.
    - The session continues until you say "I am satisfied with my care", "quit", or "exit".