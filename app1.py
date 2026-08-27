import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('My first app')
a = st.number_input('Enter a number1')
b = st.number_input('Enter a number2')
#st.button('Add', key='add')
#st.button('Subtract',key='subtract')
#st.button('Multiply',key='multiply')
#st.button('Divide',key='divide')

if st.button('Add',key='add'):
    st.success(a + b)
if st.button('Subtract',key='subtract'):
    st.success(a - b)
if st.button('Multiply',key='multiply'):
    st.success(a * b)
if st.button('Divide',key='divide'):
    st.success(a / b)

