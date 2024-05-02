from setuptools import setup, find_packages

setup(
    name="divorcehaikugen",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai', 
        'python-dotenv',  
    ],
    author="Michael Lance",
    author_email="michaelbraydenlance@gmail.com",
    description="Generate divorce letter haikus using ChatGPT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
