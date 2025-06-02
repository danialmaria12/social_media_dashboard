import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="students_social_media_addiction", layout="wide")

st.title("📱 students_social_media_addiction Dashboard")
st.markdown("""
This app explores students’ social media usage, sleep patterns, and addiction scores using visual data analysis.
""")

# Load dataset
st.subheader("📂 Load Dataset")
file_path = "students_social_media_addiction.csv"
try:
    df = pd.read_csv(file_path)
    st.success(f"✅ Loaded file: {file_path}")
except FileNotFoundError:
    st.error(f"❌ File '{file_path}' not found. Make sure it is in the same folder as app.py.")
    st.stop()

# Preview the data
st.subheader("👀 Data Preview")
st.dataframe(df.head())

# Plot 1: Histogram of Daily Usage Hours
st.subheader("📊 Distribution of Daily Social Media Usage")
fig1, ax1 = plt.subplots()
sns.histplot(data=df, x='Avg_Daily_Usage_Hours', bins=10, kde=True, ax=ax1)
ax1.set_title("Average Daily Usage Hours")
ax1.set_xlabel("Hours")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# Plot 2: Addiction Score by Gender
st.subheader("🧠 Addiction Score by Gender")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='Gender', y='Addicted_Score', palette='Set2', ax=ax2)
ax2.set_title("Addiction Score by Gender")
st.pyplot(fig2)

# Plot 3: Sleep Hours vs Addiction
st.subheader("💤 Sleep Hours vs Addiction Score")
fig3, ax3 = plt.subplots()
sns.lineplot(data=df, x='Sleep_Hours_Per_Night', y='Addicted_Score', ax=ax3)
ax3.set_title("Sleep vs Addiction Score")
st.pyplot(fig3)

st.markdown("---")
st.markdown("✨ Created with ❤️ by Maria Danial")
