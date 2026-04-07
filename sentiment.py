import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

user_input = st.text_area("Enter your text:")

if st.button("Analyze"):
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        result = "Positive 😊"
    elif polarity < 0:
        result = "Negative 😞"
    else:
        result = "Neutral 😐"

    st.subheader("Result:")
    st.write(result)
    st.write("Polarity Score:", polarity)