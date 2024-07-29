# import streamlit as st
# from prediction_page import show_predict_page
# from diameter_page import show_diameter_page

# st.set_page_config(layout="wide")

# page = st.sidebar.selectbox("Choose a page", ["Prediction", "Diameter Measurement"])

# if page == "Prediction":
#     show_predict_page()
# else:
#     show_diameter_page()

import streamlit as st
from prediction_page import show_predict_page
from diameter_page import show_diameter_page

# Set the layout to wide
st.set_page_config(layout="wide")

# Sidebar for page navigation with radio buttons
page = st.sidebar.radio("Choose a page", ["Defect Detection", "Diameter Measurement"])

# Display the selected page
if page == "Defect Detection":
    show_predict_page()
elif page == "Diameter Measurement":
    show_diameter_page()




# import streamlit as st
# from prediction_page import show_predict_page
# from diameter_page import show_diameter_page

# # Set the layout to wide
# #st.set_page_config(layout="wide")

# # Simulate authentication state
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# def login(username, password):
#     # Dummy authentication logic
#     if username == "user" and password == "password":
#         st.session_state.logged_in = True
#     else:
#         st.error("Invalid username or password")

# def logout():
#     st.session_state.logged_in = False

# # Title Bar
# st.markdown("""
#     <style>
#     .title-bar {
#         background-color: #333;
#         color: white;
#         padding: 10px;
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#     }
#     .title-bar h1 {
#         margin: 0;
#     }
#     .title-bar a {
#         color: white;
#         text-decoration: none;
#         margin-left: 15px;
#     }
#     .title-bar a:hover {
#         text-decoration: underline;
#     }
#     </style>
#     <div class="title-bar">
#         <h1>My Website</h1>
#         <div>
#             {}
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# # Login/Logout Buttons
# if st.session_state.logged_in:
#     if st.button('Logout'):
#         logout()
#         st.experimental_rerun()
# else:
#     username = st.text_input('Username')
#     password = st.text_input('Password', type='password')
    
#     if st.button('Login'):
#         login(username, password)
#         st.experimental_rerun()

# # Display content based on authentication
# if st.session_state.logged_in:
#     # Sidebar for page navigation with radio buttons
#     page = st.sidebar.radio("Choose a page", ["Prediction", "Diameter Measurement"])

#     # Display the selected page
#     if page == "Prediction":
#         show_predict_page()
#     elif page == "Diameter Measurement":
#         show_diameter_page()
# else:
#     st.write("Please log in to access the content.")




