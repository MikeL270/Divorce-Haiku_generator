# Flask webserver for Haiku Divorce Letter Generator
# Regretabbly made by Michael Lance
# Date of crime: 4/25/2024
# Last messed with: 4/28/2024
#-----------------------------------------------------------------------------------------------------------#
from flask import Flask, render_template, url_for, jsonify, request
import os
import divorcehaikugen
from dotenv import load_dotenv
#-----------------------------------------------------------------------------------------------------------#
# Basic Config
app = Flask(__name__)

load_dotenv() # Load environmnet variables

# Check if the user has set a custom API key in the settings
# THIS SHOULD ONLY BE USED WHEN SELF HOSTING
if "CUSTOM_API_KEY" in os.environ:
    api_key = os.getenv("CUSTOM_API_KEY")
else:
    api_key = os.getenv("DEFAULT_API_KEY")

generator = divorcehaikugen.DivorceLetterGenerator(api_key)

@app.route("/")
def index():
    return render_template("index.html")

#-----------------------------------------------------------------------------------------------------------#
# Functions using routes to communicate with the client
@app.route("/get_haiku", methods=["POST"])
def get_haiku():    
    try:
        data = request.get_json()
        print(data)
        haiku = generator.generate_haiku(divorced_party_name=data["name"], anger_level=data["anger_level"], divorce_reason=data["reason"])
        print(haiku)
        return jsonify(haiku=haiku), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route("/set_api_key", methods=["POST"])
def set_api_key():
    global generator
    # Save the new key to the environment variables
    os.environ["CUSTOM_API_KEY"] = new_api_key
    # Pass the new api key to the generator 
    print("hi mom")
    try:
        data = request.get_json()
        generator.update_api_key(data["key"])
        return jsonify({"message": "API key updated successfully"}), 200
        
    except Exception as e:
        return jsonify(error=str(e)), 500
    
if __name__ == "__main__":
    app.run(debug=True)