# backend.py
import os
import re
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import pdfplumber
import io
import re

# Load environment variables
load_dotenv()

# Initialize Gemini model
chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

def extract_text_from_resume(file):
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    else:
        return ""


def split_response(response: str):
    match = re.search(r"```markdown(.*?)```", response, re.DOTALL)
    if match:
        markdown_content = match.group(1).strip()
        non_markdown_content = re.sub(r"```markdown(.*?)```", "", response, flags=re.DOTALL).strip()
    else:
        markdown_content = ""
        non_markdown_content = response.strip()
    return non_markdown_content, markdown_content

def generate_resume(user_input: str):
    polish_prompt = f"""
    You are a professional resume writer. Using the following raw information, generate a polished and professional resume in markdown format.

    Details:
    {user_input}
    """
    response = chat.invoke([HumanMessage(content=polish_prompt)])
    if isinstance(response, dict):
        return response["candidates"][0]["content"]["parts"][0]["text"]
    return response.content

def analyze_resume(resume: str, job_description: str):
    analyze_prompt = f"""
    You are a professional resume analyst and recruiter. Based on the following job description and resume, provide a short analysis.

    Give:
    - Resume Score out of 10
    - Missing Keywords (if any)
    - Missing Sections (if any)
    - Suggestions for Improvement

    Resume:
    {resume}

    Job Description:
    {job_description}

    Respond concisely. Do not generate a full resume yet.
    """
    system_message = SystemMessage(content='''You are a helpful AI resume advisor. After analyzing the resume and job description, you will discuss suggestions and update the resume based on user feedback.

    Important:
    - Whenever you provide a resume update, always return the full updated resume.
    - Enclose the full updated resume inside a markdown code block like this:

    ```markdown
    <full updated resume here>''')
    messages = [system_message, HumanMessage(content=analyze_prompt)]
    response = chat.invoke(messages)
    return response, messages

def chat_with_bot(history, prompt):
    history.append(HumanMessage(content=prompt))
    response = chat.invoke(history)
    return response
