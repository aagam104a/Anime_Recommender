import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os

# Define the directory path
directory = os.path.dirname(os.path.realpath(__file__))

# Load anime names
anime_names_path = os.path.join(directory, 'anime_names.pkl')
anime_names = joblib.load(anime_names_path)

# Load cosine similarity matrix
cosine_similarity_matrix_path = os.path.join(directory, 'cosine_similarity_matrix.pkl')
tfidf_matrix = joblib.load(cosine_similarity_matrix_path)

def recommend_similar_anime(anime_name, top_n=10):
    try:
        index = anime_names.index(anime_name)
    except ValueError:
        return "Anime not found in database"
    
    similarities = cosine_similarity(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
    similar_indices = similarities.argsort()[-top_n-1:-1][::-1]
    
    recommendations = [(anime_names[i], similarities[i]) for i in similar_indices if i < len(anime_names)]
    
    return recommendations

st.set_page_config(layout="wide")

st.title('Anime Recommender System')

# Use selectbox widget with auto-suggestions based on anime names
anime_title = st.selectbox('Enter the title of an anime:', anime_names, index=anime_names.index('Cowboy Bebop'))

if st.button('Get Recommendations'):
    recommendations = recommend_similar_anime(anime_title)
    df_recommendations = pd.DataFrame(recommendations, columns=['Anime', 'Similarity Score'])
    st.write(f"Top 10 anime recommendations similar to '{anime_title}':")
    st.table(df_recommendations)
