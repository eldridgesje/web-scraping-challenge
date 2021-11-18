from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    def headline_scrape():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://redplanetscience.com/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        headline = soup.find("div", class_="content_title").get_text()
        return(headline)
        browser.quit()

    def description_scrape():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://redplanetscience.com/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        description = soup.find("div", class_="article_teaser_body").get_text()
        return(description)
        browser.quit()

    headline = headline_scrape()
    description = description_scrape()

    def image_scrape():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://spaceimages-mars.com/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        image = soup.find("img", class_="headerimage")
        image_url = url + image["src"]
        return(image_url)
        browser.quit()

    image_url = image_scrape()

    def facts_scrape():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        url = "https://galaxyfacts-mars.com/"
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        table = str(soup.find("table"))
        return(table)
        browser.quit()

    mars_table = facts_scrape()

    hemispheres = [
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    ]

    mars_dict = {
        "headline": headline,
        "description": description,
        "image": image_url,
        "facts": mars_table,
        "hemispheres": hemispheres
    }

    return(mars_dict)