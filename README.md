Anime Recommender System
Overview
The Anime Recommender System is a web application designed to provide recommendations for anime titles based on user input. It utilizes cosine similarity and TF-IDF vectorization techniques to calculate similarities between anime synopses and generate recommendations.

Features
Input Anime Title: Users can input the title of an anime they are interested in.
Auto-suggestions: As users start typing the anime title, auto-suggestions based on existing anime titles are provided to avoid input errors.
Get Recommendations: Upon clicking the "Get Recommendations" button, the system generates recommendations for anime titles similar to the input.
Top 10 Recommendations: The system displays the top 10 anime recommendations along with their similarity scores in a table format.
Beautiful Design: The user interface is designed with a visually appealing layout, including background images and styled components.
Technologies Used
Streamlit: Python library used for building interactive web applications with simple Python scripts.
Joblib: Library used for serialization and deserialization of Python objects, used for loading pre-trained models.
Scikit-learn: Python library for machine learning tasks, used for cosine similarity calculations and TF-IDF vectorization.
Pandas: Library used for data manipulation and analysis, used for handling recommendation data.
HTML/CSS/JavaScript: Used for front-end design and functionality of the web application.
Setup Instructions
Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Run the Streamlit application using the command streamlit run app.py.
Access the web application in your browser at the provided URL.
Usage
Enter the title of an anime in the input field.
Select the desired anime title from the auto-suggestions.
Click the "Get Recommendations" button to generate anime recommendations.
View the top 10 anime recommendations displayed in the table.
