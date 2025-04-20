# LegionAnalyticsT2

## Vehicle Listings Analysis Dashboard

This project presents a powerful and interactive dashboard designed to analyze vehicle listings data. By visualizing trends and patterns, users can explore how various attributes such as vehicle age, condition, fuel type, and model year—impact listing prices. The dashboard is built using **Streamlit** and **Plotly** to provide a responsive and intuitive interface.

---

## Introduction

Buying or selling a vehicle often requires understanding pricing trends and market factors. This project was created to provide users with insights into how different vehicle characteristics affect their market value. By analyzing real-world vehicle listings, the goal is to support informed decision-making for buyers, sellers, and researchers interested in automotive pricing dynamics.

---

## Project Description

The **Vehicle Listings Analysis Dashboard** is a data visualization tool that allows users to explore and analyze vehicle listing data. It helps users understand key trends in vehicle listings, including factors such as price, age, and type of vehicles. The dashboard leverages interactive visualizations to filter and analyze data based on various parameters like price, model year, and vehicle type.

This project uses **Streamlit** for the web application interface and **Plotly** for dynamic and interactive data visualizations. It provides an intuitive and interactive user experience to explore datasets and get insights into vehicle listings.

## Intermediate Insights (From the Dashboard)

Through the dashboard, users can gain key insights such as:

- **Newer vehicles tend to be listed at higher prices**, but the condition of the vehicle plays a crucial role in retaining value.
- **Fuel type** can significantly affect median price, with electric or hybrid vehicles often commanding a premium.
- **Automatic transmissions** are more prevalent in higher-priced listings compared to manual ones.
- **Vehicle age** shows a negative correlation with price, as expected, but outliers exist (e.g., vintage models in good condition).

---

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
6. The required libraries are listed in the `requirements.txt` file. You can install them using:
    ```bash
    pip install -r requirements.txt
7. Open the browser and navigate to http://localhost:8501 to view the dashboard.


## Conclusion
This project showcases how interactive visualizations can bring vehicle data to life. Users can explore real-world vehicle listings, uncover pricing insights, and understand trends based on vehicle characteristics. It combines data analysis with visual storytelling making it a valuable tool for anyone navigating the used vehicle market or building experience in data-driven app development.

## Acknowledgements
Made with ❤️ using Streamlit, Plotly, and Pandas.