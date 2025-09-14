

# 📊 Data Analysis with Pandas & Visualization with Matplotlib

This project demonstrates **data analysis** and **visualization** using Python libraries: **Pandas**, **Matplotlib**, **Seaborn**, and **NumPy**.
It loads a dataset, performs exploratory data analysis (EDA), and creates insightful visualizations.

---

## 📂 Project Structure

* **Data Loading & Cleaning**: Reads a CSV file, inspects missing values, and cleans the dataset.
* **Basic Data Analysis**: Generates summary statistics, calculates total revenue, identifies best-selling products, and derives insights.
* **Data Visualization**: Creates multiple plots to better understand sales trends and distributions.
* **Findings & Observations**: Summarizes key insights from the analysis.

---

## ⚙️ Requirements

Make sure you have the following installed:

```bash
pip install pandas matplotlib seaborn numpy
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Place your dataset (e.g., `sales_data.csv`) in the project folder.
3. Update the `file_path` in the script with the correct location of your dataset.
4. Run the script:

```bash
python assignment.py
```

---

## 📊 Features

### ✅ Data Loading & Cleaning

* Loads sales data from a CSV file.
* Handles missing values by filling them with zeros.
* Displays dataset info and preview (first 5 rows).

### ✅ Basic Data Analysis

* Summary statistics (mean, median, std, etc.).
* Average revenue by product.
* Total revenue calculation.
* Best-selling product identification.

### ✅ Visualizations

1. **📈 Line Chart** – Daily sales trend.
2. **📊 Bar Chart** – Average revenue by product.
3. **📦 Histogram** – Distribution of quantity sold.
4. **🔵 Scatter Plot** – Quantity sold vs revenue.

### ✅ Insights & Observations

* Highlights top-performing products.
* Reveals revenue distribution across products.
* Identifies sales trends and fluctuations.

---

## 📌 Example Insights (from sample dataset)

* **Best-selling product**: `Product X` (highest units sold).
* **Total revenue**: `$123,456`.
* **Trend**: Daily revenue fluctuates across different dates.
* **Observation**: Certain products contribute significantly more revenue.

---

## 📷 Sample Visualizations

**Daily Sales Trend**
![Line Chart Example](https://matplotlib.org/stable/_images/sphx_glr_lines_bars_and_markers_001.png)

**Revenue by Product**
![Bar Chart Example](https://matplotlib.org/stable/_images/sphx_glr_bar_001.png)

---

## 📝 Notes

* Ensure your dataset contains the following columns for full functionality:

  * `Date`
  * `Product`
  * `Quantity Sold`
  * `Revenue ($)`
* If your dataset has different column names, adjust the code accordingly.

---

## 👨‍💻 Author

Developed as part of a **Python Data Analysis Assignment** using Pandas & Matplotlib.


