from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/movies")
def movies():
    return get_movies()['movie_title'] \
        .to_json(orient='records')


def get_movies():
    return pd.read_csv('data/movie_metadata.csv')


if __name__ == "__main__":
    app.run()
