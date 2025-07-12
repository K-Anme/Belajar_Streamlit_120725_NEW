import streamlit as st

st.write("Hello, *World!* :sunglasses:")
import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")
Copy
import streamlit as st

video_file = open("myvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
