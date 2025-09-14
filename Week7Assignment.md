# 🌸 Iris Dataset Analysis & Visualization

## 📘 Overview

This project demonstrates how to load, explore, analyze, and visualize the classic **Iris dataset** using Python libraries such as `pandas`, `matplotlib`, and `seaborn`. The goal is to practice data handling, statistical analysis, and basic plotting techniques in a clean and reproducible workflow.

---

## 🧠 Objectives

- Load and inspect a dataset using `pandas`
- Perform basic statistical analysis
- Visualize data using `matplotlib` and `seaborn`
- Identify patterns and insights from the dataset
- Handle errors and missing data gracefully

---

## 📂 Dataset

The Iris dataset is loaded directly from `sklearn.datasets`. It contains 150 samples of iris flowers with the following features:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)
- Species (Setosa, Versicolor, Virginica)

---

## 🛠️ Tools Used

- Python 3.x
- Jupyter Notebook / Python Script
- pandas
- matplotlib
- seaborn
- scikit-learn

---

## 📈 Tasks Completed

### ✅ Task 1: Load and Explore the Dataset
- Loaded the Iris dataset using `sklearn.datasets.load_iris()`
- Converted it into a `pandas` DataFrame
- Displayed the first few rows using `.head()`
- Checked data types and missing values
- Cleaned the dataset (no missing values in this case)

### ✅ Task 2: Basic Data Analysis
- Computed descriptive statistics using `.describe()`
- Grouped data by species and calculated mean values
- Identified key differences between flower species

### ✅ Task 3: Data Visualization
Created four customized plots:
1. **Line Chart** – Petal length across sample index
2. **Bar Chart** – Average petal length per species
3. **Histogram** – Distribution of sepal width
4. **Scatter Plot** – Sepal length vs petal length, colored by species

---

## 📌 Observations

- Setosa species has significantly smaller petal dimensions.
- Virginica shows the largest petal measurements.
- Sepal length and petal length are positively correlated.
- No missing data was found in the dataset.

---

## ⚠️ Error Handling

- Wrapped dataset loading in a `try-except` block to catch potential errors.
- Included checks for missing values and handled them appropriately.

---

## 📎 How to Run

1. Clone or download the repository.
2. Open the `.ipynb` notebook in Jupyter or run the `.py` script in your Python environment.
3. Ensure required libraries are installed:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
