#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project",project_icon="★") #icons add
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.heder("welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your fullpotential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts- Winston Churchill")

st.header("What's your Challenge Todays?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"💪You're facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challange to get started!")
    
#reflexing
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection here:")
    
if reflection:
    st.success(f"✨Great Insight! your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")


#acheivments
st.header("Celebrate Your Wins!")    
acheivment = st.text_input("Share something you've recently accomplished:")


if acheivment:
    st.success(f"Amazing! You achieved:{acheivment}")
else:
    st.info("Big or small, every acheivment counts! Share one now")
    
    
#footer
st.write("- - -")
st.write("Keep believing in yourself. Growth is a journey, not a destination")
st.write("**⛔ Created by Irtiza Hassan**")
            

