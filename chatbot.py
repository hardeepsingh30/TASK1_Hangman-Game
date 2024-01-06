# Task 3 --> BASIC CHATBOT
''' Create a text-based chatbot that can have conversations with users. You can use natural 
language processing libraries like NLTK or spaCy to make your chatbot more conversational.'''


import re

def get_basic_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey|namaste)\b', user_input):
        return "Hello! How can I help you?"

    elif re.search(r'\b(how are you)\b', user_input):
        return "I'm just a computer program, but thanks for asking!"

    elif re.search(r'\b(who are you|what is your name|your name)\b', user_input):
        return "My name is Chatbot develop by happy. For more query contact to admin"
    
    elif re.search(r'\b(help|i need help)\b', user_input):
        return "I can help you with general questions."
    
    elif re.search(r'\b(bye|goodbye|thankyou|thanks)\b', user_input):
        return "Goodbye! Have a great day."

    else:
        return "I'm not sure how to respond to that. Ask me something else."

def start_chat():
    print("Hello! I'm a basic ChatGPT-like chatbot. Type 'bye' to exit the chat.")
    print("How can I help you?")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Goodbye! Have a lovely day.")
            break

        response = get_basic_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
