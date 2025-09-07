import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Power BI Report in Streamlit")
left_column, right_column = st.columns(2)

# Embed Power BI iframe
with right_column:
    components.html(
        """
        <iframe width="1000" height="600"
        src="https://app.powerbi.com/view?r=eyJrIjoiYWE2NzkyNzMtMTdmOC00YjI2LWFjMGItYTNmOWE5YzdhZDJjIiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=650,
    )
with left_column:
    components.html(
        """
        <iframe title="Olist Market Place" width="1000" height="600" 
        src="https://app.powerbi.com/view?r=eyJrIjoiODI5ZTI3NTYtNTJmYS00MWE1LWJiYmYtY2E1NjYzYzUyMmI5IiwidCI6IjEyODJlZTRlLTE5YWItNDU0Mi1hN2IyLTU2MWIyNjIwNWRlMCJ9"
        frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=650, width=1000
    )
