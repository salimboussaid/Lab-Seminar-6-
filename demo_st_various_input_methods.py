import streamlit as st

st.title("Streamlit Demo: Input Data")

# Slider
st.subheader("Slider Example")
slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Slider value:", slider_value)

# Text Field
st.subheader("Text Field Example")
text_input = st.text_input("Enter some text")
st.write("Text input:", text_input)

# Drop-down Menu
st.subheader("Drop-down Menu Example")
dropdown_value = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write("Dropdown value:", dropdown_value)

# Button
st.subheader("Button Example")
if st.button("Click Me"):
    st.write("Button was clicked!")

# Checkbox
st.subheader("Checkbox Example")
checkbox_value = st.checkbox("Check me")
st.write("Checkbox value:", checkbox_value)

# Radio Buttons
st.subheader("Radio Button Example")
radio_value = st.radio("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write("Radio button value:", radio_value)

# Display Messages
st.success("Success message")
st.info("Info message")
st.warning("Warning message")
st.error("Error message")
