from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jishnu"
PAGE_ICON = ":wave:"
NAME = "Jishnu V A"
DESCRIPTION = """
Senior Business Analyst
"""
EMAIL = "jishnuashok1994@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jishnu-v-a-836ba9138/",
    "GitHub": "https://github.com/jishnuva10",
    "Twitter": "https://twitter.com/Jishnuva10",
}
PROJECTS = {
    "🏆 Reports Dashboard ": "https://jishnuva10-indus-ansar-sir-data-availability-report-sr1523.streamlit.app/"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualification")
st.write(
    """
- ✔️ 4 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Excellent Documentation skill
- ✔️ Excellent client management
Education : 
- ✔️ BE Mechanical Engineering 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Tools: Advanced Excel, Python, SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Business Analyst | Antilia Solutions**")
st.write("12/2022 - Present")
st.write(
    """
- ► Investigating and understanding the needs of multiple
    business stakeholders and existing processes and
    capturing this in documented format

- ► Generating detailed functional requirements and
    specifications and ensuring that these guide correct
    development of key business systems.
- ► Work closely with the Project Support Manager and Head
    of Development to manage projects using agile
    methodologies appropriate ways of capturing business processes
- ► Generate business cases for proposed business changes.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior Business Analyst | WyzMindz Solutions Pvt. Ltd**")
st.write("08/2021 - 12/2022")
st.write(
    """
- ► Requirements gathering, Process mapping, Documenting
    functional and technical specifications and Modeling
    workflows
- ► Functional person in various stages of Software
    Development Lifecycle involving requirements
    elicitation, authoring user stories, reviewing test cases, conducting business and user acceptance testing (UAT)
- ►Closely working with business teams to understand
    business issues and data challenges. Building and
    maintaining relationships with stakeholders and 3rd
    parties
- ►Data Presentation using visualization tools and
    preparation of business reports for top management. 
- ►RPA - Daily,Weekly & Monthly reports.
- ►RPA - Daily,Weekly & Monthly reports.


"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Procurement Analyst | Regency Group of Corporate Management**")
st.write("09/2018 - 10/2020")
st.write(
    """
- ► Client Management, Negotiation
- ► Yearly BDA Negotiation
- ► Data Presentation using visualization tools and
    preparation of business reports for top management
- ►Data Scraping & Price benchmarking
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
