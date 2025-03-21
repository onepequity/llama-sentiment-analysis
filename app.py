import streamlit as st
from sentiment_analysis import analyze_sentiment

st.title("LLaMA Sentiment Analysis Tool")
st.write("Enter customer feedback to analyze sentiment.")

feedback = st.text_area("Feedback")
if st.button("Analyze"):
    if feedback:
        label, score = analyze_sentiment(feedback)
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence:** {score:.2f}")
    else:
        st.write("Please enter some feedback.")