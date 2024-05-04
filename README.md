# Divorce Letter Haiku Generator

The Divorce Letter Haiku Generator allows users to put an end to their ill fated maritaly affiar in an efficent manner. If it is not obvious through the concept alone, this webapp is a joke and should be treated as such. The generator was developped as a final project for SDEV1200, advanced python programming. Version 1.1 is the version that will be turned in for credit, but I have plans to develop this program further.

## Overview

Written in python, the magic occurs behind the scenes via the dlhg generator module. The module was written using OOP principles and leverages OpenAi's API to handle the generation of haikus.

The generator calls a flask webserver home, where it communicates through your browser via asyncrhonous axios requests to deliver haikus.

## Features

- **Haiku Customization:** Users pass arguments such as name, and reason to the generator to get a customized haiku, or leave it blank for something more general.
- **Interactive Web Interface:** Built using Flask to satisfy the rubric. Flask is great though.
- **AI-Powered Text Generation:** Leverages a custom gpt "assistant" accessed via OpenAI's api to generate haikus.
- **Near Instant Haiku Retrieval:** Haikus are generated almost immediately and displayed for the user to review. This is dependent on the users's network and the API's availability.
- **Responsive Design:** Compatible across a variety of devices and screen sizes.

## Tech Stack

- **Python:** Core programming language.
- **OpenAI Module:** For integrating the custom-trained GPT model.
- **Flask:** Lightweight web framework used for the user interface.
- **Vue.js** Javascript framework for handling *most ui elements

# Getting Started

## Notice

The goal is to serve this webapp as a docker-compose container where it will run on an nginx server to make self hosting straight forward. This goal has yet to be reached as this app uses an API key there are security considerations to be made, and with my other finals looming I have opted to pause further development past satisfying the requirements of the assignment. 

### Creating the environment // Installing the generator

It is recommended that you run this app in a virtual environment to issolate it from your global python set up, that way dependencies can be satisfied without conflicting with other python apps you may have.

```bash
# Create a Python virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate
```
Next you need to install the requirements and the generator itself (as a module).

```bash
# Install all needed dependencies with pip
pip3 install --no-cache-dir -r requirements.txt

# Install the generator
pip3 install --no-cache-dir .
```

## Stop-Gap
Until I can figure out a system to enable the app to start without an api_key you need to create an environment file (.env) and store your key as DEFAULT_API_KEY. If you do not do this the app will fail to run. This is primarily what is holding back the docker container.

### Running the server

Finally, run the server.

```bash
cd front_end/

python app.py
```

Then connect to the server