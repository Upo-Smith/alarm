from datetime import datetime
import streamlit as st
import pytz
import time

timezone = pytz.timezone("Asia/Jakarta")

st.title("Alarm (UTC+7)")

alarm_time = st.time_input("Time Alarm")

option = st.selectbox("Audio", ("Reisa", "Miku"))

clock_placeholder = st.empty()

while True:
    current_time = datetime.now(timezone).strftime("%H:%M:%S")

    clock_placeholder.write(f"Current Time (UTC+7): {current_time}")
    
    if current_time == f'{alarm_time}:00':
        st.audio(f"{option.lower()}.mp3", format="audio/mpeg", autoplay=True, loop=True)
        break
    
    time.sleep(1)
