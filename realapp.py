import streamlit as st
def display_chat_history():
    """Display the chat history in the sidebar."""

    # Create a separate layout for the chat history
    chat_history_layout = st.sidebar.container()

    # Display the chat history in the separate layout
    with chat_history_layout:
        st.subheader("Chat History")
        for role, text in st.session_state['chat_history']:
            st.write(f"{role}: {text}")


    # Add CSS styling to the chat history layout
    chat_history_layout.markdown(
        """
        <style>
        #chat_history {
            background-color: #efefef;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

