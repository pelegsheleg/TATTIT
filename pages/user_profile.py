import streamlit as st
from streamlit_tags import st_tags

def user_profile_page():
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

    st.title("User Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Profile Picture")
        profile_pic = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])
        if profile_pic is not None:
            st.image(profile_pic, width=150)
    
    with col2:
        st.subheader("User Information")
        user_name = st.text_input("Name")
        user_bio = st.text_area("Bio")
        user_preferences = st_tags(
            label='Preferences:',
            text='Press enter to add more',
            value=['Traditional', 'Watercolor'],
            suggestions=['Black & Grey', 'Realism', 'Abstract', 'Neo-traditional'],
            maxtags=5,
        )
        social_media = st_tags(
            label='Social Media:',
            text='Press enter to add more',
            value=['@instagram'],
            suggestions=['@facebook', '@twitter', '@tiktok'],
            maxtags=5,
        )
        update_button = st.button("Update Profile")
        if update_button:
            st.success("Profile updated successfully")

    st.subheader("Saved Designs and Match History")
    st.write("Feature to display saved designs and match history will be implemented here.")

    st.subheader("Privacy Settings")
    st.checkbox("Make profile public")
