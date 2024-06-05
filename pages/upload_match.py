import streamlit as st
from streamlit_tags import st_tags

def upload_match_page():
    st.markdown("""
        <style>
        .main {
            background-color: #111;
            color: white;
        }
        .stButton button {
            background-color: #00cc66;
            color: white;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #00994d;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Upload/Match")
    st.write("### Upload an image or screenshot for matching.")
    
    upload_option = st.selectbox("Choose an option", ["Upload a Picture", "Take a Picture on the Spot", "Take a Screenshot", "Select from Gallery App"])
    if upload_option == "Upload a Picture":
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            st.image(uploaded_image, use_column_width=True)
    elif upload_option == "Take a Picture on the Spot":
        st.write("Functionality to take a picture on the spot will be implemented here.")
    elif upload_option == "Take a Screenshot":
        st.write("Functionality to take a screenshot will be implemented here.")
    elif upload_option == "Select from Gallery App":
        st.write("Functionality to select from gallery app will be implemented here.")
    
    st.write("### Input your preferences")
    preferences = st_tags(
        label='Preferences:',
        text='Press enter to add more',
        value=['Traditional', 'Watercolor'],
        suggestions=['Black & Grey', 'Realism', 'Abstract', 'Neo-traditional'],
        maxtags=5,
    )
    location_pref = st.text_input("Location (e.g., New York, LA)")
    price_range_pref = st.selectbox("Price Range", ["$50 - $100", "$100 - $200", "$200 - $500", "$500+"])
    
    match_button = st.button("Find Matching Artists")
    if match_button:
        st.write(f"Finding artists matching your preferences: {preferences}, {location_pref}, {price_range_pref}")
        st.write("Feature to display matching artists and designs will be implemented here.")

    st.subheader("Map Interface")
    st.write("Feature to display an interactive map showing matching artists will be implemented here.")

    st.subheader("Match Preview")
    st.write("Feature to show a preview of the uploaded image and the matching designs will be implemented here.")
    
    st.subheader("Details and Contact")
    st.write("Feature to view details of each match, including information about the artist, their portfolio, and contact options will be implemented here.")
    st.write("Feature to allow booking functionality directly from the match results will be implemented here.")
