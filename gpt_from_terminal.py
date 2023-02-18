import openai
import sys
import os

openai.api_key = os.environ.get('OPENAI_API_KEY');

def generate_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1000,
      n=1,
      temperature=1,
    )
    return response.choices

if __name__ == "__main__":
    query =sys.argv[1]
    if len(sys.argv)>2 and sys.argv[2]=="-e":
        print("Calling OpenAI API with Correct this to standard English query")
        response= generate_response(f"Correct this to standard English and suggest alternatives:{query}")
    elif len(sys.argv)>2 and sys.argv[2]=="-r":
        print("Calling OpenAI API with Raw query")
        response= generate_response(query)
    else:
        print("Calling OpenAI API with Text to a programmatic command query")
        response = generate_response(f"Convert this text to a programmatic command with example: {query}")

    print("------------------------------------------------------------------------")
    for choice in response:
        print(choice.text.strip())
    print("------------------------------------------------------------------------")





