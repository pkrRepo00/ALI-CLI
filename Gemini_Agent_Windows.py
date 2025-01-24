import google.generativeai as genai
import os
import subprocess
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini API
genai.configure(api_key=API_KEY)

# List of dangerous commands to block
BLOCKED_COMMANDS = [
    "del /Q C:\\*", "rmdir /S /Q C:\\", "shutdown -s", "shutdown -r",
    "format C:", "rm -rf /", "curl -O malware.exe", "wget http", "start malware.exe",
    "diskpart", "bcdedit", "taskkill /F /IM", "net stop", "net user", "reg delete"
]

def get_ai_command(user_input):
    """Sends user input to Gemini API and retrieves a command"""
    prompt = f"""
    You are a command-line AI assistant. Generate a single valid Windows command.
    STRICT RULES:
    - Only return the command.
    - No explanations or alternatives.
    - Ensure it runs in cmd.exe.
    
    User: {user_input}
    Command:
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip() if response.text else "⚠ ERROR: No command generated"

def is_safe_command(command):
    """Checks if the command is safe to execute"""
    for blocked in BLOCKED_COMMANDS:
        if blocked.lower() in command.lower():
            return False
    return True

def execute_command(command):
    """Executes a system command if it's safe"""
    if not is_safe_command(command):
        return "⚠ ERROR: Command blocked for safety!"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return str(e)

# Main AI loop
print("🚀 Semi-Safe AI Assistant Started (Type 'exit' to quit)")
while True:
    user_input = input("\nUser: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("Shutting down AI Assistant...")
        break

    ai_command = get_ai_command(user_input)
    print(f"AI Generated Command: {ai_command}")

    output = execute_command(ai_command)
    print(f"Executing...\n{output}")
