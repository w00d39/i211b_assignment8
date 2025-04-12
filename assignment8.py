import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def exercise_analysis():
    """
    THis is a fruitful function that analyzes the exercise data. The first part of the function is a 
    heatmap that shows the average pulse rates for each exercise type. The second part of the function is a
    bar plot that shows the average pulse rates for each exercise type and diet. 
    """

    #id  1 min  15 min  30 min     diet  kind
    exercise_df = pd.read_csv('Exercise_Data.csv')
    #Grouping by exercise type and mean pulse rates for each time interval
    grouped_pulse_df = exercise_df.groupby('kind')[['1 min', '15 min', '30 min']].mean()
    #all pulses into one column
    melted_df = pd.melt(
        exercise_df,
        id_vars=['diet', 'kind'],  # Keep 'diet' and 'kind' as identifiers
        value_vars=['1 min', '15 min', '30 min'],  # Columns to melt
        var_name='time_interval',  # New column for time intervals
        value_name='pulse_rate'  # New column for pulse rates
    )
    
    #figure for the exercise analysis
    plt.figure(figsize=(10, 8))  
    #heatmap that shows the average pulse rates for each exercise type the cbar shows the average pulse rate
    #for each exercise type
    sns.heatmap(grouped_pulse_df, annot=True, cmap='coolwarm', fmt='.1f', cbar_kws={'label': 'Average Pulse Rate'})
    
    plt.title('Average Pulse Rates vs Exercise Type') #title
    plt.xlabel('Time Intervals') #x label
    plt.ylabel('Exercise Type') #y label
    
    #pulse values by diet and by type of exercise
    cat_plot = sns.catplot(
        data=melted_df,
        x='diet',
        y='pulse_rate',
        hue='time_interval',  # Differentiate by time interval
        col='kind',  # Separate plots by exercise type
        kind='bar',  # Use a bar plot
        height=6,  # Adjust the height of the plot
        aspect=1 , # Adjust the aspect ratio
        palette = 'pastel'
    )
       




    return plt.show()


def planets_analysis():
    """
    Obligatory psych line bc planets: You heard about Pluto? That's messed up, right?
    This is a void function because it is not returning anything. It is just plotting the data.
    THe first relational plot is a scatter plot that shows the relationship between the orbital period and the mass of the planets.
    The second relational plot is a scatter plot that shows the relationship between the distance and the orbital period of the planets.
    The first distribution plot is a histogram that shows the distribution of the mass of the planets.
    The second distribution plot is a box plot that shows the distribution of the orbital period by discovery method.
    The first categorical plot is a bar plot that shows the average mass of the planets by year.
    The second categorical plot is a count plot that shows the count of planets by discovery method.
    """
    planets_data = sns.load_dataset('planets')
    #method  number  orbital_period   mass  distance  year

 
# Relational Plot 1: Orbital Period vs Planet Mass
    relplot1 = sns.relplot(
        data=planets_data,
        x='orbital_period',
        y='mass',
        kind='scatter',  # Scatter plot
        hue='method',  # Differentiate by discovery method
        palette='viridis',
        height=6,
        aspect=1.5
    )
    relplot1.fig.suptitle('Orbital Period vs Planet Mass', y=1.02)
    relplot1.set(xscale='log', yscale='log')  # Log scale for to see better
    
    # Relational Plot 2: Distance vs Orbital Period
    relplot2 = sns.relplot(
        data=planets_data,
        x='distance',
        y='orbital_period',
        kind='scatter',  # Scatter plot
        hue='method',  # Differentiate by discovery method
        palette='coolwarm',
        height=6,
        aspect=1.5
    )
    relplot2.fig.suptitle('Distance vs Orbital Period', y=1.02)
    relplot2.set(xscale='log', yscale='log')  # Log scale for to see better
    
 
    # Distribution Plot 1: Distribution of Planet Mass
    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=planets_data,
        x='mass',
        kde=True,  # Add a Kernel Density Estimate (KDE) line
        color='blue',
        bins=30
    )
    plt.title('Distribution of Planet Mass')
    plt.xlabel('Mass')
    plt.ylabel('Frequency')
    plt.xscale('log')  # Use a logarithmic scale for better visualization
    plt.show()
    
    # Distribution Plot 2: Orbital Period by Discovery Method
    plt.figure(figsize=(12, 6))
    sns.boxplot(
        data=planets_data,
        x='method',
        y='orbital_period',
        palette='coolwarm'
    )
    plt.title('Orbital Period by Discovery Method')
    plt.xlabel('Discovery Method')
    plt.ylabel('Orbital Period')
    plt.yscale('log')  # Use a logarithmic scale for better visualization
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

# Categorical Plot 1: Average Planet Mass by Year
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=planets_data,
        x='year',
        y='mass',
        palette='viridis',
        ci=None  # Disable confidence intervals
    )
    plt.title('Average Planet Mass by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Mass')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.yscale('log')  # Use a logarithmic scale for better visualization
    plt.show()
    
    # Categorical Plot 2: Count of Planets by Discovery Method
    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=planets_data,
        x='method',
        palette='coolwarm'
    )
    plt.title('Count of Planets by Discovery Method')
    plt.xlabel('Discovery Method')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()


#exercise_analysis()
planets_analysis()