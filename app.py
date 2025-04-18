import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load and inspect file
st.write("📁 Current directory:", os.getcwd())
st.write("📂 Files:", os.listdir())

csv_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

if not os.path.exists(csv_path):
    st.error(f"❌ File not found at path: {csv_path}")
    st.stop()

# Show preview of raw CSV content
try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        content = f.read(500)
        st.text_area("🧾 CSV Preview (first 500 chars)", content)
except Exception as e:
    st.error(f"❌ Failed reading file: {e}")
    st.stop()

# Read CSV with pandas, skipping bad lines
try:
    df = pd.read_csv(csv_path, encoding='utf-8', on_bad_lines='skip')
    st.success(f"✅ Loaded CSV with shape: {df.shape}")
except Exception as e:
    st.error(f"❌ Failed to load CSV: {e}")
    st.stop()

# Clean and transform
df.columns = df.columns.str.strip().str.lower()
df = df.dropna(subset=['model_year'])
df['age'] = 2023 - df['model_year']

# Sidebar filters
st.sidebar.header("Filter the Data")

# Vehicle type filter
vehicle_types = df['type'].dropna().unique()
selected_type = st.sidebar.selectbox("Select Vehicle Type", ["All"] + list(vehicle_types))
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
    st.subheader("Raw Data")
    st.dataframe(df)

# Price Distribution
if st.checkbox("Show Price Distribution Histogram", value=True):
    fig = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
    st.plotly_chart(fig)

# Age vs Price
if st.checkbox("Show Age vs Price Scatter Plot", value=True):
    fig = px.scatter(df, x="age", y="price", color='condition', title="Vehicle Age vs Price by Condition")
    st.plotly_chart(fig)

# Only Automatic vehicles
if st.checkbox("Show only Automatic vehicles"):
    filtered_df = df[df['transmission'] == 'automatic']
    fig_filtered = px.scatter(filtered_df, x="age", y="price", title="Automatic Vehicles: Age vs Price")
    st.plotly_chart(fig_filtered)

# Average price by fuel
if st.checkbox("Show Average Price by Fuel Type", value=True):
    avg_price_fuel = df.groupby('fuel')['price'].mean().reset_index()
    fig = px.bar(avg_price_fuel, x='fuel', y='price', title="Average Price by Fuel Type")
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>Made with ❤️ using Streamlit + Plotly</h6>", unsafe_allow_html=True)
