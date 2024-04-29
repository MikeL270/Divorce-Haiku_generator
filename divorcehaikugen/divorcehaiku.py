# Haiku Divroce Letter Generator
# Written in Python by a maniac
# A Michael Lance catastrophe
# Created: 4/24/24
# Finished: NEVER
# I am so very sorry this exists
#-----------------------------------------------------------------------------------------------------------#
from openai import OpenAI
import os
import time

class DivorceLetterGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.assistant_id="asst_OCpjHEWcKCkxQInod0LYTRED"
        self.client = OpenAI(
            api_key = self.api_key
        )
        self.assistant = self.client.beta.assistants.retrieve(
            assistant_id=self.assistant_id
        )
        self.thread = self.client.beta.threads.create()
        
    def generate_haiku(self, divorced_party_name, anger_level, divorce_reason):
        
        
        message = self.client.beta.threads.messages.create(
            thread_id = self.thread.id,
            role = "user",
            content = f"serve: divorced_party_name={divorced_party_name}, anger={anger_level}, reason={divorce_reason}"
        )
        
        running = True
        while running:
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id = self.thread.id,
                assistant_id = self.assistant.id,
                instructions = "serve only the haiku"
            )
                    
            if run.status == 'completed':
                self.messages = self.client.beta.threads.messages.list(
                    thread_id = self.thread.id
                )
                
            for msg in self.messages.data: 
                for content_block in msg.content:  
                    if hasattr(content_block.text, 'value'): 
                        return content_block.text.value 
                running = False
            
            else:
                print(run.status)
                time.sleep(0.1) 

    def update_api_key(self, new_key):
        self.api_key = new_key
        
if __name__ == "__main__":
    example_letter = DivorceLetterGenerator()
    print(example_letter.generate_haiku(divorced_party_name = "Karen", anger_level = "5", divorce_reason = "farting in her sleep"))