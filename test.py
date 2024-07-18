import streamlit as st

# Title of the app
st.title('Simple Streamlit App for Testing')

# Text input field
user_input = st.text_input("Enter some text:")

# Button to display the input text
if st.button('Display Text'):
    if user_input:
        st.write(f'You entered: {user_input}')
    else:
        st.write('Please enter some text to display.')

# A simple slider
slider_value = st.slider("Select a number:", 0, 100, 50)
st.write(f'Slider value is: {slider_value}')

# A selectbox to choose a color
color = st.selectbox('Choose a color:', ['Red', 'Green', 'Blue'])
st.write(f'You selected: {color}')
