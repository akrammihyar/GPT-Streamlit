import streamlit as st
from model import GeneralModel
from pandas as pd
import random


def app():
    df = pd.read_csv("questions.csv")
    api_key = st.sidebar.text_input("APIkey", type="password")

    # Using the streamlit cache
    @st.cache
    if api_key:

        # Setting up the Title
        st.title("Card Game Generator")

        # st.write("---")

        s_example = " "
        input = st.text_area(
            "Enjoy!",
            value=s_example,
            max_chars=250,
            height=50,
        )

        if st.button("Generate"):
            question = df.sample(1)["question"].values[0]
            st.write("---")
            st.write(question)
            st.write("---")
                
    else:
        st.error("🔑 Please enter API Key")
