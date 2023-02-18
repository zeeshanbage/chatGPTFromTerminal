# GPT from Terminal
Introducing GPT from Terminal - the AI-powered friend you never knew you needed! Simply pass GPT a prompt through the terminal, and it'll use the OpenAI API to generate an insightful response to help you out.
A Python script that uses the OpenAI API to generate responses to prompts. This script can be used from the terminal by passing the prompt as a command-line argument.

## Prerequisites

To use this script, you'll need an OpenAI API key. You can get an API key by creating an account on the OpenAI website.
```shell
export OPENAI_API_KEY=<API-KEY>
```
You can generate API keys in the OpenAI web interface. You can find your Secret API key in your [User settings](https://platform.openai.com/account/api-keys).

Install openai python library. 
```shell
pip install openai
```

Clone the script
```shell
git clone https://github.com/zeeshanbage/chatGPTFromTerminal.git
```

Add the function `chatgpt` inside .zshrc or .bashrc. you can call it anything, just replace `chatgpt` with your cool/lame custom name.
```shell
echo 'function chatgpt {
    query=$1
    python3 $HOME/chatGPTFromTerminal/gpt_from_terminal.py $query $2
}' >> ~/.zshrc
```

## Usage

To use this script, you can call the `chatgpt` function in your terminal. The function takes two arguments:

- `query`: The prompt you want to pass to the OpenAI API. It converts the Text to a programmatic command by default if no flag provided.
- `-r` (optional): A flag that runs the query without any filters (Raw).
- `-e` (optional): A flag that tells the script to correct the prompt to standard English and suggest alternatives.

### Example Usage
```css
$ chatgpt "How do I create a Python virtual environment?"
```

###Acknowledgments
This script was created using the OpenAI API and the openai Python library. Special thanks to the OpenAI team for making their technology available to the public!
