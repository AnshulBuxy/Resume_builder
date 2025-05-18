# main.py
import streamlit as st
from backend import generate_resume, analyze_resume, chat_with_bot, split_response, extract_text_from_resume, markdown_to_latex, read_latex_template
from langchain_core.messages import AIMessage
import pdfplumber
import io
import re

# Set page config
st.set_page_config(layout="wide")
st.title("🧠 AI Resume Builder and Analyzer")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "updated_resume" not in st.session_state:
    st.session_state.updated_resume = ""

if "resume_analyzed" not in st.session_state:
    st.session_state.resume_analyzed = False

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Sidebar Inputs
with st.sidebar:
    st.header("📌 Job Description")
    job_description = st.text_area("Paste the job description here")

    st.markdown("---")
    st.markdown("### 🔄 Upload your resume _or_ fill in the details manually below")
    st.markdown("---")

    st.header("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF resume", type=["pdf"])

    st.markdown("---")
    
    with st.expander("If you dont Have the resume fill the details manually", expanded=True):
        st.header("📌 Personal Information")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        linkedin = st.text_input("LinkedIn URL")
        github = st.text_input("GitHub URL")

        st.header("🎓 Education")
        education = st.text_area("Your education (even if messy)")

        st.header("💼 Experience")
        experience = st.text_area("Describe your experience (raw format)")

        st.header("📁 Projects")
        projects = st.text_area("Mention your projects (raw or messy)")

        st.header("🛠️ Skills")
        skills = st.text_area("List your skills")

    if uploaded_file:
        text = extract_text_from_resume(uploaded_file)
        st.session_state.user_input = text
    else:
        st.session_state.user_input =  f"""
                                        Name: {name}
                                        Email: {email}
                                        Phone: {phone}
                                        LinkedIn: {linkedin}
                                        GitHub: {github}

                                        Education:
                                        {education}

                                        Experience:
                                        {experience}

                                        Projects:
                                        {projects}

                                        Skills:
                                        {skills}
                                        """

    

# Columns
left_col, right_col = st.columns([2, 2], gap="medium")

with left_col:
    resume_to_analyze = st.session_state.updated_resume if st.session_state.updated_resume else st.session_state.user_input
    if uploaded_file or (name and email and phone and linkedin and github and education and experience and projects and skills):
        polished_resume = generate_resume(st.session_state.user_input)
        text, markdown = split_response(polished_resume)
        st.session_state.updated_resume = markdown
            
    if st.button("📊 Analyze Resume"):
        with st.spinner("Analyzing..."):
            response, messages = analyze_resume(resume_to_analyze, job_description)
            content = response["candidates"][0]["content"]["parts"][0]["text"] if isinstance(response, dict) else response.content

            messages.append(AIMessage(content=content))
            st.session_state.chat_history = messages
            st.session_state.resume_analyzed = True

            st.markdown("### 📋 Analysis Report")
            st.markdown(content)

    if st.session_state.resume_analyzed:
        st.markdown("---")
        st.markdown("### 💬 Chat with Resume Bot")
        user_prompt = st.chat_input("Give feedback or ask to update the resume")

        if user_prompt:
            st.chat_message("user").markdown(user_prompt)
            response = chat_with_bot(st.session_state.chat_history, user_prompt)
            content = response["candidates"][0]["content"]["parts"][0]["text"] if isinstance(response, dict) else response.content

            text_content, markdown_resume = split_response(content)
            st.chat_message("assistant").markdown(text_content)
            st.session_state.chat_history.append(AIMessage(content=content))
            if markdown_resume:
                st.session_state.updated_resume = markdown_resume

with right_col:
    st.subheader("📄 Live Resume Preview")
    with st.expander("Chat History", expanded=True):
        if st.session_state.updated_resume:
            st.markdown(st.session_state.updated_resume)
        else:
            st.info("Your polished resume will appear here after generation.")
        
        if st.session_state.updated_resume:
            if st.button("📄 click here to convert this to Latex"):
                latex_template = read_latex_template("main.tex")
                latex_content = markdown_to_latex(st.session_state.updated_resume, latex_template)
                st.download_button("📄 Download LaTeX Resume", latex_content, file_name="resume.tex")
            st.download_button("📄 Download Updated Resume", st.session_state.updated_resume, file_name="updated_resume.md")
