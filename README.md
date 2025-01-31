# Wine Quality Analysis

## ** Project Overview**
This project analyzes **wine quality** using **machine learning**. It trains a model on the **Wine Quality Dataset** and evaluates it using **Mean Squared Error (MSE) and R² score**.  
It provides two ways to run the analysis:
1. **Using Docker**
2. **Using a Shell Script**  
---
## **🚀 Running the Project**
You can run the project using **Docker** or **a Shell Script (without Docker).**

### **🔹 Option 1: Using Docker**
1️⃣ **Clone the repository**:
```sh
git clone https://github.com/Tani303/Wine_Quality_Analysis.git
cd Wine_Quality_Analysis
---
- **Build Docker Image**
```sh
  docker build -t wine_quality_analysis_app .
  
---
**Run the Docker Image**

docker run --rm wine_quality_analysis_app

## **📂 Dataset**
- The dataset used is `winequality-red.csv`, available in the **`data/`** folder.
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wine+Quality).

---


