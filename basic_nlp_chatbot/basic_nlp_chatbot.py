# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob
import random

# Defining the ChatBot class for interaction.
class ChatBot:
    def __init__(self):
        #Defining intents based on keywords
        self.intents = {
            "hours": {
                "keywords": ["hour", "open", "close"],
                "response": "We are open during weekdays from 9 AM to 5 PM."
            },
            "location":{
                "keywords": ["located", "location", "city", "state", "where"],
                "response": "We are situated in New Jersey in the heart of Middlesex County."
            },
            "return": {
                "keywords": ["refund", "money back", "return"],
                "response": "I'd be happy to help you process your return. Let me transfer you to a live agent."
            },
            "live agent": {
                "keywords": ["live agent", "talk to someone", "connect"],
                "response": "Let me transfer you to a live agent. Our agents would love to assist you today."
            }
        }
    # Performing sentiment analysis of the user's message using textblob which is efficient for Natural Language Processing (NLP).
    def get_response(self, message):
        message = message.lower()
        for intent_data in self.intents.values():
            if any(word in message for word in intent_data["keywords"]):
                return intent_data["response"]
            
        # Generating the chatbot's response based on sentiment.
        sentiment = TextBlob(message).sentiment.polarity
        
        # Printing the chatbot's response and sentiment.
        if (sentiment>0):
            sentimentResponse = ["That's great to hear! Please drop a rating at xyz.com about your experience", 
                                 "We aboslutely loved your feedback, please don't forget to leave us a positive rating!", 
                                 "That's so nice of you, please fill out the form at xyz.com explainig what impressed you the most"]
            # Return a randomly selected string from the alternatives
            return random.choice(sentimentResponse)
        # Responding to negative comments
        elif (sentiment<0):
            sentimentResponse = ["I'm so sorry to hear that. Please let me know in detail how may I help you?", 
                                 "I am sorry for this. Our team would definitely help you out.", 
                                 "That is definitely not the experience we want our customers to have. Please explain in few words how may I assist you today?"]
            # Return a randomly selected string from the alternatives
            return random.choice(sentimentResponse)
        # Responding to neutral statements
        else:
            return "I see. Can you tell me more about that?"

    def chat(self):
        print("ChatBot: Hi, how can I help you today?")
        while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
            print(f"\nChatBot: {self.get_response(user_message)}")
        print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    ChatBot().chat()