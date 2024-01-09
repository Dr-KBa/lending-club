# Unsupervised Learning & Hyperparameter Tuning overview
I am a data scientist who was just hired by the LendingClub. They want to automate their lending decisions fully, and they hired me to lead this project. My team consists of a product manager to help me understand the business domain and a software engineer who will help me integrate my solution into their product. During the initial investigations, I've found that there was a similar initiative in the past, and luckily for me, they have left a somewhat clean dataset of LendingClub's loan data.

In the first meeting with my team, we all have decided to use this dataset because it will allow me to skip months of work of building a dataset from scratch. In addition, I have decided to tackle this problem iteratively so that I can get test my hypothesis that I can automate these decisions and get actual feedback from the users as soon as possible. For that, I have proposed a few-step plan on how to approach this problem:

The first step of my plan is to create a machine learning model to classify loans into accepted/rejected so that I can start learning if I have enough data to solve this simple problem adequately.

The second step is to predict the grade for the loan.

The third step is to predict the subgrade and/or interest rate.

My team likes the plan, especially because after every step, I'll have a fully-working deployed model that my company can use. Excitedly I get to work!

# Project structure
This project (Project_M3S2) is composed of the following notebooks:
-Part 1 - accept reject preparation;
-Part 2 - model streamlit deploy;
-Part 3 - Data prep grade int_rate;
-Part 4 - Prediction of grade int_rate-final;

Ant two additional files of web access and interaction with the model:
app.py
requirements.txt

# Data acquisition
The dataset was provided in Turing College website (unknown licence info)


# The notebooks
The notebooks include data preparation, exploratory analysis, and prediction model training parts.

# Model deployment and web interface
Model to classify applications as accepted/rejected is deployed as a streamlit app. Backend is running at GitHub Codespaces. And is accessible via: https://fluffy-telegram-jj567x6jqv7v2p779-8501.app.github.dev/
It may not be accessible at all times to conserve resources!

Models predicting grade and interest rate are not included in the notebooks (their metrics) as at the time of submitting they are still running. Models will be demonstrated at the demo time.

# Contribution
The analysis and most of the coding was done by Kazimieras Badokas.

ChatGPT and GitHub co-pilot was prompted to generate some complex functions or workarounds also to help with domain knowledge and web interface. Major help and explanations are highlithed and dislosed in the text throughout the code to avoid plagiarism.

Dall-E3 was prompted to generate cover image for the notebook.

# License for dataset
MIT License for notebooks (consult for the use of dataset!)

Copyright (c) [2023] [Kazimieras]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


