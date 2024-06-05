import streamlit as st

def main():
    st.set_page_config(page_title="About Us - Movie Recommender", page_icon=":movie_camera:")

    # CSS styles
    st.markdown(
        """
        <style>
            .stApp {
                background-image: url("https://pointerclicker.com/wp-content/uploads/2022/12/A-TV-with-bias-lighting-behind-960x960.jpg");
                background-size: cover;
            }
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                color: rgb(172, 160, 137);
                background-color: azure;
            }
            .bg {
                position: absolute;
                right: 0;
                bottom: 0;
                z-index: -1;
                opacity: 90%;
                width: 100%;
            }
            header {
                text-align: center;
                padding: 20px 0;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            section {
                margin-bottom: 40px;
            }
            h2 {
                color: #007bff;
                margin-bottom: 10px;
            }
            p {
                margin-bottom: 20px;
            }
            .team-member {
                text-align: center;
            }
            .team-member img {
                width: 150px;
                border-radius: 50%;
                margin-bottom: 10px;
            }
            footer {
                text-align: center;
                padding: 20px 0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # st.image("1.jpg", output_format='JPG', width=None, use_column_width=True, caption=None, clamp=False, channels='RGB')

    st.header("About Us")

    st.markdown(
        """
        <div class="container">
            <section>
                <h2>Our Mission</h2>
                <p>We are passionate about movies and believe that everyone deserves to find movies they'll love. Our
                    mission is to provide personalized movie recommendations tailored to each user's unique preferences. By
                    leveraging advanced algorithms and user feedback, we strive to deliver accurate and enjoyable movie
                    suggestions, helping users discover hidden gems and popular hits alike. Whether you're a casual
                    moviegoer or a dedicated cinephile, we're here to enhance your movie-watching experience and broaden
                    your cinematic horizons.</p>
            </section>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="container">
            <section>
                <h2>Our Team</h2>
                <div class="team-member">
                    <h3>Abu Said Akunji (21053263)</h3>
                </div>
                <div class="team-member">
                    <h3>Komalika Das (21053418)</h3>
                </div>
                <div class="team-member">
                    <h3>Bharati Majumder (2105189)</h3>
                </div>
                <div class="team-member">
                    <h3>Fariya Afrin()</h3>
                </div>
                <div class="team-member">
                    <h3>Rahul Dev Mallick()</h3>
                </div>
            </section>
        </div>
        <footer>
            <p>&copy; 2024 | Movie Recommender. All rights reserved.</p>
          </footer>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()