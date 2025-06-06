import streamlit as st

st.title("Human Health Analysis Assistant")

user_input = st.text_area("Enter your lifestyle details or health-related question:")

if st.button("Analyze"):
    # Placeholder response (you can connect your AI model here)
    st.write("Analyzing your input...")
    # Example output
    st.success("You may be experiencing fatigue due to poor sleep. Consider improving sleep hygiene.")

st.markdown("**Disclaimer**: This assistant does not provide medical advice. Always consult a healthcare provider.")
