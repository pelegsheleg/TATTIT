import streamlit as st

def artist_profile_page():
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

    st.title("Artist Profile")
    st.image("https://images.unsplash.com/photo-1520611632994-8aa1f22d19b2", width=200)
    
    st.write("## John Doe")
    st.write("Experienced tattoo artist specializing in realism and traditional styles.")
    
    st.subheader("Portfolio")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1508174448729-57d16890c4d9", use_column_width=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1512253562774-5ad99d3f0c1a", use_column_width=True)
    with col3:
        st.image("https://images.unsplash.com/photo-1520611632994-8aa1f22d19b2", use_column_width=True)
    
    st.subheader("Ratings and Reviews")
    st.write("★★★★★ 5.0 (20 reviews)")
    
    st.subheader("Contact/Booking Options")
    contact_button = st.button("Contact Artist")
    booking_button = st.button("Book an Appointment")
    if contact_button:
        st.write("Contact form to be implemented.")
    if booking_button:
        st.write("Booking functionality to be implemented.")
    
    st.subheader("Availability Calendar")
    st.write("Feature to display the artist's availability calendar will be implemented here.")
    
    st.subheader("Social Media Links")
    st.write("Feature to display social media links and website will be implemented here.")
