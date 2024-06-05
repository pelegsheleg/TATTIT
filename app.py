import streamlit as st
from pages.onboarding import onboarding_page
from pages.user_profile import user_profile_page
from pages.home import home_page
from pages.gallery import gallery_page
from pages.tattoo_detail import tattoo_detail_page
from pages.artist_profile import artist_profile_page
from pages.upload_match import upload_match_page

st.set_page_config(
    page_title="Tattit",
    page_icon="🖋️",
    layout="centered",
    initial_sidebar_state="expanded",
)

page_names_to_funcs = {
    "Onboarding": onboarding_page,
    "User Profile": user_profile_page,
    "Home": home_page,
    "Gallery/Explore": gallery_page,
    "Tattoo Detail": tattoo_detail_page,
    "Artist Profile": artist_profile_page,
    "Upload/Match": upload_match_page,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
