import streamlit as st
from elevenlabs import generate, play, voices
from elevenlabs.api.error import UnauthenticatedRateLimitError, RateLimitError

st.image(image='./LOGO-eleven-labs.png',
         caption="Model supports multiple languages, including English, German, Polish, Spanish, Italian, French, Portuguese, and Hindi.")

with st.sidebar:
    with st.expander(label="llElevenLabs", expanded=False):
        st.caption(
            "The basic API has a limited number of characters. To increase this limit, you can get a free API key from [llElevenLabs](https://beta.elevenlabs.io/subscription)")
        API_KEY = st.text_input(label="API KEY")

    st.title("Text to Voice")
    english = st.radio(
        label="Choose your language", options=['English', 'Multilingual'], index=0, horizontal=True)

    value = "I am the machine." if english == 'English' else "बस बातें अपने जैसे करते है"
    text = st.text_area(label="Enter the text here",
                        value=value, max_chars=30 if not API_KEY else None)
    voice = st.selectbox(
        label="Choose the voice", options=[v.name for v in voices()]
    )
    st.divider()

if st.button("🔈 Generate Speech"):
    try:
        audio = generate(text=text, voice=voice, model='eleven_multilingual_v1',
                         api_key=API_KEY if API_KEY else st.secrets['API_KEY'])
        st.audio(data=audio)
    except UnauthenticatedRateLimitError:
        e = UnauthenticatedRateLimitError("Unauthenticated Rate Limit Error")
        st.exception(e)

    except RateLimitError:
        e = RateLimitError('Rate Limit')
        st.exception(e)
else:
    st.write('Input the text and click Generate')
