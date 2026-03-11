import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="A/B Testing Experiment",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("Projects/E-Commerce AB Testing Analysis/ab_testing_cleaned.csv")

control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

control_rate = control["converted"].mean()
treatment_rate = treatment["converted"].mean()

lift = (treatment_rate - control_rate) / control_rate

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🧪 E-commerce A/B Testing Experiment")

st.markdown("""
### Evaluating the Impact of a New Landing Page on Conversion Performance
""")

st.markdown("""
# Project Introduction
Online businesses frequently experiment with website design changes to improve user engagement and increase conversions. A common method to evaluate the results of such changes is A/B testing. In this method, users are split into
two groups and each group is exposed to different versions of a webpage. User behaviour is then compared across the two groups to determine whether a new design leads to a significant improvement in performance.

Users visiting the website were randomly assigned to one of the two groups:
- Control group: They were exposed to the original landing page.
- Treatment group: They were exposed to the new landing page.
This experiment evaluates whether a redesigned landing page improves conversion rates compared to the original page.

**Dataset Source:**https://www.kaggle.com/datasets/putdejudomthai/ecommerce-ab-testing-2022-dataset1
""")

st.markdown("---")

# ---------------------------------------------------
# KPI METRICS
# ---------------------------------------------------

st.subheader("Experiment Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Users", f"{len(df):,}")
col2.metric("Total Conversions", f"{df['converted'].sum():,}")
col3.metric("Control Conversion Rate", f"{control_rate:.2%}")
col4.metric("Treatment Conversion Rate", f"{treatment_rate:.2%}")

st.metric("Conversion Lift", f"{lift:.2%}")

st.markdown("---")

# ---------------------------------------------------
# EDA SECTION
# ---------------------------------------------------

st.header("Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Traffic Distribution")

    fig, ax = plt.subplots()
    sns.countplot(x="group", data=df, ax=ax)
    st.pyplot(fig)

with col2:

    st.subheader("Conversion Distribution")

    fig, ax = plt.subplots()
    sns.countplot(x="converted", data=df, ax=ax)
    st.pyplot(fig)

st.markdown("---")

# ---------------------------------------------------
# CONVERSION RATE ANALYSIS
# ---------------------------------------------------

st.header("Conversion Rate Analysis")

fig, ax = plt.subplots()

sns.pointplot(x="group", y="converted", data=df, ax=ax)

ax.set_ylabel("Conversion Rate")

st.pyplot(fig)

st.markdown("""
The conversion rate comparison shows only a small difference between the control and treatment groups.
However, visual inspection alone cannot determine whether this difference is statistically meaningful.
""")

st.markdown("---")

# ---------------------------------------------------
# SEGMENT ANALYSIS
# ---------------------------------------------------

st.header("Conversion Rate by Country")

fig, ax = plt.subplots()

sns.barplot(x="country", y="converted", data=df, ax=ax)

st.pyplot(fig)

st.markdown("""
Segment analysis shows that conversion behavior remains relatively consistent across geographic regions.
No strong regional differences were observed in experiment performance.
""")

st.markdown("---")

# ---------------------------------------------------
# HYPOTHESIS TEST
# ---------------------------------------------------

st.header("Statistical Hypothesis Test")

st.markdown("""
A two-proportion Z-test was performed to determine whether the difference in conversion rates between the control and treatment groups is statistically significant.

Test Results:

• **Z-score:** 1.196  
• **P-value:** 0.232
""")

st.markdown("""
Since the p-value is greater than the standard significance level of **0.05**, we fail to reject the null hypothesis.

This indicates that the difference in conversion rates between the two landing pages is **not statistically significant**.
""")

st.markdown("---")

# ---------------------------------------------------
# KEY FINDINGS
# ---------------------------------------------------

st.header("Key Findings")

st.markdown("""
**Key insights from the experiment:**

• The treatment page shows only a small difference in conversion rate compared to the control page.

• Statistical testing indicates that this difference is **not statistically significant**.

• The confidence interval for the difference includes zero, suggesting the observed variation may be due to random chance.

• Conversion behavior appears consistent across geographic regions.

**Conclusion:**  
The redesigned landing page does not provide sufficient evidence of improved conversion performance.
""")

st.markdown("---")

# ---------------------------------------------------
# BUSINESS RECOMMENDATION
# ---------------------------------------------------

st.header("Business Recommendation")

st.markdown("""
Based on the experiment results, there is insufficient statistical evidence to recommend replacing the existing landing page with the redesigned version.

Future experiments could explore alternative design improvements such as:

• simplifying the purchase flow  
• improving product messaging  
• testing alternative layouts or CTAs  
• personalized landing pages for different user segments

Further experimentation may help identify changes that meaningfully increase conversion performance.
""")