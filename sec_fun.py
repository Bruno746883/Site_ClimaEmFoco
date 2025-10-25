

#APIs de noticias ()
from serpapi import GoogleSearch

params = {
  "q": "pollution",
  "location": "Brazil",
  "hl": "pt",
  "gl": "br",
  "google_domain": "google.com.br",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()

