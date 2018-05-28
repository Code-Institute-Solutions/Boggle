#!/usr/bin/env python
import os

from flask import Flask
from flask import render_template

import boggle

app = Flask(__name__)


@app.route("/")
def boggle_page():
    ROWS, COLS = 4, 4
    grid = boggle.make_grid(ROWS, COLS)
    dictionary = boggle.get_dictionary('words.txt')
    words = boggle.search(grid, dictionary)

    # to simplify the template, we'll convert the grid into a list
    grid_list = []
    for row in range(ROWS):
        grid_list.append([grid[(row, col)] for col in range(COLS)])
    return render_template("boggle.html", grid=grid_list, words=words)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', '8080')),
            debug=True)
