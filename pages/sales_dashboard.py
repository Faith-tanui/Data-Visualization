import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("📊 Retail Sales Performance Analysis")

st.write("""
This dashboard explores retail transaction data to understand revenue performance,
profitability drivers, and product relationships.
""")
st.markdown("## Project Overview")

st.write("""
This project analyzes retail transaction data to understand **sales performance, profitability drivers, and customer purchasing behavior**. 

The dataset contains nearly **10,000 retail transactions** including order dates, product categories, discounts, profit margins, and customer information.

The goal of this analysis is to answer key business questions:

- How has revenue evolved over time?
- Which regions generate the highest revenue and profit?
- How do discounts impact profitability?
- Which product categories drive business performance?
- Are there products frequently purchased together that suggest cross-selling opportunities?

The analysis combines **exploratory data analysis, business performance metrics, and product relationship analysis** to uncover actionable insights for retail strategy.
""")

# Load data
df = pd.read_csv("Projects/sales_performance_analysis/Superstore_cleaned.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# ---------- KPI SECTION ----------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
orders = df["Order ID"].nunique()
profit_margin = total_profit / total_sales

customers = df.groupby("Customer ID")["Order ID"].nunique()
returning_rate = (customers > 1).sum() / customers.count()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Revenue", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Orders", orders)
col4.metric("Profit Margin", f"{profit_margin:.2%}")
col5.metric("Returning Customers", f"{returning_rate:.1%}")

st.markdown("---")

# ---------- REVENUE TREND ----------
st.subheader("Revenue Trend")

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig, ax = plt.subplots()

ax.plot(monthly_sales["Order Date"], monthly_sales["Sales"])

plt.xticks(rotation=90)

st.pyplot(fig)

st.markdown("### Observation")

st.write("""
Revenue trends show noticeable fluctuations over time, suggesting periods of higher purchasing activity likely driven by seasonal demand or promotional campaigns. 
While overall revenue demonstrates steady business activity, there are spikes in certain months indicating potential opportunities to align marketing and inventory strategies with peak demand periods.
""")

# ---------- REGION ANALYSIS ----------
st.subheader("Regional Sales Performance")

region_sales = df.groupby("Region")[["Sales","Profit"]].sum()

fig, ax = plt.subplots()

region_sales["Sales"].plot(kind="bar", ax=ax)

st.pyplot(fig)

st.markdown("### Observation")

st.write("""
Regional performance analysis shows clear differences in revenue contribution across geographic markets. 
Some regions consistently outperform others, indicating stronger market demand or customer concentration.

However, revenue alone does not fully represent performance — profitability and operational efficiency should also be considered when evaluating regional strategy.
""")

# ---------- DISCOUNT IMPACT ----------
st.subheader("Discount Impact on Profit")

fig, ax = plt.subplots()

sns.scatterplot(data=df, x="Discount", y="Profit", ax=ax)

st.pyplot(fig)

st.markdown("### Observation")

st.write("""
The relationship between discount levels and profit reveals a clear pattern: higher discounts often correspond with lower profit margins and, in some cases, negative profitability.

While discounting may help increase sales volume, excessive discounting appears to erode profit, suggesting the need for a more balanced pricing strategy that maintains competitiveness without sacrificing margins.
""")

# ---------- PRODUCT PORTFOLIO ----------
st.subheader("Product Portfolio Analysis")

product_perf = df.groupby("Sub-Category")[["Sales","Profit"]].sum().reset_index()

fig, ax = plt.subplots()

sns.scatterplot(data=product_perf, x="Sales", y="Profit", ax=ax)

for i,row in product_perf.iterrows():
    ax.text(row["Sales"], row["Profit"], row["Sub-Category"])

st.pyplot(fig)

st.markdown("### Observation")

st.write("""
The product portfolio analysis highlights how different product categories contribute to revenue and profit. 

Some products generate strong revenue and profit simultaneously, making them key drivers of business performance. 
Others generate high sales volume but contribute little or negative profit, suggesting pricing or cost structure issues that may require further review.
""")

st.markdown("---")

st.markdown("## Key Findings")

st.write("""
**1. Revenue shows periodic spikes.**
Retail performance demonstrates seasonal fluctuations, suggesting opportunities to better align promotions and inventory with high-demand periods.

**2. Regional markets contribute unevenly to revenue.**
Some regions dominate sales performance, indicating strong geographic demand but also highlighting potential opportunities to expand in underperforming regions.

**3. Heavy discounting reduces profitability.**
Higher discount levels frequently correspond with negative profit margins, indicating that aggressive pricing strategies may be undermining overall profitability.

**4. Product portfolio performance varies significantly.**
Certain product categories deliver both high revenue and strong profit margins, while others generate high sales volume but contribute little to profit.

**5. Opportunities exist for pricing and product strategy improvements.**
By optimizing discount strategies and focusing on high-performing product categories, the business could improve overall profitability while maintaining sales growth.
""")

st.markdown("## Business Recommendations")

st.write("""
• Review discount policies to ensure profitability is not sacrificed for short-term sales volume.  
• Focus marketing and inventory strategies around peak demand periods identified in the revenue trends.  
• Invest in high-performing product categories that drive both revenue and profit.  
• Investigate underperforming product segments to determine whether pricing, supply costs, or demand issues are responsible.
""")