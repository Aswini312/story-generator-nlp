import os
import streamlit as st
import google.generativeai as genai

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #4b9bfa;
        }
        .stTextArea textarea {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #4b9bfa;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 8px 16px;
        }
        .stButton > button:hover {
            background-color: #357abf;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    """
    Main function to run the Streamlit app for story generation.
    """
    # Add custom CSS
    add_custom_css()

    # Set your Gemini API key directly here
    api_key = 'AIzaSyC4uuDvckQovU60PCjhErx9SQ3GO6krwb0'
    genai.configure(api_key=api_key)

    # Set up the Streamlit interface
    st.title("🌟 Story Generator")

    # Sidebar with instructions
    st.sidebar.header("Instructions")
    st.sidebar.write("""
    1. Enter a theme or style for the story.
    2. Click 'Generate Story' to get your story.
    3. Enjoy your personalized story!
    """)

    # User input for story prompt
    user_prompt = st.text_area(
        "Please describe the theme or style of the story you want",
        height=100,
        placeholder="e.g., A sci-fi adventure in a distant galaxy..."
    )

    # Button to generate the story
    if st.button("Generate Story"):
        if user_prompt.strip():
            # Create a prompt for generating the story
            prompt = f"""
            Generate a story based on the following theme or style:

            "{user_prompt}"

            Provide a creative and original story.
            """

            try:
                # Generate the story using the Google Generative AI model
                response = genai.generate_text(prompt=prompt)

                # Extract the generated story from the 'candidates' list
                generated_story = response.candidates[0]['output']

                # Display the generated story
                st.subheader("📖 Your Generated Story")
                st.write(generated_story)

            except Exception as e:
                st.error(f"An error occurred while generating the story: {e}")
        else:
            st.warning("Please enter a prompt to generate a story.")

    
            

if __name__ == "__main__":
    main()




