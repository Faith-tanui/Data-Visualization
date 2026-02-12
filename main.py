import streamlit as st
import streamlit.components.v1 as components

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Faith Cherono | Data Analyst Portfolio", layout="wide")

# ---------- HEADER ----------
st.title("👋 Hi, I'm Faith Cherono")
st.subheader("Data Analyst | Power BI Specialist | Turning Data into Insightful Stories")
st.write("I transform raw data into strategic insights that drive smarter business decisions.")

# Social links
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[📧 Email Me](mailto:faith.cherono@outlook.com)")
with col2:
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/faithcherono)")  # Replace with your actual LinkedIn
with col3:
    st.markdown("[🐙 GitHub](https://github.com/faithcherono)")  # Replace with your GitHub username

st.markdown("---")

# ---------- ABOUT ME ----------
st.header("💡 About Me")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("/Users/faithcherono/Desktop/Job Applications/Important documents/Faith Cherono - Passport Photo.jpg", width=250, caption="Faith Cherono", use_container_width=False)

with col2:
    st.markdown("""
    I’m **Faith Cherono**, a data analyst passionate about transforming data into meaningful insights and clear business strategy.  
    My work focuses on helping organizations **see beyond the numbers**  identifying patterns, solving problems,  
    and driving smarter decisions through data storytelling.

    I love building **interactive dashboards** and **automated analytics workflows** that reveal what truly drives performance.  
    Using tools like **Power BI**, **SQL**, and **Python**, I bring together the precision of data with the clarity of design  
    turning complex information into visual stories that inspire action.

    When I’m not analyzing data, I’m exploring new ways to make insights more human   
    because great analytics doesn’t just inform decisions, it **shapes how we understand the world**.
    """)

st.info("“Good data tells you what happened. Great analysis tells you what to do next.”")

# Optional styling for rounded image
st.markdown("""
<style>
img {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- SKILLS ----------
st.header("🛠️ Skills")

skills = [
    "Power BI", "SQL", "Python", "Excel",
    "Data Visualization", "ETL", "Data Cleaning",
    "Storytelling with Data", "Business Analytics", "DAX"
]

cols = st.columns(5)
for index, skill in enumerate(skills):
    with cols[index % 5]:
        st.markdown(f"- {skill}")

st.markdown("---")

# ---------- PROJECTS ----------
st.header("📊 Featured Projects")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Olist Market Place Dashboard")
    st.write("An interactive dashboard analyzing e-commerce performance and customer behavior.")
    components.html(
        """
        <iframe title="Olist Market Place" width="100%" height="400" 
        src="https://app.powerbi.com/view?r=eyJrIjoiODI5ZTI3NTYtNTJmYS00MWE1LWJiYmYtY2E1NjYzYzUyMmI5IiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=420,
    )

with col2:
    st.subheader("Business Performance Dashboard")
    st.write("A Power BI report tracking KPIs, sales trends, and business efficiency across departments.")
    components.html(
        """
        <iframe width="100%" height="400"
        src="https://app.powerbi.com/view?r=eyJrIjoiYWE2NzkyNzMtMTdmOC00YjI2LWFjMGItYTNmOWE5YzdhZDJjIiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=420,
    )

with col3:
    st.subheader("Airline Loyalty Program Analysis")
    st.write("A Power BI dashboard showing customer loyalty patterns, retention, and engagement metrics.")
    components.html(
        """
        <iframe title="Airline Loyalty Program" width="100%" height="400"
        src="https://app.powerbi.com/view?r=eyJrIjoiMGI3YTBmNWEtMzE3OC00NmMzLTgzNzYtMTUwOThmNjUyZTVmIiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=420,
    )

st.markdown("---")

# ---------- CONTACT ----------
st.header("📬 Let’s Connect")

st.write("""
If you'd like to collaborate, discuss data projects, or just say hello, feel free to reach out!
""")

st.markdown("[📧 Email Me](mailto:faith.cherono@outlook.com)")

