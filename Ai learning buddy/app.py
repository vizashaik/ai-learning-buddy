import streamlit as st
from ai_helper import get_ai_response

st.set_page_config(page_title="AI Learning Buddy", page_icon="🤖")

st.title("🤖 AI Learning Buddy")
st.write("Learn any topic with AI!")

topic = st.text_input("Enter a topic")

activity = st.selectbox(
    "Choose an activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Quiz",
        "Feedback"
    ]
)

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if activity == "Explain Topic":
            prompt = f"Explain {topic} in simple language."

        elif activity == "Real-Life Example":
            prompt = f"Give one real-life example of {topic}."

        elif activity == "Quiz":
            prompt = f"Generate 5 quiz questions with answers on {topic}."

        else:
            prompt = f"Give feedback to a beginner learning {topic}."

        with st.spinner("Generating response..."):
            response = get_ai_response(prompt)

        st.success("Done!")
        st.write(response)