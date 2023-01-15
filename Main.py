import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Card Game Generator")

        # st.write("---")

        s_example = " "
        input = st.text_area(
            "Enjoy!",
            value=s_example,
            max_chars=500,
            height=50,
        )

        if st.button("Generate"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
                
        if st.button("Next Card"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
                
    else:
        st.error("🔑 Please enter API Key")
