import streamlit as st

st.set_page_config(
    page_title="Youtube Harvesting",
    page_icon=":oops:",
)

st.title("Project Overview")
multi ="This project involves creating a Streamlit application for harvesting and warehousing data from multiple YouTube channels. The application offers a user-friendly interface for users to access, analyze, and store data from these channels. The data is stored in a MySQL database for structured data and a MongoDB database for unstructured data. This README will guide you through the project's workflow and how to run it."
st.markdown(multi)
st.sidebar.success("Select a page above.")
