import streamlit as st
from elevenlabs import generate, play, voices
from elevenlabs.api.error import UnauthenticatedRateLimitError, RateLimitError

st.image(image='./LOGO-eleven-labs.png',
         caption="Model supports multiple languages, including English, German, Polish, Spanish, Italian, French, Portuguese, and Hindi.")

with st.sidebar:
    st.title("Text to Voice")
    english = st.radio(
        label="Choose your language", options=['English', 'Multilingual'], index=0, horizontal=True)

    value = "I am the machine." if english == 'English' else "बस बातें अपने जैसे करते है"
    text = st.text_area(label="Enter the text here",
                        value=value, max_chars=100)
    voice = st.selectbox(
        label="Choose the voice", options=[v.name for v in voices()]
    )
    st.divider()
    with st.expander(label="llElevenLabs", expanded=True):
        st.caption(
            "The basic API has a limited number of characters. To increase this limit, you can get a free API key from [llElevenLabs](https://beta.elevenlabs.io/subscription)")
        API_KEY = st.text_input(label="API KEY")

try:
    audio = generate(text=text, voice=voice, model='eleven_multilingual_v1',
                     api_key=API_KEY if API_KEY else None)
    st.audio(data=audio)
except UnauthenticatedRateLimitError:
    e = UnauthenticatedRateLimitError("Unauthenticated Rate Limit Error")
    st.exception(e)

except RateLimitError:
    e = RateLimitError('Rate Limit')
    st.exception(e)
