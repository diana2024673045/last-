import streamlit as st
import analyzer
import data

st.set_page_config(page_title="Personality Analyzer", page_icon="💡")

language = st.sidebar.selectbox("Language / 언어", ["English", "한국어"])

if language == "English":
    st.title("Personality Analyzer 🌟")
    mbti = st.selectbox("Select your MBTI", data.mbti_types)
    zodiac = st.selectbox("Select your Zodiac Sign", data.zodiac_signs)
    animal = st.selectbox("Select your Eastern Animal Sign", data.animal_signs)
    if st.button("Analyze"):
        st.markdown(analyzer.analyze_personality(mbti, zodiac, animal, "en"), unsafe_allow_html=True)

else:
    st.title("성격 분석기 🌟")
    mbti = st.selectbox("MBTI를 선택하세요", data.mbti_types)
    zodiac = st.selectbox("별자리를 선택하세요", data.zodiac_signs_kr)
    animal = st.selectbox("띠를 선택하세요", data.animal_signs_kr)
    if st.button("분석하기"):
        st.markdown(analyzer.analyze_personality(mbti, zodiac, animal, "kr"), unsafe_allow_html=True)
