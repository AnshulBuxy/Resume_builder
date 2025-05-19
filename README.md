# Resume Builder with Smart Chatbot Assistance

This project was developed as an internship assignment for **Sama**. It’s a next-generation resume builder powered by AI that helps users create, analyze, and improve their resumes simply by chatting with an intelligent chatbot. Whether you're starting from scratch or already have a resume, this tool adapts to your needs — providing resume scoring, keyword analysis, and actionable suggestions based on the job description you provide.

> _Note: The current project is primarily focused on showcasing LLM integration and chatbot intelligence rather than frontend design. A more polished UI will be built if required._

---

## 📽️ Video Preview 

- 🎬 **Demo Video**: [Watch here](https://drive.google.com/drive/folders/13jaAZiafVsJBUDcr9OL-rvC6xJi5_pIb?usp=sharing)

---

## 🛠️ Technologies Used

- **Google Gemini Flash Lite** – Used as the core large language model for fast, intelligent conversations.
- **LangChain** – Provides a robust framework to manage modular agents, enabling resume analysis, transformation, and dialogue management.
- **Streamlit** – Handles the web interface and real-time resume previews.
- **Python** – Powers the backend logic and integrates all components.
- **LaTeX / Markdown** – Enables high-quality and customizable resume formats for download.

---

## 🌐 Website Structure & Preview

The website is organized into two main sections:

### 🔹 Sidebar
- Upload your current resume (PDF or text)
- Paste or type the job description you're targeting
- If you don’t have a resume, scroll down to input personal/professional details — the bot will generate one for you

### 🔹 Main Panel
- **Live Resume Preview (Right Side)**:
  - See updates in real-time as the resume is modified
  - Resume is rendered from LaTeX or Markdown
  - Download buttons available to export in `.tex` or `.md` formats
- **Resume Analysis & Chatbot Interface (Left Side)**:
  - Click the **Analyze** button to receive a complete evaluation based on your resume and job description
  - View resume score, missing keywords, and detailed suggestions
  - Chat with the bot to apply suggestions or make changes
  - Example: *"Improve the experience section based on the analysis."* — and the bot will modify it accordingly.

### 💻 Website Visual Preview

| Sidebar Interface | Resume Analysis & Chat | Live Preview & Download |
|-------------------|------------------------|--------------------------|
| ![Sidebar](https://github.com/AnshulBuxy/Resume_builder/blob/main/assets/WhatsApp%20Image%202025-05-19%20at%2009.25.51_55ed31a6.jpg) | ![Chatbot](https://github.com/AnshulBuxy/Resume_builder/blob/main/assets/WhatsApp%20Image%202025-05-19%20at%2009.26.29_b7e768e3.jpg) | ![Preview](https://github.com/AnshulBuxy/Resume_builder/blob/main/assets/WhatsApp%20Image%202025-05-19%20at%2009.26.56_0a59ab48.jpg)|

---

## 🧠 Utility of the Website

- **Job-specific Resume Analysis**: Understand how well your resume aligns with the job.
- **AI Recommendations**: Receive targeted feedback and ask the bot to update your resume in real time.
- **From Scratch Creation**: Don’t have a resume? Input your details and the AI will build one for you.
- **Multi-format Output**: Download resumes in LaTeX or Markdown.
- **Instant Preview**: See changes live before downloading.

---

## 🚀 Advantages of the Tech Stack

- **LLM (Gemini Flash Lite)**: Delivers high-speed, context-aware, and conversational intelligence.
- **LangChain**: Makes it easy to build and manage different agents (chat, analysis, resume generation).
- **Streamlit**: Enables rapid deployment and real-time interactivity with minimal boilerplate.
- **LaTeX & Markdown Support**: Ensures professional formatting and future extensibility to other formats.

---

## 🔮 Future Improvements

1. **Enhanced UI/UX**:
   - Rebuilding the frontend using HTML, CSS, and JavaScript for better styling and flexibility.
2. **LaTeX Previewer Integration**:
   - Currently, LaTeX resumes must be downloaded for preview; we plan to support direct rendering.
3. **Multiple LaTeX Templates**:
   - Users will be able to choose from various pre-built professional templates.
4. **User Accounts & Save Sessions**:
   - Allow users to save and edit their resume drafts over time.
5. **In-depth Section Suggestions**:
   - Extend chatbot capabilities to suggest section-level improvements (e.g., work experience, summary).

---

## 📦 How to Clone & Run the Project Locally
### create a .env file and Inside your .env file, add the following:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
---
```bash
# Step 1: Clone the repository
git clone https://github.com/AnshulBuxy/Resume_builder
cd Resume_builder

# Step 2: Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt


# Step 4: Run the Streamlit app
streamlit run frontend.py
