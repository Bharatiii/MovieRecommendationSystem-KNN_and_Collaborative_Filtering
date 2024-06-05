import streamlit as st
import subprocess

# Define the title and page layout
st.set_page_config(page_title="Movie Recommendation App", layout="wide")

col1, col2 = st.columns([0.1, 1])
with col1:
    if st.button("About"):
        st.markdown('<a href="about.html" target="_blank">About</a>', unsafe_allow_html=True)
with col2:
    if st.button("Contact Us"):
        st.markdown('<a href="contact.html" target="_blank">Contact Us</a>', unsafe_allow_html=True)

st.markdown(
    """
<style>

.stApp {
background-image: url("https://pointerclicker.com/wp-content/uploads/2022/12/A-TV-with-bias-lighting-behind-960x960.jpg");
background-size: cover;
}
.reportview-container .markdown-text-container {
    font-family: monospace;
    
    
    background-size: cover;
    {
    background-color: rgba(0, 0, 0, 0);
    }
}
.stHeader {
    background-color: rgba(0, 0, 0, 0);
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: linear-gradient(#2e7bcf,#2e7bcf);
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #38ACEC;
}

</style>
""",
    unsafe_allow_html=True,
)


# Sidebar navigation
st.sidebar.title("Navigation")
app_selection = st.sidebar.radio("Select App", ("Collaborative Filtering", "K-Nearest Neighbors"))

# Main content
st.title("Movie Recommendation App")

# Define function to run Streamlit apps
def run_streamlit_app(app_path):
    subprocess.Popen(["streamlit", "run", app_path])

# Load selected app based on user's choice
if app_selection == "Collaborative Filtering":
    st.markdown("## Collaborative Filtering App")
    st.write("This app uses collaborative filtering to recommend movies.")
    st.write("To run this app, please click the button below:")
    if st.button('Run Collaborative Filtering App'):
        run_streamlit_app("app_CF.py")

elif app_selection == "K-Nearest Neighbors":
    st.markdown("## K-Nearest Neighbors App")
    st.write("This app uses K-nearest neighbors algorithm to recommend movies.")
    st.write("To run this app, please click the button below:")
    if st.button('Run K-Nearest Neighbors App'):
        run_streamlit_app("app_KNN.py")

