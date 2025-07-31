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
  This project focuses on building a machine learning model to predict car prices. It utilizes a preprocessed dataset containing over 200 examples and more than 20 features. The workflow includes:
    * **Data Transformation:** Categorical features are converted into a computer-interpretable numerical format using `ColumnTransformer` and `OneHotEncoder`, while numerical features are scaled using `StandardScaler`.
    * **Model Selection & Hyperparameter Tuning:** `GridSearchCV` is employed to find the optimal hyperparameters for various regression models, including Linear Regression, Random Forest, and Gradient Boosting.
    * **Model Training & Evaluation:** The best-performing models are trained and evaluated using key regression metrics: Root Mean Squared Error (RMSE) and R-squared ($R^2$) score.
    The core analysis and model development are presented in the [Jupyter Notebook](./predicting_car_prices/predicting_car_prices.ipynb) within this directory.
