import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt
import seaborn as sns

# Set paths for data and results
data_path = './data/winequality-red.csv'
plots_path = './results/plots/'
results_path = './results/'

# Ensure the results directories exist
os.makedirs(plots_path, exist_ok=True)
os.makedirs(results_path, exist_ok=True)

def load_data(filepath):
    """Load the dataset into a pandas DataFrame."""
    return pd.read_csv(filepath, sep=';')

def preprocess_data(df):
    """Preprocess the data: clean and prepare for analysis."""
    df.dropna(inplace=True)
    return df

def plot_quality_distribution(df, output_path):
    """Plot the distribution of wine qualities."""
    plt.figure(figsize=(10, 6))
    sns.countplot(x='quality', data=df, color='b')  # Using color instead of palette
    plt.title('Distribution of Wine Quality')
    plt.xlabel('Quality')
    plt.ylabel('Frequency')
    plt.savefig(output_path)
    plt.close()

def plot_horizontal_correlation_bar_plot(df, output_path):
    """Create a horizontal bar plot to show the correlation of features with wine quality."""
    corr = df.corr()
    wine_quality_correlations = corr['quality'].drop('quality').sort_values()
    plt.figure(figsize=(10, 12))
    sns.barplot(x=wine_quality_correlations.values, y=wine_quality_correlations.index, color='b')  # Using color instead of palette
    plt.xlabel('Correlation with Wine Quality')
    plt.ylabel('Features')
    plt.title('Correlation of Features with Wine Quality')
    plt.savefig(output_path)
    plt.close()

def detect_and_remove_outliers(X, y):
    """Remove outliers using Isolation Forest."""
    isol_forest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    is_inlier = isol_forest.fit_predict(X)
    return X[is_inlier == 1], y[is_inlier == 1]

def feature_selection(X_train, X_test, y_train):
    """Feature selection using RandomForestRegressor for its importance."""
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    sfm = SelectFromModel(model, threshold='median', prefit=True)
    feature_indices = sfm.get_support(indices=True)
    X_train_selected = X_train.iloc[:, feature_indices]
    X_test_selected = X_test.iloc[:, feature_indices]
    return X_train_selected, X_test_selected

def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train the RandomForestRegressor and evaluate it."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    print(f'R2 Score: {r2}')
    # Write results to a text file
    with open(results_path + 'evaluation_results.txt', 'w') as f:
        f.write(f'Mean Squared Error: {mse}\n')
        f.write(f'R2 Score: {r2}\n')

def main():
    df = load_data(data_path)
    df = preprocess_data(df)
    plot_quality_distribution(df, os.path.join(plots_path, 'quality_distribution.png'))
    plot_horizontal_correlation_bar_plot(df, os.path.join(plots_path, 'horizontal_correlation_bar_plot.png'))

    X = df.drop('quality', axis=1)
    y = df['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, y_train = detect_and_remove_outliers(X_train, y_train)
    X_train, X_test = feature_selection(X_train, X_test, y_train)

    train_and_evaluate(X_train, X_test, y_train, y_test)

if __name__ == '__main__':
    main()
