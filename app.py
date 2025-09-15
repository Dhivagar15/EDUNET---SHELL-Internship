import streamlit as st
import pandas as pd
import plotly.express as px

# --- STREAMLIT PAGE CONFIGURATION ---
st.set_page_config(page_title="Climate Risk Dashboard", layout="wide")
st.title("🌎 Climate Risk and Disaster Management Dashboard")
st.markdown("An interactive dashboard to explore the World Risk Index (WRI) dataset.")

# --- DATA LOADING FUNCTION ---
@st.cache_data
def load_data(file_path):
    """Loads and cleans the dataset safely."""
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()  # Clean column names
        return df
    except FileNotFoundError:
        return None

# --- FILE UPLOAD & DATA LOADING ---
uploaded_file = st.sidebar.file_uploader("📂 Upload World Risk Index CSV", type=["csv"])
if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data('world_risk_index.csv')

if df is None:
    st.error("⚠️ The dataset was not found. Please upload a valid 'world_risk_index.csv' file.")
    st.stop()

# --- SAFETY CHECKS ---
required_columns = {"Year", "Region", "WRI"}
if not required_columns.issubset(df.columns):
    st.error(f"⚠️ The dataset must contain at least these columns: {', '.join(required_columns)}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔎 Filter Data")
years = sorted(df['Year'].unique())
selected_year = st.sidebar.selectbox("Select a Year", years, index=len(years) - 1)

df_filtered = df[df['Year'] == selected_year]

# --- MAIN DASHBOARD ---
st.header(f"📊 Data Overview for {selected_year}")
st.dataframe(df_filtered.head())  # Display top 5 rows

# --- 1. WORLD MAP (CHOROPLETH) ---
st.subheader("🌍 World Risk Index (WRI) by Country")
fig_map = px.choropleth(
    df_filtered,
    locations="Region",
    locationmode="country names",
    color="WRI",
    hover_name="Region",
    color_continuous_scale=px.colors.sequential.YlOrRd,
    title=f"WRI Scores in {selected_year}",
    labels={'WRI': 'World Risk Index'}
)
st.plotly_chart(fig_map, use_container_width=True)

# --- 2. HISTOGRAM OF WRI ---
st.subheader("📊 Distribution of WRI Scores")
fig_hist = px.histogram(
    df_filtered,
    x="WRI",
    nbins=20,
    title="Distribution of WRI Scores",
    labels={'WRI': 'World Risk Index'}
)
st.plotly_chart(fig_hist, use_container_width=True)

# --- 3. INTERACTIVE SCATTER PLOT ---
st.subheader("📈 Correlation between Features")
st.write("Select two features to explore their relationship:")

numerical_columns = df_filtered.select_dtypes(include=['float64', 'int64']).columns.tolist()
if len(numerical_columns) >= 2:
    col1, col2 = st.columns(2)
    with col1:
        x_axis_col = st.selectbox("X-Axis", numerical_columns, index=0)
    with col2:
        y_axis_col = st.selectbox("Y-Axis", numerical_columns, index=1)

    fig_scatter = px.scatter(
        df_filtered,
        x=x_axis_col,
        y=y_axis_col,
        hover_name="Region",
        title=f"Scatter Plot: {x_axis_col} vs {y_axis_col}"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.warning("⚠️ Not enough numerical columns to plot a scatter plot.")
