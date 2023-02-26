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
python3 -m pip install openai
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
Restart the terminal now.
## Usage

To use this script, you can call the `chatgpt` function in your terminal. The function takes two arguments:

- `query`: The prompt you want to pass to the OpenAI API. It converts the Text to a programmatic command by default if no flag provided.
- `-r` (optional): A flag that runs the query without any filters (Raw).
- `-e` (optional): A flag that tells the script to correct the prompt to standard English and suggest alternatives.

### Example Usage
```css
$chatgpt "git revert last 3 commits"
Calling OpenAI API with Text to a programmatic command query
------------------------------------------------------------------------
Example - git revert HEAD~3..HEAD
------------------------------------------------------------------------
```

```css
chatgpt "create a sql job in ssms" -r
Calling OpenAI API with Raw query
------------------------------------------------------------------------
1. Open SQL Server Management Studio (SSMS).
2. In the Object Explorer panel, expand the SQL Server Agent node, and then expand its child nodes: Jobs, Local, and Right-Click Jobs.
3. Right-click Jobs, select New Job... from the context menu.
4. In the New Job window, type a name for the new job.
5. In the Category drop-down menu, choose a category for the job.
6. In the Owner drop-down menu, select the owner of the job.
7. Select the Steps page and click the New... button to create a new job step.
8. In the New Job Step window, type a Step Name and select the type of job step.
9. Select the appropriate box to specify what happens if the job fails or succeeds.
10. Enter the command that should be executed when the job runs.
11. Select the Schedules page and click the New... button to create a new schedule for the job.
12. In the New Job Schedule window, type a name for the schedule, select the frequency of the job, and specify when the job should start.
13. Click OK to close the job schedule window.
14. Select the Notifications page and configure how you want to be notified when the job runs.
15. Click OK to create the new job.
------------------------------------------------------------------------
```

### Acknowledgments
This script was created using the OpenAI API and the openai Python library. Special thanks to the OpenAI team for making their technology available to the public!
