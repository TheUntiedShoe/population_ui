"""
Creates a Streamlit interface for the data gathered in data.py
"""

import streamlit as st
import pandas as pd
from data import get_population

# create a session state to keep track of whether the table or chart is displayed
if "table" not in st.session_state:
    st.session_state.table = True

def display_as_table(population: dict) -> None:
    """
    Displays the data on the Streamlit page as a table
    Parameters:
        population: dict
    Returns: None
    """
    column_labels = ["Year", "Population"]
    table = pd.DataFrame(list(population.items()), columns=column_labels)
    st.dataframe(table)

def display_as_chart(population: dict) -> None:
    """
    Displays the data on the Streamlit page as a chart
    Parameters:
        population: dict
    Returns: None
    """
    st.line_chart(data=population, x_label="Years", y_label="US Population")

def toggle_session_state() -> None:
    """
    Toggles the value of streamlit's session state
    Returns: None
    """
    st.session_state.table = not st.session_state.table

st.set_page_config(page_title="US Population By Year")

population = get_population()

st.title("US Population By Year")

st.button("Toggle Display Method", on_click=toggle_session_state)

if st.session_state.table:
    # if state is true, then display the table
    st.empty()
    display_as_table(population)
else:
    # if state is false, then display the chart
    st.empty()
    display_as_chart(population)
