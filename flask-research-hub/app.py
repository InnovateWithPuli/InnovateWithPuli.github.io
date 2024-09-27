from flask import Flask, jsonify, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API to fetch upcoming calls for papers
@app.route('/api/cfps')
def get_cfps():
    # Scrape a website or use an API that lists conferences
    url = "https://example.com/cfps"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example scraping logic - extract call for papers data
    cfps = []
    for item in soup.find_all('div', class_='conference'):
        title = item.find('h3').text
        deadline = item.find('span', class_='deadline').text
        link = item.find('a')['href']
        cfps.append({'title': title, 'deadline': deadline, 'link': link})

    return jsonify(cfps)

# API to fetch reviewing opportunities
@app.route('/api/reviewing')
def get_reviewing():
    # Scrape a website or use an API for reviewing opportunities
    url = "https://example.com/reviewing"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviewing = []
    for item in soup.find_all('div', class_='review'):
        title = item.find('h3').text
        link = item.find('a')['href']
        reviewing.append({'title': title, 'link': link})

    return jsonify(reviewing)

if __name__ == '__main__':
    app.run(debug=True)
