import pprint
import google.generativeai as palm
import streamlit as st
st.set_page_config(page_title='ChatDictionary',layout='wide')

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


API_KEY = 'AIzaSyC0vpxE7ypq10Qf3NbiaQLgdOvvWfK34CA'
palm.configure(api_key=API_KEY)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
st.title("Chat Dictionary")
st.subheader("Unleash the potential of Large Language Models")
word = st.text_input("Type the word")
options = ['General', 'Law', 'Medicine', 'Science', 'Technology', 'Business',
           'Finance', 'Sports', 'Arts', 'Literature', 'History', 'Philosophy']
context = st.selectbox("Choose The Context", options=options)
temperature = st.slider('How much creative you want me to be', min_value=0, max_value=10, help="Higher the creativity "
                                                                                               "The Less Exact answer"
                                                                                               " or more variation in "
                                                                                               "the result ")


st.button(label="Search")

prompt = (f"Give me the meaning of the word {word} in the context of {context}, along with its synonyms, antonyms, "
          f"and use cases also give a short essay or story wherein the word is used")

if st.button:
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=temperature / 10,
        # The maximum length of the response
        max_output_tokens=800,
    )
    st.write(completion.result)

