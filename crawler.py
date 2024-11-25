import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_wikipedia(base_url, depth=1):
    """
    Краулер для Wikipedia, який збирає текст зі сторінки та наступних посилань.
    :param base_url: URL статті Wikipedia, з якої починається парсинг.
    :param depth: Глибина переходів за посиланнями.
    :return: Список текстів статей.
    """
    visited = set()
    texts = []

    def crawl(url, current_depth):
        if current_depth > depth or url in visited:
            return
        visited.add(url)

        try:
            # Завантаження сторінки
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Отримання заголовка статті
            title = soup.find('h1', id='firstHeading').get_text(strip=True)

            # Отримання тексту основної статті
            content = soup.find('div', id='bodyContent')
            paragraphs = content.find_all('p')
            text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

            # Збереження тексту статті
            if text:
                texts.append({
                    'title': title,
                    'text': text,
                    'url': url
                })

            # Переходи за посиланнями (обмежуємо до Wikipedia)
            links = content.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('/wiki/') and not href.startswith('/wiki/Special:'):
                    next_url = urljoin(base_url, href)
                    crawl(next_url, current_depth + 1)
        except Exception as e:
            print(f"Помилка при обробці {url}: {e}")

    crawl(base_url, 0)
    return texts
