from fastapi import FastAPI, Query
from db import search_texts

app = FastAPI()

@app.get("/articles")
def get_filtered_articles(query: str = Query(None, description="Ключове слово для пошуку у текстах"),
                          tag: str = Query(None, description="Тег для пошуку у статтях")):
    """
    Ендпоінт для отримання статей із можливістю фільтрації за ключовим словом або тегом.
    :param query: Ключове слово для пошуку у тексті статей.
    :param tag: Тег для пошуку статей.
    :return: Відфільтрований список статей.
    """
    articles = search_texts(query=query, tag=tag)
    return [
        {
            "id": article[0],
            "text": article[1],
            "source": article[2],
            "tags": article[3]
        }
        for article in articles
    ]
