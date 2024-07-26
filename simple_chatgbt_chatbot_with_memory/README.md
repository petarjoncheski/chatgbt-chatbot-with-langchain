# Simple Console ChatGPT Bot with Langchain

This project demonstrates how to create a simple console-based ChatGPT bot using Langchain. The bot interacts with users via the console, processes their inputs using OpenAI's GPT model, and provides responses based on a defined prompt template.

## Features

- Simple console interaction
- Integration with OpenAI's GPT-3.5-turbo
- Customizable prompt templates
- Environment variable management for API keys

## Prerequisites

- Python 3.7 or higher
- PyCharm IDE Community Edition (optional, but recommended for development)
- An OpenAI API key

## Getting Started

Follow these steps to set up and run the chat bot:

### 1. Download and Install PyCharm

- Go to the [PyCharm download page](https://www.jetbrains.com/pycharm/download/) and download the Community edition (free). Optionally, you can use the Professional edition (paid).
- Follow the installation instructions for your operating system.

### 2. Create a New Project in PyCharm

- Open PyCharm and click on "New Project".
- Choose a location for your project and select "Pure Python" as the project type.
- Click "Create" to set up your new project.

### 3. Configure the Python Interpreter

- Go to `File -> Settings` (or `Preferences` on macOS) -> `Project: <your_project_name>` -> `Python Interpreter`.
- Click the gear icon and select "Add".
- Choose "Virtual Environment" and click "OK" to set up a new virtual environment for your project.

### 4. Obtain an OpenAI API Key

To use the OpenAI API, you'll need an API key:

- Visit [OpenAI's platform](https://platform.openai.com/signup) and sign up for an account if you don't already have one.
- After logging in, navigate to the [API Keys page](https://platform.openai.com/api-keys).
- Click "Create new key", give your key a name, and click "Create Key".
- Copy the API key and store it securely.

### 5. Set Up the Environment

- Create a `.env` file in your project directory.
- Add the following line to the `.env` file:
   OPENAI_API_KEY=your_api_key_here
   
### 8. Installing `pip`

Windows: Download and install Python from the official [Python website](https://www.python.org/downloads/). pip is included by default with Python installations. After installation, you can use pip from the Command Prompt.

macOS: pip comes pre-installed with Python if you installed it using Homebrew or the official installer from the Python website. To ensure pip is installed, you can run pip --version in Terminal. If pip is not available, install it using the following command:
    `sudo easy_install pip`
    Alternatively, download and install Python from the official [Python website](https://www.python.org/downloads/).


### 7. Install Required Packages

Open the terminal in PyCharm and run the following command:
`pip install python-dotenv langchain-core langchain-openai`

### 8. Running the app

- In PyCharm, right-click the Python file and select "Run 'simple_chatgpt_chatbot.py'".
- Or you can run the Script in Terminal: `python simple_chatgpt_chatbot.py`