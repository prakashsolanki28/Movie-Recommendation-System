# Movie Recommender

This is a movie recommendation system that takes a movie name as input and returns recommended movies.

## Getting Started

To use this movie recommender system, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies from `requirements.txt`.

3. Run Jupyter Notebook First
``` python []
jupyter notebook  # run command in terminal 
```
![Image Description](./jupyter_notebook.png)
Run all cell one bye one in jupyter notebook, get `movies.pkl` and `similarity.pkl` file

Run app file
``` python []
streamlit run app.py #
```

## Jupyter Notebook

import csv files
```
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
```
merge the two dataframes using `title`
```
movies = movies.merge(credits,on="title")
```
drop unnecessary columns
```
movies = movies.drop(columns=["homepage","title_x","title_y","status","production_countries"])
```
remove all rows with null values
```
movies.dropna(inplace=True)
```
check duplicates
```
movies.duplicated().sum()
```

## Usage

To get movie recommendations, provide the name of a movie as input. The system will then generate a list of recommended movies based on the input.
