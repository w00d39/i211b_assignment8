Overview
This Python script, assignment8.py, is designed to analyze two datasets: an exercise dataset (Exercise_Data.csv) and the built-in planets dataset from Seaborn. The script generates various visualizations to explore relationships, distributions, and categorical trends in the data.

The script contains two main functions:

exercise_analysis(): Analyzes exercise data and generates visualizations related to pulse rates, diets, and exercise types.
planets_analysis(): Analyzes the planets dataset and generates relational, distributional, and categorical plots to explore planetary characteristics.
Dependencies
The script requires the following Python libraries:

NumPy: For numerical operations.
Pandas: For data manipulation and analysis.
Seaborn: For creating statistical visualizations.
Matplotlib: For plotting and figure customization.

Functions
1. exercise_analysis()
This function analyzes the Exercise_Data.csv file, which contains data on pulse rates, diets, and exercise types. It generates the following visualizations:

Heatmap:

Displays the average pulse rates for each exercise type (kind) across three time intervals (1 min, 15 min, 30 min).
Purpose: To identify trends in pulse rates for different exercise types.
Categorical Plot:

A bar plot showing pulse rates by diet and time interval, separated by exercise type.
Purpose: To compare pulse rates across diets and exercise types.
Key Steps in the Function:

Loads the Exercise_Data.csv file using Pandas.
Groups the data by kind (exercise type) to calculate average pulse rates.
Reshapes the data using pd.melt() to prepare it for categorical plotting.
Generates:
A heatmap using sns.heatmap().
A categorical bar plot using sns.catplot().
2. planets_analysis()
This function analyzes the planets dataset from Seaborn, which contains information about exoplanets discovered using various methods. It generates six visualizations:

Relational Plots:
Orbital Period vs Planet Mass:

A scatter plot showing the relationship between orbital period and planet mass, colored by discovery method.
Purpose: To explore how orbital periods and masses vary across planets.
Logarithmic Scale: Both axes use a log scale for better visualization of wide-ranging values.
Distance vs Orbital Period:

A scatter plot showing the relationship between distance and orbital period, colored by discovery method.
Purpose: To explore how distance and orbital periods are related.
Logarithmic Scale: Both axes use a log scale.
Distributional Plots:
Distribution of Planet Mass:

A histogram with a KDE (Kernel Density Estimate) line showing the distribution of planet masses.
Purpose: To understand the spread of planet masses.
Logarithmic Scale: The x-axis uses a log scale for better visualization.
Orbital Period by Discovery Method:

A box plot showing the distribution of orbital periods for each discovery method.
Purpose: To compare orbital periods across different discovery methods.
Logarithmic Scale: The y-axis uses a log scale.
Categorical Plots:
Average Planet Mass by Year:

A bar plot showing the average planet mass for each year of discovery.
Purpose: To observe trends in the mass of discovered planets over time.
Logarithmic Scale: The y-axis uses a log scale.
Count of Planets by Discovery Method:

A count plot showing the number of planets discovered using each method.
Purpose: To identify the most common discovery methods.
Key Steps in the Function:

Loads the planets dataset using Seaborn.
Generates:
Two relational plots using sns.relplot().
Two distributional plots using sns.histplot() and sns.boxplot().
Two categorical plots using sns.barplot() and sns.countplot().
How to Run the Script
Ensure the required libraries are installed.
Place the Exercise_Data.csv file in the same directory as the script.
Run the script using Python:
The script will generate and display all the visualizations sequentially.

Expected Output
Exercise Analysis
Heatmap:
A grid showing average pulse rates for each exercise type and time interval.
Categorical Bar Plot:
Bar plots grouped by diet, showing pulse rates for different time intervals and exercise types.
Planets Analysis
Relational Plots:
Scatter plot: Orbital Period vs Planet Mass.
Scatter plot: Distance vs Orbital Period.
Distributional Plots:
Histogram: Distribution of Planet Mass.
Box plot: Orbital Period by Discovery Method.
Categorical Plots:
Bar plot: Average Planet Mass by Year.
Count plot: Count of Planets by Discovery Method.
File Structure
Customization
You can customize the script by:

Modifying the datasets:
Replace Exercise_Data.csv with your own dataset, ensuring it has similar columns (diet, kind, 1 min, 15 min, 30 min).
Adjusting visualizations:
Change color palettes, figure sizes, or add/remove plots as needed.
