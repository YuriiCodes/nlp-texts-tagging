import spacy
from collections import Counter
from string import punctuation

# Завантажуємо модель spaCy
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, num_keywords=5):
    """
    Витягує ключові слова з тексту за допомогою spaCy.
    :param text: Текст для аналізу.
    :param num_keywords: Кількість ключових слів для повернення.
    :return: Список ключових слів.
    """
    doc = nlp(text.lower())  # Приводимо текст до нижнього регістру
    words = [token.text for token in doc if token.is_alpha and token.text not in nlp.Defaults.stop_words]
    word_freq = Counter(words)

    # Вилучаємо найчастотніші слова
    most_common = word_freq.most_common(num_keywords)
    return [word for word, freq in most_common]
