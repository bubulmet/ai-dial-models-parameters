from task.app.main import run
import argparse

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

parser = argparse.ArgumentParser(
    description="Run the chat app with specific model"
)
parser.add_argument(
    "-m", "--modelname", type=ascii, help="LLM name", 
    default="gpt-4o"
)

if __name__ == "__main__":
    args = parser.parse_args()
    DEPLOYMENT_NAME = args.modelname

    run(
        deployment_name=DEPLOYMENT_NAME,
        print_request=False, # Switch to False if you do not want to see the request in console
        print_only_content=False, # Switch to True if you want to see only content from response
    )

# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API