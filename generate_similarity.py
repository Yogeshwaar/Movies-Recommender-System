import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    movie_list_path = os.path.join(dir_path, 'movie_list.pkl')
    similarity_path = os.path.join(dir_path, 'similarity.pkl')

    print(f"Loading {movie_list_path}...")
    with open(movie_list_path, 'rb') as f:
        movies = pickle.load(f)
    
    print("DataFrame info:")
    print(movies.info())
    
    print("Fitting CountVectorizer and computing cosine similarity...")
    cv = CountVectorizer(max_features=5000, stop_words='english')
    # Fill any NaN tags with empty string
    movies['tags'] = movies['tags'].fillna('')
    vector = cv.fit_transform(movies['tags']).toarray()
    
    print(f"Vector shape: {vector.shape}")
    similarity = cosine_similarity(vector)
    
    print(f"Similarity matrix shape: {similarity.shape}")
    print(f"Saving to {similarity_path}...")
    with open(similarity_path, 'wb') as f:
        pickle.dump(similarity, f)
    
    print("Done! similarity.pkl generated successfully.")

if __name__ == '__main__':
    main()
