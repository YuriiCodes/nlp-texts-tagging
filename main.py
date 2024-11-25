import streamlit as st
from db import create_table, add_text, get_texts

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

# Відображення збережених текстів
st.subheader("Збережені тексти")
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
