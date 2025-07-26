import streamlit as st
import streamlit.components.v1 as components

st.title("Power BI Report in Streamlit")
st.text()

# Embed Power BI iframe
components.html(
    """
    <iframe width="1000" height="600"
    src="https://app.powerbi.com/view?r=eyJrIjoiYWE2NzkyNzMtMTdmOC00YjI2LWFjMGItYTNmOWE5YzdhZDJjIiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
    frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=650,
)

components.html(
    """
    <iframe title="SUPERSTORE SALES" width="600" height="373.5" 
    src="https://app.powerbi.com/view?r=eyJrIjoiYWE2NzkyNzMtMTdmOC00YjI2LWFjMGItYTNmOWE5YzdhZDJjIiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9" 
    frameborder="0" allowFullScreen="true"></iframe>
    """
)