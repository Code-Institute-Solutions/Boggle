#!/usr/bin/env python
import os

from flask import Flask
from flask import render_template

import boggle

app = Flask(__name__)




@app.route('/<int:rows>/<int:cols>')
@app.route('/<int:rows>')
@app.route("/")
def boggle_page(rows=4, cols=None):
    if not cols:
        cols = rows
    grid = boggle.make_grid(cols, rows)
    dictionary = boggle.get_dictionary('words.txt')
    words = boggle.search(grid, dictionary)

    # to simplify the template, we'll convert the grid into a list
    grid_list = []
    for row in range(rows):
        grid_list.append([grid[(row, col)] for col in range(cols)])
    return render_template("boggle.html", grid=grid_list, words=words)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', '8080')),
            debug=True)
