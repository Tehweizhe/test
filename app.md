from flask import Flask, render_template
from scraper import scrape_the_verge

app = Flask(__name__)

@app.route('/')
def background():
    headlines = scrape_the_verge()
    return render_template('background.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
