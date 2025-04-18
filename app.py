import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Debug: show working directory and files
st.write("📁 Current working directory:", os.getcwd())
st.write("📂 Files in directory:", os.listdir())

# Set up CSV path
csv_path = os.path.join(os.path.dirname(__file__), "vehicles_us.csv")

# Preview CSV content
if not os.path.exists(csv_path):
    st.error(f"❌ File not found at: {csv_path}")
    st.stop()
else:
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            preview = f.read(300)
            st.text_area("📄 CSV preview (first 300 characters)", preview)

        # Use forgiving parser
        df = pd.read_csv(csv_path, engine='python', encoding='utf-8', on_bad_lines='skip')

        if df.empty:
            st.error("⚠️ CSV file loaded but it's empty. Please check the file.")
            st.stop()
        
        st.success(f"✅ Loaded dataset with shape {df.shape}")

    except Exception as e:
        st.error(f"❌ Error loading CSV: {e}")
        st.stop()

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
