import streamlit as st
import pandas as pd
import os

# Debug info
st.write("📁 Current directory:", os.getcwd())
st.write("📂 Directory contents:", os.listdir())

# Path to CSV
csv_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

# Check file existence
if not os.path.exists(csv_path):
    st.error(f"❌ File not found: {csv_path}")
    st.stop()

# Show raw preview of file before parsing
try:
    with open(csv_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    st.text_area("🧾 First 20 lines of CSV", "".join(lines[:20]), height=300)
except Exception as e:
    st.error(f"❌ Error reading file: {e}")
    st.stop()

# Try parsing with pandas
try:
    df = pd.read_csv(csv_path, engine='python', encoding='utf-8', on_bad_lines='skip')
    st.success(f"✅ CSV loaded successfully with shape {df.shape}")
except Exception as e:
    st.error(f"❌ pandas.read_csv() failed: {e}")
    st.stop()

# Show column names
st.subheader("🧠 Column Names")
st.write(df.columns.tolist())


# Preprocessing
df.columns = df.columns.str.strip().str.lower()
df = df.dropna(subset=['model_year'])
df['age'] = 2023 - df['model_year']

# Sidebar filters
st.sidebar.header("🔍 Filter the Data")

# Vehicle type
vehicle_types = df['type'].dropna().unique()
selected_type = st.sidebar.selectbox("Select Vehicle Type", ["All"] + list(vehicle_types))
if selected_type != "All":
    df = df[df['type'] == selected_type]

# Price range
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))
df = df[df['price'].between(*price_range)]

# Year range
min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())
year_range = st.sidebar.slider("Select Model Year Range", min_year, max_year, (min_year, max_year))
df = df[df['model_year'].between(*year_range)]

# App title
st.header("🚘 Vehicle Listings Analysis Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.subheader("🔢 Raw Data")
    st.dataframe(df)

# Price distribution histogram
if st.checkbox("Show Price Distribution Histogram", value=True):
    fig = px.histogram(df, x="price", nbins=50, title="Distribution of Vehicle Prices")
    st.plotly_chart(fig)

# Age vs Price scatter
if st.checkbox("Show Age vs Price Scatter Plot", value=True):
    fig = px.scatter(df, x="age", y="price", color='condition', title="Vehicle Age vs Price by Condition")
    st.plotly_chart(fig)

# Filtered automatic only
if st.checkbox("Show only Automatic vehicles"):
    filtered_df = df[df['transmission'] == 'automatic']
    fig_filtered = px.scatter(filtered_df, x="age", y="price", title="Automatic Vehicles: Age vs Price")
    st.plotly_chart(fig_filtered)

# Avg price by fuel type
if st.checkbox("Show Average Price by Fuel Type", value=True):
    avg_price_fuel = df.groupby('fuel')['price'].mean().reset_index()
    fig = px.bar(avg_price_fuel, x='fuel', y='price', title="Average Price by Fuel Type")
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>Made this app with ❤️ using Streamlit and Plotly</h6>", unsafe_allow_html=True)
