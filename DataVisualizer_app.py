import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
# ------------------ CUSTOM CSS + DARK MODE ------------------ #
st.markdown("""
    <style>
    .title-style {
        font-size: 40px;
        color: #00FFAA;
        text-align: center;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .stButton > button {
        background-color: #00AA88;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #00ccaa;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------ #
st.markdown('<div class="title-style">📊 Data Visualizer App (Line Chart)</div>', unsafe_allow_html=True)

# ------------------ FILE UPLOAD ------------------ #
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Load data
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File loaded successfully!")
        st.dataframe(df.head(), use_container_width=True)

        # ------------------ DETECT NUMERIC COLUMNS ------------------ #
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

        # ------------------ FILTER ------------------ #
        st.subheader("🔍 Optional: Filter numeric column")
        filter_col = st.selectbox("Filter column (optional)", ["None"] + numeric_cols)
        filtered_df = df.copy()
        if filter_col != "None":
            min_val = float(df[filter_col].min())
            max_val = float(df[filter_col].max())
            filter_range = st.slider(f"Filter range for {filter_col}", min_value=min_val, max_value=max_val,
                                     value=(min_val, max_val))
            filtered_df = df[(df[filter_col] >= filter_range[0]) & (df[filter_col] <= filter_range[1])]
            st.info(f"Filtered data has {len(filtered_df)} rows.")
            st.dataframe(filtered_df, use_container_width=True)

        # ------------------ CHOOSE X/Y COLUMNS ------------------ #
        st.subheader("📈 Select columns for Line Plot")
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("X-axis", filtered_df.columns)
        with col2:
            y_col = st.selectbox("Y-axis", filtered_df.columns)

        # ------------------ PLOT ------------------ #
        if st.button("Generate Line Plot"):
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(filtered_df[x_col], filtered_df[y_col], marker='o', color='#00FFAA')
            ax.set_title(f"{x_col} vs {y_col} (Line Plot)")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.grid(True)
            st.pyplot(fig)

        # ------------------ DOWNLOAD FILTERED DATA ------------------ #
        st.subheader("⬇️ Download Filtered Data")
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
