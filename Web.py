import streamlit as st
import pandas as pd

# ------------------------
# Page Selector
# ------------------------
st.sidebar.title("Pages")
page = st.sidebar.selectbox("Choose Page", ["Dashboard", "SQL Queries"])

# ------------------------
# DASHBOARD PAGE
# ------------------------
if page == "Dashboard":
    st.title("🌎 Global Superstore Dashboard")
    
    st.subheader("Overview Charts")
    
    # Display images
    st.image("Sales Distribution by category.png", caption="Sales distribution by category", use_container_width= True)
    st.image("Top 10 products.png", caption="Top 10 Products by Revenue", use_container_width= True)
    st.image("monthly_sals.png", caption="Monthly Sales Trend", use_container_width= True)
    
    st.subheader("Cleaned Dataset Example")
    # Load and show cleaned CSV (first 10 rows)
    df = pd.read_csv("gs_clean.csv")
    st.dataframe(df.sample(10))

# ------------------------
# SQL QUERIES PAGE
# ------------------------
elif page == "SQL Queries":
    st.title("💻 SQL Queries")

    queries = [
        {"title": "Cohort analysis", 
         "csv_file": "Cohort analysis.csv"},
        {"title": "Month over Month growth", 
         "csv_file": "Month Over month growth.csv"},
        {"title": "Profitability analysis per region",
         "csv_file": "Profitability Analysis per Region.csv"},
        {"title": "RFM Analysis",
         "csv_file": "RFM Analysis.csv"},
        {"title": "TOP 5 Products per region",
         "csv_file": "TOP 5 Products per region.csv"},
        {"title": "Top 10 most profitable products",
         "csv_file": ""}
    ]

    # Dropdown to select query
    query_titles = [q["title"] for q in queries]
    selected_query = st.selectbox("Select Query", query_titles)

    # Find the corresponding CSV file
    csv_file = next(q["csv_file"] for q in queries if q["title"] == selected_query)

    st.subheader(selected_query)
    df_result = pd.read_csv(csv_file)
    st.dataframe(df_result)
