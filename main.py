
import requests
import json
import sys
import utils

# read in all the endpoints we are going to be chatting with
llms = {
  "llama3": "http://localhost:11434/api/generate",
  "mistral": "http://localhost:11435/api/generate",
}
main_llm = "llama3"
main_prompt = "Give me a response I can use to start a discussion with other LLMs."

# pick a main llm in which we will ask "Lets start a discussion with other LLMs"
response = requests.post(llms.get(main_llm), json= {
  "model": main_llm,
  "prompt": main_prompt,
})
# Check if the response was successful
if response.status_code != 200:
  print("Error:", response.status_code, response.text)
  sys.exit(1)  # Exit the program with an error code

final_message = ""
total_duration = 0
load_duration = 0
# Iterate through each line in the response content
for line in response.iter_lines():
  if line:  # check if line is not empty
    json_object = utils.dotdict(json.loads(line.decode('utf-8')))  # decode and parse the JSON
    # Now you can work with json_object as a Python dictionary
    print(json_object)
    if json_object.done:
      total_duration = json_object.total_duration / 1000000 / 1000
      load_duration = json_object.load_duration / 1000000 / 1000
    else:
      final_message += json_object.response
print(f"Response: {final_message}")
print(f"Took {total_duration} seconds.")

# go around the horn and ask each LLM the same question and get responses back
for llm, url in llms.items():
  print(f"The URL for {llm} is: {url}")

# repeat this at random intervals

