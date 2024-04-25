from setuptools import setup, find_packages

setup(
    name="divorce_haiku_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai',   # Ensure this is the correct package name on PyPI
        'python-dotenv',  # This is the typical PyPI package name for dotenv
    ],
    author="Michael Lance",
    author_email="michaelbraydenlance@gmail.com",
    description="Generate divorce letter haikus using ChatGPT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
