# Flask webserver for Haiku Divorce Letter Generator
# Regretabbly made by Michael Lance
# Date of crime: 4/25/2024
# Finished: NEVER
#-----------------------------------------------------------------------------------------------------------#
from flask import Flask, render_template, url_for, jsonify, request
import divorcehaikugen

generator = divorcehaikugen.DivorceLetterGenerator()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_haiku', methods=['POST'])
def get_haiku():    
    try:
        data = request.get_json()
        print(data)
        haiku = generator.generate_haiku(divorced_party_name=data["name"], anger_level=data["anger_level"], divorce_reason=data["reason"])
        print(haiku)
        return jsonify(haiku=haiku), 200
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run()