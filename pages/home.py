import streamlit as st

def home_page():
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
        .stTextInput > div > input {
            background-color: #222;
            color: white;
            border: none;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Home")
    st.write("### Main navigation hub.")
    
    st.subheader("Featured Tattoo Designs")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1508174448729-57d16890c4d9", use_column_width=True)
        st.button("View Design 1")
    with col2:
        st.image("https://images.unsplash.com/photo-1512253562774-5ad99d3f0c1a", use_column_width=True)
        st.button("View Design 2")
    with col3:
        st.image("https://images.unsplash.com/photo-1520611632994-8aa1f22d19b2", use_column_width=True)
        st.button("View Design 3")
    
    st.subheader("Search for Designs or Artists")
    search_query = st.text_input("Search...", placeholder="Type to search...")
    voice_search_button = st.button("Voice Search")
    search_button = st.button("Search")
    if search_button:
        st.write("Search results for:", search_query)

    st.subheader("Personalized Recommendations")
    st.write("Feature to display personalized recommendations will be implemented here.")

    st.subheader("Interactive Categories and Tags")
    st.write("Interactive categories and tags with hover effects and clickable filters will be implemented here.")

    st.write("### Quick Access")
    st.button("Notifications")
    st.button("Messages")
    st.button("User Profile")
