from flask import render_template
from app import app
from .news_requests import get_sources

@app.route('/')
def HomePage():
    return render_template('sources.html')
    """
    Views thats renders the home page
    """
    general_news = get_sources('general')
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    return render_template('sources.html',general=general_news,business=business_news,sports=sports_news ) 
