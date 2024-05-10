
import json
import sys
import requests

class dotdict(dict):
  """dot.notation access to dictionary attributes"""
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

def send_message(url, model, prompt):
  response = requests.post(url, json= {
    "model": model,
    "prompt": prompt,
  })
  if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    sys.exit(1)

  # Iterate through each line in the response content
  final_message = ""
  total_duration = 0
  load_duration = 0
  for line in response.iter_lines():
    if line:  # check if line is not empty
      json_object = dotdict(json.loads(line.decode('utf-8')))  # decode and parse the JSON
      #print(json_object)
      if json_object.done:
        total_duration = json_object.total_duration / 1000000 / 1000
        load_duration = json_object.load_duration / 1000000 / 1000
      else:
        final_message += json_object.response
  #print(f"Response: {final_message}")
  #print(f"Took {total_duration} seconds.")
  return final_message
