import urllib.request,json
from app import app
from .models import news

Sources = news.Sources



def get_sources(category):
    """
    function that gets response from the api call
    """
    api_key = app.config['API_KEY']

    url = app.config['NEWS_API_BASE_URL']
    sources_url = url.format(category, api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None

        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

def process_new_sources(sources_list):
    sources_outcome = []
    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")

        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)

    return sources_outcome
