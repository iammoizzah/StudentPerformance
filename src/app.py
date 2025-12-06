# app.py 
"""cd ~/Documents/GitHub/StudentPerformance/src
streamlit run app.py"""
import streamlit as st
import pandas as pd
import os

# -------------------------------------------------
st.set_page_config(page_title="CS-4048 Project I", layout="wide")

st.title("CS-4048 - Data Science (Fall 2025)")
st.header("Project I - Student Performance Prediction")


st.markdown("---")

# Research Questions
st.subheader("Research Questions")
st.write("• RQ1: How accurately can we predict **Midterm I** marks?")  
st.write("• RQ2: How accurately can we predict **Midterm II** marks?")  
st.write("• RQ3: How accurately can we predict **Final Exam** marks?")
st.markdown("---")

# Load and display results
st.subheader("Model Performance Comparison")

if not os.path.exists("comparison_table.csv"):
    st.error("comparison_table.csv not found! Place it in the same folder as app.py")
    st.stop()

df = pd.read_csv("comparison_table.csv")

# Highlight best model (highest R²) for each RQ
def highlight_row(row):
    best_r2 = df[df["RQ"] == row["RQ"]]["R2"].max()
    if row["R2"] == best_r2 and "Dummy" not in row["Model"]:
        return ["background-color: #d4edda; font-weight: bold"] * len(row)
    elif "Dummy" in row["Model"]:
        return ["background-color: #f8d7da"] * len(row)
    else:
        return [""] * len(row)

styled_df = df.style.apply(highlight_row, axis=1).format({
    "MAE": "{:.3f}", "RMSE": "{:.3f}", "R2": "{:.4f}"
})
st.dataframe(styled_df, use_container_width=True)

# Key Findings
st.subheader("Key Findings")
st.success("RQ1 (Midterm I) → Very poor prediction (negative R²) – early assessments alone are not useful.")
st.warning("RQ2 (Midterm II) → Moderate accuracy (R² ≈ 0.60) – Midterm I is a strong predictor.")
st.success("RQ3 (Final Exam) → Excellent prediction (R² = 0.721, MAE = 3.82) – best model beats Dummy by 53%!")

st.info("**Conclusion:** Student performance becomes highly predictable after Midterm I. Early intervention after Midterm I can help at-risk students significantly.")

st.subheader("Project Workflow Diagram (All Deliverables Included)")

#Workflow (simple text version – always works)
st.subheader("Project Workflow")
st.code("""
Raw Excel Sheets (6 files)
    ↓
Cleaning & Preprocessing
    ↓
final_dataset.csv (combined)
    ↓
EDA + Visualization
    ↓
Feature Selection (No Data Leakage!)
    ↓
RQ1 → RQ2 → RQ3 Modeling
    ↓
Simple + Multiple Linear + Polynomial + Dummy
    ↓
Bootstrapping (500 samples)
    ↓
This Interactive Dashboard
""", language="text")

# Optional image if you have it
if os.path.exists("workflow.png"):
    st.image("workflow.png", use_column_width=True)