import streamlit as st

def tattoo_detail_page():
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

    st.title("Tattoo Detail")
    st.image("https://images.unsplash.com/photo-1512253562774-5ad99d3f0c1a", use_column_width=True)
    st.write("## Tattoo Design Title")
    st.write("Detailed view of a selected tattoo design. Information about the design and the artist.")
    
    st.subheader("Artist Information")
    st.write("Artist Name: John Doe")
    st.write("Artist Bio: Experienced tattoo artist specializing in realism.")
    
    st.write("### Actions")
    like_button = st.button("Like")
    share_button = st.button("Share")
    save_button = st.button("Save")
    
    if like_button:
        st.success("You liked this design.")
    if share_button:
        st.success("Share functionality to be implemented.")
    if save_button:
        st.success("Design saved to your profile.")
    
    st.subheader("User Reviews and Ratings")
    st.write("Feature to display user reviews and ratings will be implemented here.")

    st.subheader("Similar Designs")
    st.write("Feature to display similar designs will be implemented here.")
