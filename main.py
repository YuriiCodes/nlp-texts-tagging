import streamlit as st
from db import create_table, add_text, get_texts, search_texts

# Створення бази даних при запуску
create_table()

st.title("Система накопичення текстів")
st.subheader("Додайте текст у базу даних")

# Форма для додавання текстів
with st.form("add_text_form"):
    text = st.text_area("Введіть текст")
    source = st.text_input("Джерело тексту (необов'язково)")
    tags = st.text_input("Теги (через кому, наприклад: навчання, стаття)")
    submitted = st.form_submit_button("Зберегти")

    if submitted:
        if text.strip():
            add_text(text, source, tags)
            st.success("Текст успішно збережено!")
        else:
            st.error("Поле тексту не може бути порожнім!")


# Секція пошуку текстів
st.subheader("Пошук та фільтрація текстів")

# Поля для пошуку
query = st.text_input("Пошук за текстом (введіть ключове слово):")
filter_tag = st.text_input("Фільтр за тегом (введіть тег):")

# Кнопка для виконання пошуку
if st.button("Пошук"):
    results = search_texts(query=query, tag=filter_tag)
    st.subheader("Результати пошуку")
    if results:
        for t in results:
            st.write(f"**ID:** {t[0]}")
            st.write(f"**Текст:** {t[1]}")
            st.write(f"**Джерело:** {t[2]}")
            st.write(f"**Теги:** {t[3]}")
            st.markdown("---")
    else:
        st.info("Результатів не знайдено.")
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
