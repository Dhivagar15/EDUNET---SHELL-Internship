Climate Risk and Disaster Management
This repository contains the work for the AICTE Internship on Climate Risk and Disaster Management, focusing on a two-week project that involves data analysis and exploratory data analysis (EDA).

Project Overview
The goal of this project is to analyze data related to climate risk and disaster management. The analysis is structured in two parts:

Week 1: Focused on initial data exploration. This involved loading a suitable dataset, checking for missing values, and getting a statistical summary of the data.

Week 2: Focused on in-depth data analysis. This included performing Exploratory Data Analysis (EDA) with visualizations, cleaning and transforming the data, and selecting key features for further modeling.

Dataset
The dataset used for this project is world_risk_index.csv. It contains various metrics related to a country's exposure, vulnerability, and overall risk to natural disasters.

Data Source: [You can add a link to the Kaggle page or original source here]

Key Tasks & Methods
The following steps were performed in the Week-1-2-Project.ipynb Jupyter Notebook:

Initial Exploration:

Imported pandas and numpy libraries.

Loaded the .csv dataset into a DataFrame.

Used .info() and .describe() to understand the data's structure and summary statistics.

Checked for missing values with .isnull().sum().

Exploratory Data Analysis (EDA):

Visualized data distributions using histograms to understand the spread of key variables like the World Risk Index (WRI).

Used correlation heatmaps to identify relationships between different numeric features.

Data Transformation & Cleaning:

Handled missing values by filling them with a mean/mode or dropping them, depending on the column.

Cleaned column names by removing extra spaces.

Created a new categorical feature (WRI_Category) by binning the continuous WRI variable.

Feature Selection:

Identified the most relevant features for analysis based on the EDA and correlation analysis.

Repository Contents
Week-1-2-Project.ipynb: The Jupyter Notebook containing all the Python code and analysis.

world_risk_index.csv: The dataset used for the project.
