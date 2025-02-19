# Chatbot with NLP

## Overview
This project is a simple chatbot that uses **Natural Language Processing (NLP)** with **NLTK** and **spaCy** to understand user queries and respond accordingly. The chatbot tokenizes input, recognizes intents, and provides relevant responses.

## Features
- Tokenization using **NLTK**
- Intent recognition
- Named Entity Recognition (NER) with **spaCy**
- Customizable response system

## Requirements
Make sure you have the following installed:

### Dependencies
```sh
pip install nltk spacy
```

### Download Required Data
After installing dependencies, download the required NLP models:
```sh
python -m spacy download en_core_web_sm
```

Inside Python, run:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

## Usage
Run the chatbot script using:
```sh
python chatbotwithnlp.py
```
Then, type your queries and interact with the chatbot.

## File Structure
```
/chatbot-with-nlp
│── chatbotwithnlp.py  # Main chatbot script
│── requirements.txt    # List of dependencies
│── README.md           # Project documentation
```

## Troubleshooting
If you get an error about missing NLTK data, try downloading all required resources:
```python
import nltk
nltk.download('all')
```

For **spaCy model issues**, ensure `en_core_web_sm` is downloaded:
```sh
python -m spacy download en_core_web_sm
```

## License
This project is open-source and can be modified or distributed freely.

