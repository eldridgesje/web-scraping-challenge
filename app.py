from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

marsDict = {
    "headline": "Latest headline",
    "description": "The latest story will appear here.",
    "image": "https://mars.nasa.gov/system/news_items/main_images/8901_1-PIA24543-Curiosity's-Selfie-at-Mont-Mercou-main-web.jpg",
    "facts": "Mars facts will appear here.",
    "hemispheres": [{"title": "Placeholder", "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"},
    {"title": "Placeholder", "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"},
    {"title": "Placeholder", "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"},
    {"title": "Placeholder", "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"}] 
}
mars = mongo.db.mars
mars.update({}, marsDict, upsert=True)


@app.route("/")

def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)