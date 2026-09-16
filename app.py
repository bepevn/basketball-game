import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="🏀 Dunk Master",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_path = Path(__file__).parent / "game.html"

with open(html_path, "r", encoding="utf-8") as f:
    game_html = f.read()

components.html(
    game_html,
    height=850,
    scrolling=False
)
