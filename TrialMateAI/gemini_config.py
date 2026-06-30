"""
gemini_config.py
Configuration file for TrialMate AI
"""
import os
import streamlit as st

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
