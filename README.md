# Wine Quality Analysis

## Introduction
This project analyzes wine quality based on physicochemical properties using machine learning. The pipeline includes data preprocessing, model training, and evaluation using **RandomForestRegressor**.

## Prerequisites
- Docker installed on your machine.

## Setup & Usage

### Cloning the Repository:
```
git clone https://github.com/Tani303/Wine_Quality_Analysis.git
```
### Change to the project directory
```
cd Wine_Quality_Analysis
```
## Running the Application:
- **Build Docker Image**
```
docker build -t wine_quality_analysis_app .
```
- **Run the Docker Image**
```
docker run wine_quality_analysis_app
```
- **In orderr to see the result plot and text file use the command below**
```
docker run --rm -v "${PWD}/results:/wine_quality_analysis/results" wine_quality_analysis_app
```

## Dataset Information
- **Name:** Wine Quality Dataset  
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)  
- **File Used:** `winequality-red.csv`  
- **Location:** `data/`  
- **Description:**  
This dataset contains physicochemical attributes (such as acidity, alcohol content, pH, etc.) of different **red wine** samples, along with a **quality score (0-10)** given by wine tasters. The goal of the analysis is to predict the **quality score** based on these features.

- **Features:**
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (Target Variable)

## What Happens When You Run the Code?
- The script **loads the dataset** from the `data/` folder.
- **Preprocesses the data** and **splits it** into training and testing sets.
- A **RandomForestRegressor model** is trained to predict wine quality.
- The model's performance is **evaluated** using **Mean Squared Error (MSE)** and **R² Score**.
- Results are displayed in the **console** and in the results folder depending on the chosen command.
