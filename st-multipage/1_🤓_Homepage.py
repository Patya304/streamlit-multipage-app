import streamlit as st

st.set_page_config(
    page_title = "Multipage App",
    page_icon = "✌",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Kérem a szöveget", st.session_state["my_input"])
submit = st.button("Küldés")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Amit megadtál szöveg: ", my_input)