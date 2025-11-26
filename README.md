# StudentPerformance

# Data Science Project I  
### Student Performance Prediction (Fall 2025)

This project analyzes anonymized student assessment data from six different sections of a course.  
The goal is to explore the data, perform preprocessing, and build regression models to answer the following research questions:

##  Research Questions
1. **RQ1:** How accurately can we predict student marks in **Midterm I**?
2. **RQ2:** How accurately can we predict student marks in **Midterm II**?
3. **RQ3:** How accurately can we predict student marks in the **Final Examination**?

---

## Project Structure

project/
│
├── data/
│ ├── raw/
│ │ └── dataset.xlsx # Contains all 6 sheets
│ │
│ └── processed/
│ └── final_dataset.csv # Will be created after preprocessing
│
├── notebooks/
│ └── project.ipynb # Main notebook for EDA, models, bootstrapping
│
├── src/ # Additional helper scripts 
│
├── dashboard/
│ └── app.py # Streamlit or Gradio dashboard (later)
│
├── workflow-diagram/
│ └── workflow.png # Project pipeline diagram
│
└── README.md # Project documentation

##  Requirements
Install these packages:

pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
plotly

##  Notes
- Excel dataset contains six sheets, each representing a different section.
- No data leakage is allowed in preprocessing or modeling.
- Final processed dataset must be saved as a CSV file.

## Contributors

