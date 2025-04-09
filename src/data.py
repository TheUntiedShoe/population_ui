"""
Gets data on the US population per year from the web
"""

from requests import get
import streamlit as st

def get_population() -> dict:
    """
    Accesses a web API to get data on the US population per year
    Returns a dictionary with years as keys and population as values
    """
    try:
        # get the data from the web and format it as json
        data = get('https://datausa.io/api/data?drilldowns=Nation&measures=Population').json()

        # this function doesn't need to return as much data as it gathered
        years = [i["Year"] for i in data["data"]] # this list contains all the years from the api in descending order
        populations = [i["Population"] for i in data["data"]] # this list contains all the population values corresponding to the years

        # this returns a dictionary with the values from the "years" list as keys and the "populations" list as values
        return dict(zip(years, populations))

    except Exception as e:
        # if the function encounters an exception, have streamlit throw the error and return an empty dictionary
        st.error(str(e))
        return {}
    