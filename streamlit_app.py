import streamlit as st
import pandas as pd

# Load data
hitters_df = pd.read_csv("d2_draft_bat.csv")
pitchers_df = pd.read_csv("d2_draft_pitch.csv")

# App Title
st.title("Potential D2 Draftees")

# Tabs for Hitters and Pitchers
tab1, tab2 = st.tabs(["Hitters", "Pitchers"])

with tab1:
    st.header("Potential D2 Position Player Draftees")
    st.dataframe(hitters_df, use_container_width=True)

with tab2:
    st.header("Potential D2 Pitcher Draftees")
    st.dataframe(pitchers_df, use_container_width=True)
