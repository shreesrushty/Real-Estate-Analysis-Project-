import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE SETTINGS
st.set_page_config(
    page_title="Real Estate Dashboard",
    layout="wide"
)

# LOAD DATA
df = pd.read_csv("cleaned_data.csv")

# TITLE
st.title("🏠 Real Estate Investment Dashboard")

st.markdown("### 📊 Property Market Analysis & EDA")

# SIDEBAR
st.sidebar.header("Filter Properties")

selected_city = st.sidebar.selectbox(
    "Select City",
    df["City"].unique()
)

filtered_df = df[df["City"] == selected_city]

# =========================
# TABLE 1
# =========================

st.subheader("📋 Filtered Property Data")

st.dataframe(filtered_df.head(20))

# =========================
# TABLE 2
# =========================

st.subheader("📈 Statistical Summary")

st.write(filtered_df.describe())

# =========================
# CHART 1
# =========================

st.subheader("1️⃣ Property Price Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(df["Price_in_Lakhs"], kde=True, ax=ax)

st.pyplot(fig)

# =========================
# CHART 2
# =========================

st.subheader("2️⃣ Property Size Distribution")

fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(df["Size_in_SqFt"], kde=True, ax=ax)

st.pyplot(fig)

# =========================
# CHART 3
# =========================

st.subheader("3️⃣ Size vs Price Relationship")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="Size_in_SqFt",
    y="Price_in_Lakhs",
    data=df,
    ax=ax
)

st.pyplot(fig)

# =========================
# CHART 4
# =========================

st.subheader("4️⃣ Average Price by City")

fig, ax = plt.subplots(figsize=(10,5))

df.groupby("City")["Price_in_Lakhs"].mean().sort_values().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# =========================
# CHART 5
# =========================

st.subheader("5️⃣ Correlation Heatmap")

fig, ax = plt.subplots(figsize=(12,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

# =========================
# CHART 6
# =========================

st.subheader("6️⃣ Furnished Status vs Price")

fig, ax = plt.subplots(figsize=(8,5))

sns.boxplot(
    x="Furnished_Status",
    y="Price_in_Lakhs",
    data=df,
    ax=ax
)

st.pyplot(fig)

# =========================
# CHART 7
# =========================

st.subheader("7️⃣ Parking Space vs Property Price")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="Parking_Space",
    y="Price_in_Lakhs",
    data=df,
    ax=ax
)

st.pyplot(fig)

# =========================
# CHART 8
# =========================

st.subheader("8️⃣ Public Transport Accessibility")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="Public_Transport_Accessibility",
    y="Price_per_SqFt",
    data=df,
    ax=ax
)

st.pyplot(fig)

# FOOTER
st.markdown("---")
st.markdown("✅ Built with Streamlit | Real Estate EDA Project")
