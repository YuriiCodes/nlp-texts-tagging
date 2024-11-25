import streamlit as st
from db import create_table, add_text, get_texts, update_tags, search_texts
from crawler import crawl_wikipedia

# Ініціалізація бази даних
create_table()

st.title("Система накопичення текстів")

# Форма для додавання текстів
st.subheader("Додайте текст у базу даних")
with st.form("add_text_form"):
    text = st.text_area("Введіть текст")
    source = st.text_input("Джерело тексту (необов'язково)")
    tags = st.text_input("Теги (необов'язково; залиште порожнім для автоматичного генерування)")
    submitted = st.form_submit_button("Зберегти")

    if submitted:
        if text.strip():
            add_text(text, source, tags)
            st.success("Текст успішно збережено!")
        else:
            st.error("Поле тексту не може бути порожнім!")

# Відображення всіх текстів
st.subheader("Збережені тексти")
texts = get_texts()

if texts:
    for t in texts:
        st.write(f"**ID:** {t[0]}")
        st.write(f"**Текст:** {t[1][:200]}...")
        st.write(f"**Джерело:** {t[2]}")
        st.write(f"**Теги:** {t[3]}")

        # Додамо форму для редагування тегів
        with st.form(f"edit_tags_form_{t[0]}"):
            new_tags = st.text_input("Редагувати теги:", t[3])
            submitted = st.form_submit_button("Зберегти")
            if submitted:
                update_tags(t[0], new_tags)
                st.success(f"Теги для тексту ID {t[0]} оновлено!")
        st.markdown("---")
else:
    st.info("Немає збережених текстів.")

# Секція пошуку текстів
st.subheader("Пошук та фільтрація текстів")
query = st.text_input("Пошук за текстом (введіть ключове слово):")
filter_tag = st.text_input("Фільтр за тегом (введіть тег):")

if st.button("Пошук"):
    results = search_texts(query=query, tag=filter_tag)
    st.subheader("Результати пошуку")
    if results:
        for t in results:
            st.write(f"**ID:** {t[0]}")
            st.write(f"**Текст:** {t[1][:200]}...")
            st.write(f"**Джерело:** {t[2]}")
            st.write(f"**Теги:** {t[3]}")
            st.markdown("---")
    else:
        st.info("Результатів не знайдено.")



st.subheader("Краулер для Wikipedia")
# Поле для введення початкового URL
base_url = st.text_input("URL статті Wikipedia для початку краулінгу:", "https://en.wikipedia.org/wiki/Web_scraping")
# Поле для вибору глибини
depth = st.slider("Глибина переходів за посиланнями", 1, 3, 1)
# Поле для обмеження кількості статей
max_articles = st.number_input("Максимальна кількість статей (0 - без обмежень):", min_value=0, step=1, value=0)

# Кнопка для запуску краулера
if st.button("Запустити краулер"):
    st.info("Краулер виконується, зачекайте...")
    texts = crawl_wikipedia(base_url, depth=depth, max_articles=(max_articles if max_articles > 0 else None))

    if texts:
        for t in texts:
            add_text(t['text'], t['url'], None)
        st.success(f"Краулер завершив роботу! Зібрано {len(texts)} статей.")
    else:
        st.warning("Не вдалося знайти текст для збереження.")

# Відображення збережених текстів
st.subheader("Усі збережені тексти")
texts = get_texts()

if texts:
    for t in texts:
        st.write(f"**ID:** {t[0]}")
        st.write(f"**Текст:** {t[1]}")
        st.write(f"**Джерело:** {t[2]}")
        st.write(f"**Теги:** {t[3]}")
        st.markdown("---")
else:
    st.info("Немає збережених текстів.")
