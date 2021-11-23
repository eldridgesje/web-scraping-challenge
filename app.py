from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

mars = mongo.db.mars
mars_data = scrape_mars.scrape()
mars.update({}, mars_data, upsert=True)

@app.route("/")
def index():
    marsOne = mongo.db.mars.find_one()
    return render_template("index.html", mars=marsOne)


@app.route("/scrape")
def scraper():
    marsTwo = mongo.db.mars
    mars_data = scrape_mars.scrape()
    marsTwo.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
