import os
import google.auth as auth
from vertexai.language_models._language_models import ChatModel
from google.cloud import aiplatform



class PalmAiModelSingleton:
  _instance = None
  _ai = None
  _parameters = dict()
    
  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
    return cls._instance
  
  def __init__(self):
   
    model = ChatModel.from_pretrained("chat-bison@001")
    self._ai = model.start_chat()
    pass
  
  def message(self, msg:str, temp, max_op_token, top_p, top_k):
    
    if max_op_token != None and max_op_token > 1024:
      raise Exception("Maximum output token allowed is 1024!")
    self._parameters["temperature"] =  temp if temp != None else 0.2
    self._parameters["max_output_tokens"] = max_op_token if max_op_token != None else 1000
    self._parameters["top_p"] = top_p if top_p != None else 0.95
    self._parameters["top_k"] = top_k if top_k != None else 0.4

    response = self._ai.send_message(msg, **self._parameters)
    # print(response.text)
    return response.text

if __name__ == '__main__':
  model = PalmAiModelSingleton()
  model.message("write a song using the names and properties of 10 famous programming language")