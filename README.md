# LegionAnalyticsT2

# Vehicle Listings Analysis Dashboard

This project provides an interactive dashboard that allows users to explore vehicle listings data and gain insights into factors that affect vehicle prices. 

## Project Description

The **Vehicle Listings Analysis Dashboard** is a data visualization tool that allows users to explore and analyze vehicle listing data. It helps users understand key trends in vehicle listings, including factors such as price, age, and type of vehicles. The dashboard leverages interactive visualizations to filter and analyze data based on various parameters like price, model year, and vehicle type.

This project uses **Streamlit** for the web application interface and **Plotly** for dynamic and interactive data visualizations. It provides an intuitive and interactive user experience to explore datasets and get insights into vehicle listings.

## Features
- **Data Filtering**: Users can filter the data by vehicle type, price range, and model year using dropdowns and sliders in the sidebar.
- **Visualizations**: The dashboard displays multiple visualizations such as histograms, scatter plots, and bar charts.
- **Checkboxes**: Allows toggling between different visualizations and viewing raw data.
- **Responsive**: The app dynamically updates based on user inputs.

## Libraries and Methods Used
The project utilizes the following libraries:
- **Streamlit**: For building the interactive web application.
- **Plotly**: For creating interactive data visualizations.
- **Pandas**: For data manipulation and analysis.

### The following key methods are used in the project:
- **st.sidebar.selectbox()**: Used for dropdown menus for filtering the data.
- **st.sidebar.slider()**: Used for sliders to filter price and model year ranges.
- **st.checkbox()**: Toggles between different charts and displays raw data.
- **px.scatter()** and **px.histogram()**: Plotly functions used to create scatter plots and histograms for visualizing data.

## How to Run the Project Locally

Follow these steps to launch the project on your local machine:

### Prerequisites:
- Python 3.x
- A virtual environment (optional but recommended)

### Installation Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LegionAnalyticsT2.git
   cd LegionAnalyticsT2

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
3. Activate the virtual environment:
    ```bash
    venv\Scripts\activate (Windows)
    source venv/bin/activate (Mac/Linux)
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
5. Run the Streamlit app:
    ```bash
    streamlit run app.py
6. Open the browser and navigate to http://localhost:8501 to view the dashboard.

## Dependencies

The required libraries are listed in the `requirements.txt` file. You can install them using:

```bash
pip install -r requirements.txt
