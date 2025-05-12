# python-wk7-basic-data-analysis
Explanation:
Data Loading:

You can load either the Iris dataset from sklearn or any custom CSV dataset (just replace the df loading line with pd.read_csv('your_dataset.csv')).

Data Exploration:

The script prints the first few rows, checks the data types, and handles any missing values (it fills missing values with the mean in this case).

Basic Data Analysis:

Basic statistics are calculated using .describe().

It groups the data by the species and calculates the mean of numerical columns for each group.

Visualizations:

Bar Chart: Shows the average petal length per species.

Histogram: Plots the distribution of petal length.

Scatter Plot: Visualizes the relationship between sepal length and petal length.

Plot Customization:

The script customizes the plots with titles, axis labels, legends, and colors.

How to Run:
Save this script in a file with a .py extension (e.g., data_analysis.py).

Make sure to have pandas, matplotlib, and seaborn installed (if not, install them using pip install pandas matplotlib seaborn).

Run the script in your Python environment, and it will display the plots.
