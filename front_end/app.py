# Flask webserver for Haiku Divorce Letter Generator
# Regretabbly made by Michael Lance
# Date of crime: 4/25/2024
# Finished: NEVER
#-----------------------------------------------------------------------------------------------------------#
from flask import Flask, render_template, url_for
import divorce_haiku_generator
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)