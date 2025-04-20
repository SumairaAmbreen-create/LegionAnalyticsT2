import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config
st.set_page_config(page_title="Vehicle Listings Dashboard", layout="wide")

# Load cleaned data
try:
        df = pd.read_csv("vehicles_cleaned.csv")

        # Force clean + flatten structure
        df = df.copy(deep=True)
        df.to_csv("vehicles_cleaned.csv", index=False)

except Exception as e:
    st.error(f"Failed to load cleaned CSV: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter the Data")

# Vehicle type filter
vehicle_types = df['type'].dropna().unique()
selected_type = st.sidebar.selectbox("Select Vehicle Type", ["All"] + sorted(vehicle_types))
if selected_type != "All":
    df = df[df['type'] == selected_type]

# Price slider
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))
df = df[df['price'].between(*price_range)]

# Year slider
min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())
year_range = st.sidebar.slider("Select Model Year Range", min_year, max_year, (min_year, max_year))
df = df[df['model_year'].between(*year_range)]

# App title
st.header("🚘 Vehicle Listings Analysis Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.subheader("📄 Raw Data")
    st.dataframe(df)

# Histogram: Price Distribution
if st.checkbox("Show Price Distribution Histogram", value=True):
    fig = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
    st.plotly_chart(fig)

# Scatter Plot: Age vs Price
if st.checkbox("Show Age vs Price Scatter Plot", value=True):
    fig = px.scatter(df, x="age", y="price", color='condition', title="Vehicle Age vs Price by Condition")
    st.plotly_chart(fig)

# Filtered scatter: Automatic transmission
if st.checkbox("Show only Automatic vehicles"):
    filtered_df = df[df['transmission'] == 'automatic']
    fig_filtered = px.scatter(filtered_df, x="age", y="price", title="Automatic Vehicles: Age vs Price")
    st.plotly_chart(fig_filtered)

# Median Price by Fuel Type
if st.checkbox("Show Median Price by Fuel Type", value=True):
    median_price_fuel = df.groupby('fuel')['price'].median().reset_index()
    fig = px.bar(median_price_fuel, x='fuel', y='price', title="Median Price by Fuel Type")
    st.plotly_chart(fig)

# Median Price by Condition
if st.checkbox("Show Median Price by Condition", value=True):
    median_price_condition = df.groupby('condition')['price'].median().reset_index()
    fig = px.bar(median_price_condition, x='condition', y='price', title="Median Price by Condition")
    st.plotly_chart(fig)

# Median Price by Top 20 Models
if st.checkbox("Show Median Price by Top 20 Models", value=True):
    n = 20
    top_models = df['model'].value_counts().head(n).index
    top_df = df[df['model'].isin(top_models)]
    median_price_by_model = top_df.groupby('model')['price'].median().reset_index()
    fig = px.bar(median_price_by_model, x='model', y='price', title=f"Median Price (Top {n} Models)")
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>Made this app with ❤️ using Streamlit and Plotly</h6>", unsafe_allow_html=True)
