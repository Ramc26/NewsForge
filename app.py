from flask import Flask, request, render_template
from driver import getNews, getNewsTe, getNewsEn

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    news_data = None
    if request.method == 'POST':
        query = request.form['query']
        lang=request.form['language']
        category=request.form['category']
        news_data = getNews(query,lang,category)
    return render_template('index.html', data=news_data)

@app.route('/telugu', methods=['GET', 'POST'])
def Telugu():
    news_data = None
    if request.method == 'POST':
        query = request.form['query']
        lang=request.form['language']
        category=request.form['category']
        news_data = getNews(query,lang,category)

    elif request.method == 'GET':
        news_data = getNewsTe()
    return render_template('index.html', data=news_data)

@app.route('/english', methods=['GET', 'POST'])
def English():
    news_data = None
    if request.method == 'POST':
        query = request.form['query']
        lang=request.form['language']
        category=request.form['category']
        news_data = getNews(query,lang,category)

    elif request.method == 'GET':
        news_data = getNewsEn()
    return render_template('index.html', data=news_data,)
    
    

if __name__ == '__main__':
    app.run(debug=True)
