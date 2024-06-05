import streamlit as st
import base64
from PIL import Image

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_image_as_page_bg(image_file, image_format='png'):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = f'''
    <style>
    body {{
    background-image: url("data:image/{image_format};base64,{bin_str}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

def onboarding_page():
    # Set the background image
    set_image_as_page_bg(r"C:\Users\peleg\OneDrive\Desktop\tattit_app\IMG_20220926_134029.jpg", 'jpg')

    # Apply custom CSS styles
    st.markdown(f"""
        <style>
        .main {{
            background-color: #1E1E1E;
            color: white;
        }}
        .stButton button {{
            background-color: #FF6B6B;
            color: white;
            border: none;
            border-radius: 10px;
            transition: background-color 0.3s ease;
            padding: 15px 30px;
            font-size: 18px;
        }}
        .stButton button:hover {{
            background-color: #FF4B4B;
        }}
        .stTextInput > div > input {{
            background-color: #2C2C2C;
            color: white;
            border: none;
            padding: 15px;
            border-radius: 10px;
        }}
        .stTitle {{
            font-size: 36px;
            font-weight: bold;
        }}
        .stSubtitle {{
            font-size: 24px;
            margin-bottom: 30px;
        }}
        .header-image {{
            width: 100%;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .intro-text {{
            font-size: 20px;
            margin-bottom: 30px;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        </style>
        """, unsafe_allow_html=True)

    # HTML content
    st.markdown(f"""
        <div class="container">
            <div class="stTitle">TATTIT</div>
            <div class="stSubtitle">Simply Choose</div>
            <div class="stSubtitle">Your Next Tattoo</div>
            <div class="intro-text">Artist</div>
            <div class="intro-text">Explore Unique Designs</div>
            <div class="intro-text">Unlock and save your favorite tattoo designs and artists.</div>
        </div>
    """, unsafe_allow_html=True)

    # Buttons for navigation
    if st.button("Get Started Now"):
        st.write("Choose a method to sign up or log in:")
        if st.button("Sign Up"):
            st.write("Choose a method to sign up:")
            st.button("Sign Up with Email", key="signup_email")
            st.button("Sign Up with Google", key="signup_google")
            st.button("Sign Up with Facebook", key="signup_facebook")
            st.button("Sign Up with Apple ID", key="signup_apple")

        if st.button("Login"):
            st.write("Choose a method to log in:")
            st.button("Login with Email", key="login_email")
            st.button("Login with Google", key="login_google")
            st.button("Login with Facebook", key="login_facebook")
            st.button("Login with Apple ID", key="login_apple")

        st.button("Skip Login and Explore as Guest", key="skip_login")


