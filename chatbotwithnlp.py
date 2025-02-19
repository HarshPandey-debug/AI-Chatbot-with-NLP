import nltk
import spacy
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Define some responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "thanks": ["You're welcome!", "Anytime!"],
    "default": ["I'm not sure I understand. Can you rephrase that?", "Sorry, I didn't get that."]
}

# Simple intent recognition function
def get_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words("english")]
    
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in tokens for word in ["thanks", "thank you"]):
        return "thanks"
    else:
        return "default"

# Chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
