# Movie Recommender System

A content-based movie recommender system using Python, Streamlit, and Scikit-Learn.

## How to Run via Command Prompt (cmd)

Follow these steps to run the application on your computer:

### Step 1: Open Command Prompt and Navigate to the Project Folder
Open your Command Prompt (`cmd`) and run the following command to go into the project directory:
```cmd
cd "c:\Users\HP\Downloads\Movies-Recommender-System-main\Movies-Recommender-System-main\MoviesRecommedSystem"
```

### Step 2: Install Python Dependencies
Install the required libraries (Streamlit, Pandas, Scikit-Learn) by running:
```cmd
pip install -r requirements.txt
```

### Step 3: Generate the Similarity Matrix
Generate the missing `similarity.pkl` file using the included utility script:
```cmd
python generate_similarity.py
```

### Step 4: Run the Application
Start the Streamlit server:
```cmd
python -m streamlit run app.py
```

Once executed, the command prompt will output the local URL (usually `http://localhost:8501`). Copy and paste that URL into your web browser to open the movie recommender system.
