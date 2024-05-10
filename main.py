
import utils

# read in all the endpoints we are going to be chatting with
llms = {
  "llama3": "http://localhost:11434/api/generate",
  "mistral": "http://localhost:11435/api/generate",
}
main_llm = "llama3"
main_prompt = "Give me a response I can use to start a discussion with other LLMs."

# pick a main llm in which we will ask "Lets start a discussion with other LLMs"
response = utils.send_message(llms.get(main_llm), main_llm, main_prompt)
print(response)

# go around the horn and ask each LLM the same question and get responses back
for llm, url in llms.items():
  print(f"The URL for {llm} is: {url}")

# repeat this at random intervals

