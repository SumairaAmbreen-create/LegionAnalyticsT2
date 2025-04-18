import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Vehicle Listings Dashboard", layout="wide")

# Load and clean data
try:
    df = pd.read_csv("vehicles_us1.csv", sep=",", encoding='utf-8')
    st.dataframe(df.head())

    # Standardize columns
    df.columns = df.columns.str.strip().str.lower()

    # Coerce numeric columns and clean them
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
    df['is_4wd'] = pd.to_numeric(df['is_4wd'], errors='coerce')

    # Drop rows where essential fields are missing
    df = df.dropna(subset=['model_year', 'price'])

    # Convert types safely
    df['model_year'] = df['model_year'].astype(int)
    df['is_4wd'] = df['is_4wd'].fillna(0).astype(int)
    df['odometer'] = df['odometer'].fillna(0).astype(int)
    df['age'] = 2023 - df['model_year']
    df['paint_color'] = df['paint_color'].fillna("unknown")
    df['condition'] = df['condition'].fillna("unknown")
    df['transmission'] = df['transmission'].fillna("unknown")
    df['fuel'] = df['fuel'].fillna("unknown")
    df['type'] = df['type'].fillna("unknown")

except Exception as e:
    st.error(f"Failed to load CSV: {e}")
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

# Avg Price by Fuel Type
if st.checkbox("Show Average Price by Fuel Type", value=True):
    avg_price_fuel = df.groupby('fuel')['price'].mean().reset_index()
    fig = px.bar(avg_price_fuel, x='fuel', y='price', title="Average Price by Fuel Type")
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>Made this app with ❤️ using Streamlit and Plotly</h6>", unsafe_allow_html=True)
