import streamlit as st

def gallery_page():
    # CSS styles
    st.markdown("""
        <style>
        * {
          box-sizing: border-box;
        }

        body {
          margin: 0;
          font-family: sans-serif;
          background: #f5f6f7;
        }

        .header {
          text-align: center;
          text-transform: uppercase;
          padding: 32px;
          background-color: #0a0a23;
          color: #fff;
          border-bottom: 4px solid #fdb347;
        }

        .gallery {
          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
          justify-content: center;
          align-items: center;
          gap: 16px;
          max-width: 1400px;
          margin: 0 auto;
          padding: 20px 10px;
        }

        .gallery img {
          width: 100%;
          max-width: 350px;
          height: 300px;
          object-fit: cover;
          border-radius: 10px;
        }

        .gallery::after {
          content: "";
          width: 350px;
        }

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

    # Header
    st.markdown('<div class="header"><h1>Gallery/Explore</h1></div>', unsafe_allow_html=True)
    
    # Filters
    st.write("### Browse through tattoo designs.")
    st.subheader("Filters")
    col1, col2, col3 = st.columns(3)
    with col1:
        style_filter = st.selectbox("Style", ["Traditional", "Realism", "Watercolor", "Abstract"])
    with col2:
        size_filter = st.selectbox("Size", ["Small", "Medium", "Large"])
    with col3:
        color_filter = st.selectbox("Color", ["Black & Grey", "Colorful"])
    
    filter_button = st.button("Apply Filters")
    if filter_button:
        st.write(f"Showing {style_filter} tattoos, {size_filter} size, {color_filter} color")
    
    # Gallery
    st.subheader("Trending Designs")
    st.markdown('<div class="gallery">', unsafe_allow_html=True)
    for i in range(5):
        st.markdown(f'''
            <div>
                <img src="https://cdn.freecodecamp.org/curriculum/css-photo-gallery/9.jpg" alt="Tattoo Design {i}">
                <button>View Details</button>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### Infinite Scrolling")
    st.write("Feature to implement infinite scrolling will be here.")

# Main Script
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    gallery_page()
