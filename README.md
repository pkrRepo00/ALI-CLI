# AI CLI: Your Personal AI-Powered Command Line Assistant

## 🚀 Introduction

Imagine having an AI-powered assistant right in your command line - one that understands your commands, automates tasks, and interacts seamlessly with your system. Enter **AI CLI**, a powerful AI agent integrated with the **Gemini API**, designed to execute commands, manage files, fetch system details, and much more - all from your terminal!

This guide walks you through what AI CLI is, how to set it up, and how to make the most out of it. Whether you're a developer, sysadmin, or tech enthusiast, this tool will revolutionize the way you interact with your machine.

## 🔥 What is AI CLI?

AI CLI is a command-line automation tool that integrates Google's Gemini AI to generate and execute system commands based on natural language input. Instead of typing out long and complex commands, you simply describe what you want to do, and the AI converts it into an executable command.

### ✨ Features:
- **Natural Language Understanding**: Ask in plain English, and AI CLI translates it into a valid system command.
- **Automation**: Run system tasks like file management, system info retrieval, and more.
- **Customizable Safety Modes**: Choose between safe execution (only allows predefined commands) and unsafe mode (executes any command).
- **Interactive Confirmation**: Approve commands before execution to avoid accidental actions.
- **Logging System**: Keep track of all executed commands and AI responses.

## 🛠️ How to Set Up AI CLI

### 1️⃣ Prerequisites

Before you start, ensure you have:
- Python 3.1+ installed
- A Google Gemini API Key (Sign up on Google AI)
- Required dependencies installed

### 2️⃣ Installation Steps

#### 1. Clone the Repository:
```bash
git clone https://github.com/pkrRepo00/Ai-CLI.git
cd Ai-CLI
```

#### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

#### 3.1 Set Up API Key:
Add your Gemini API key to your environment variables:

- **macOS/Linux**:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

- **Windows**:
```bash
set GEMINI_API_KEY="your-api-key-here"
```
#### 3.2 Set Up .env:
In the root directory of your AI CLI project, create a `.env` file and add your API key like this:
```bash
GEMINI_API_KEY="your-api-key-here"
```
Then save it
#### 4. Run AI CLI:
```bash
python Gemini_Agent_Windows.py      # For Windows

python Gemini_Agent_Linux.py        # For Linux

python Gemini_Agent_MacOS.py        # MacOS


```

## 🏗️ How to Use AI CLI

Once launched, AI CLI will prompt you for input. Simply type your request in natural language:

#### Example Commands:

- **User**: List all files in the current directory  
  **AI CLI**: `dir`

- **User**: Create a file named "test.txt"  
  **AI CLI**: `echo. > test.txt`

- **User**: Move "test.txt" to the Documents folder  
  **AI CLI**: `move test.txt C:\Users\YourName\Documents`

By default, **safe mode** is enabled, preventing execution of dangerous commands. To run in unsafe mode (allowing all commands), use:

```bash
python ai_cli.py --unsafe
```

⚠️ **Use unsafe mode cautiously, as it can execute any system command!**

## 📌 Additional Features
- **Interactive Confirmation**: Before executing a command, AI CLI will ask for your confirmation.
- **Logging**: All commands and responses are logged for review.
- **Retry Mechanism**: AI CLI intelligently retries if command generation fails.

## 🔮 Future Enhancements
We're continuously improving AI CLI. Some upcoming features include:
- **Voice Command Support** 🎙️
- **Task Scheduling & Automation** 📅
- **Cross-Platform Enhancements** 🖥️

Got ideas? Contribute to the project on GitHub!

## 🎉 Conclusion
AI CLI is your AI-powered command-line assistant, making automation seamless and efficient. Whether you're managing files, checking system info, or scripting workflows, AI CLI empowers you to work smarter.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

