from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)

#function that displays the input button gets the input variable 
#search and then stores in index
@app.route("/", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        index = request.form["nm"]
        return redirect(url_for("index", search=index ))
    else:
        return render_template("button.html")
        





#route that gets the meme from subreddit of the search variable input
@app.route("/<search>")   
def index(search):
    def get_meme():
        response = requests.get('https://meme-api.com/gimme'+"/"+search)
        meme_large = response.json()["preview"][-2]
        subreddit = response.json()["subreddit"]
        return meme_large, subreddit
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
