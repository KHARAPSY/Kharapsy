import requests

def get_answer_from_wikipedia(question):
    WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "opensearch",
        "search": question,
        "limit": 1,
        "namespace": 0,
        "format": "json"
    }
    
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    
    try:
        return data[2][0]
    except (IndexError, TypeError):
        return "Sorry, I couldn't find an answer to that."

