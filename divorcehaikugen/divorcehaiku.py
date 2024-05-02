# Haiku Divroce Letter Generator
# Written in Python by a maniac
# A Michael Lance catastrophe
# Created: 4/24/24
# Last modified: 5/2/2024
# I am so very sorry this exists
#-----------------------------------------------------------------------------------------------------------#
from openai import OpenAI
import os
import time

class DivorceLetterGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.assistant_id="asst_OCpjHEWcKCkxQInod0LYTRED" # Hardcoded assistant id saves me a ton of money 
        self.client = OpenAI(
            api_key = self.api_key # api_key management abstracted up to the server for ease of modification
        )
        self.assistant = self.client.beta.assistants.retrieve(
            assistant_id=self.assistant_id
        )
        self.thread = self.client.beta.threads.create() # create a new thread and maintain it per session
        
    def generate_haiku(self, divorced_party_name, anger_level, divorce_reason):
        
        message = self.client.beta.threads.messages.create(
            thread_id = self.thread.id,
            role = "user", # I don't fully understand the roles in OpenAI's API
            # content argument is left purposefully sparse to save on tokens
            content = f"serve: divorced_party_name={divorced_party_name}, anger={anger_level}, reason={divorce_reason}"
        )
        
        running = True
        while running: # could have easily been an async await, but this was easier and this project is huge
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id = self.thread.id,
                assistant_id = self.assistant.id,
                instructions = "serve only the haiku"
            )
                    
            if run.status == 'completed': # this conditional block could be expanded to include error handling 
                self.messages = self.client.beta.threads.messages.list(
                    thread_id = self.thread.id
                )
                
            for msg in self.messages.data: # I have a sneaking suspicion that there is a more efficient way to do this
                for content_block in msg.content: # I am fully aware this kills my runtime complexity
                    if hasattr(content_block.text, 'value'): 
                        return content_block.text.value 
                running = False
            
            else:
                print(run.status)
                time.sleep(0.1) # pace the sscript a little to let openAI breathe

    def update_api_key(self, new_key): # I have no vehicle to test this as I will not purchase a second key
        self.api_key = new_key
        self.client = OpenAI(
            api_key = self.api_key
        )
        
#-----------------------------------------------------------------------------------------------------------#       
        
if __name__ == "__main__":
    example_letter = DivorceLetterGenerator()
    print(example_letter.generate_haiku(divorced_party_name = "Karen", anger_level = "5", divorce_reason = "farting in her sleep"))
    # 