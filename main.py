import streamlit as st

from nlp.model import predict_job_title


JOBS_LINKS = {
    'Data Scientist': r'https://www.linkedin.com/jobs/view/3635238507/',
    'Full-Stack Developer': r'https://www.linkedin.com/jobs/view/3606000801/',
    'Software Developer': r'https://www.linkedin.com/jobs/view/3611699569/',
    'Cloud Engineer': r'https://www.linkedin.com/jobs/view/3606004754/',
    'Network Administrator': r'https://www.linkedin.com/jobs/view/3623816565/',
}

PRIMARY_COLOR = '#FFA500'
SECONDARY_COLOR = '#1E90FF'

st.set_page_config(page_title='Job Recommendation System', page_icon='💸')

st.markdown(
    f"""
    <style>
    body {{
        background-color: #F9F9F9;
        font-family: 'Montserrat', sans-serif;
    }}
    textarea {{
        background-color: #F0F0F0;
        border-radius: 10px;
        border: none;
        padding: 10px;
        margin-bottom: 20px;
        height: 200px;
        font-size: 16px;
        font-weight: 400;
        color: #333;
        resize: none;
    }}
    .btn-primary {{
        background-color: {PRIMARY_COLOR};
        color: #FFF;
        font-weight: 500;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 20px;
        margin-bottom: 40px;
    }}
    .btn-primary:hover {{
        background-color: darken({PRIMARY_COLOR}, 10%);
    }}
    .sidebar {{
        background-color: {SECONDARY_COLOR};
        color: #FFF;
    }}
    .sidebar .sidebar-content {{
        padding: 20px;
    }}
    .sidebar .sidebar-content .sidebar-section {{
        margin-bottom: 20px;
    }}
    .sidebar .sidebar-content .sidebar-section a {{
        color: #FFF;
        text-decoration: none;
        font-weight: 500;
    }}
    .sidebar .sidebar-content .sidebar-section a:hover {{
        text-decoration: underline;
    }}
    </style>
    """
    , unsafe_allow_html=True
)

st.image('images/banner.jpg', width=700)
st.title('Job Recommendation System')

st.sidebar.title('Menu')
rad = st.sidebar.radio(
    'Navigation Bar',
    ('Home', 'About Us')
)

if rad == 'Home':
    st.markdown(
        """
        Enter your skills below and we'll recommend the best matching jobs for you!
        """
    )

    skills = st.text_area('Enter your skills')

    if st.button('Get job recommendations', key='prediction_button'):
        predicted_title = predict_job_title(skills)
        predicted_link = JOBS_LINKS[predicted_title]
        st.success(f'Predicted job title: [{predicted_title}]({predicted_link})')


elif rad == 'About Us':
    st.markdown(
        """
        ## About Us

        We are a highly skilled and dedicated team of data scientists and software developers who are deeply 
        committed to empowering individuals to achieve their career goals. Our unwavering mission is to utilize 
        cutting-edge machine learning and natural language processing techniques to deliver personalized job 
        recommendations that perfectly align with each user's unique skillset and experience. By harnessing the power 
        of our advanced algorithms and industry expertise, we aim to revolutionize the job searching process and 
        provide unparalleled value to our users.
        """
    )

st.markdown(
    """
    ---

    Connect with us on [Kaggle](https://www.kaggle.com/ahmedkandeil) and [LinkedIn](
    https://www.linkedin.com/in/ahmed-kandil-/)!
    """
)
