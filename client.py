"""
Streamlit App for Questioning

A simple Streamlit application that allows users to input a question,
submits it to an API endpoint, and displays the answers received from
different clients (countries) along with a final global answer.
"""

import json
import streamlit as st
import requests


def ask_question(question):
    """
    Send a question to the API endpoint and retrieve the answer.

    Args:
    - question: A string containing the user's question.

    Returns:
    - A string containing the JSON response from the API.
    """
    response = requests.post("http://localhost:5999/ask", json={"question": question})
    return response.text


def escape_markdown(text):
    """
    Escape special characters in a text string for Markdown formatting.

    Args:
    - text: A string containing text to be escaped.

    Returns:
    - A string with special characters escaped for Markdown formatting.
    """
    # Characters to escape in markdown
    special_chars = [
        "\\",
        "`",
        "*",
        "_",
        "{",
        "}",
        "[",
        "]",
        "(",
        ")",
        "#",
        "+",
        "-",
        ".",
        "!",
        "$",
    ]
    for char in special_chars:
        text = text.replace(char, "\\" + char)
    return text


# App UI
st.title("Ask a Question")

question = st.text_area("Global question:")

if st.button("Submit"):
    with st.spinner("Wait for it..."):
        response = ask_question(question)

    response_dict = json.loads(response)

    responses = {
        answer["user_id"]: (answer["question"], answer["answer"])
        for answer in response_dict["answers"]
    }

    clients_info = {
        0: {"name": "Norway", "flag": "materials/Flag_of_Norway.svg.png"},
        1: {"name": "Sweden", "flag": "materials/Flag_of_Sweden.svg.png"},
        2: {"name": "Denmark", "flag": "materials/Flag_of_Denmark.svg.png"},
    }

    for i, col in enumerate(st.columns(3)):
        with col:
            client = clients_info[i]
            st.subheader(f"Client {i+1}: {client['name']}")
            st.image(client["flag"])
            st.text("Local question:")
            st.markdown(escape_markdown(responses[i][0]))
            st.divider()
            st.text("Local answer:")
            st.markdown(escape_markdown(responses[i][1]))

    st.subheader("Global answer:")
    st.markdown(escape_markdown(response_dict["final_answer"]))

else:
    st.header("How It Works")
    st.image("materials/howitworks.png")
