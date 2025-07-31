# Python AI/ML Projects
This repository is a collection of Python code examples and projects focused on Artificial Intelligence (AI) and Machine Learning (ML). It aims to provide practical implementations of various AI/ML concepts, from foundational data preparation to advanced predictive modeling and natural language processing.<br><br>
**Currently features projects on *Natural Language Processing* and *Predictive Modeling*.**
---
## Projects

This repository currently includes the following projects:
* ### [Basic NLP Chatbot](./basic_nlp_chatbot)
  This project implements a basic chatbot that processes user input. It first attempts **intent recognition** to match the input with predefined conversational topics. If a match is found, a corresponding response is provided. If no specific intent is recognized, the chatbot leverages **sentiment analysis** using the `TextBlob` library to determine the emotional tone (polarity) of the user's message.
    * If the sentiment polarity is greater than 0 (positive), the chatbot responds with a randomly chosen message from a set of predefined positive responses.
    * If the sentiment polarity is less than 0 (negative), it sends a randomly selected response from predefined negative responses.
    * If the sentiment polarity is exactly 0, indicating a neutral statement, the chatbot will handle it accordingly (e.g., with a generic or neutral response).


* ### [Predicting Car Prices](./predicting_car_prices)
    An end-to-end machine learning project focused on predicting car prices based on various features. This includes data cleaning, exploratory data analysis, feature engineering, model training (e.g., using regression algorithms), and model evaluation.
