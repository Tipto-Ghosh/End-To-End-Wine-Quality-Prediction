# Wine Quality Dataset Analysis Report

## Dataset Overview

**Dataset Dimensions:** 6,497 rows × 14 columns  
**Data Quality:** No missing values detected  
**Target Variable:** Wine quality rating

## Feature Information

The dataset contains the following features related to wine characteristics:

| Feature | Description | Data Type |
|---------|-------------|-----------|
| wine type | Type/category of wine | Categorical |
| fixed acidity | Non-volatile acids in wine (tartaric acid) | Numerical |
| volatile acidity | Amount of acetic acid in wine | Numerical |
| citric acid | Citric acid content (adds freshness) | Numerical |
| residual sugar | Sugar remaining after fermentation | Numerical |
| chlorides | Salt content in wine | Numerical |
| free sulfur dioxide | Free form SO2 (prevents microbial growth) | Numerical |
| total sulfur dioxide | Total SO2 content (bound + free) | Numerical |
| density | Density of wine (depends on alcohol and sugar) | Numerical |
| pH | Acidity level (scale 0-14) | Numerical |
| sulphates | Wine additive (potassium sulphate) | Numerical |
| alcohol | Alcohol percentage by volume | Numerical |
| quality | Wine quality rating (target variable) | Numerical |

## Univariate Analysis Results

### Data Distribution and Transformations Required

#### Wine Quality Distribution
- Dataset contains distinct wine quality rating values
- Target variable shows clear categorical distribution

![Wine Quality Distribution](wine%20grpahs/download%20(1).png)

#### Fixed Acidity
- **Distribution:** Right-skewed
- **Outliers:** None detected
- **Transformation:** Log transformation recommended (no negative/zero values)
- **Result:** After transformation, distribution becomes more normalized

![Fixed Acidity - After Log Transformation](wine%20grpahs/download%20(2).png)

#### Volatile Acidity
- **Distribution:** Right-skewed
- **Outliers:** None detected
- **Data Range:** Maximum value 1.6 (very small values overall)
- **Transformations:** Log transformation + scaling required

**Before Transformation** | **After Transformation**
:-------------------------:|:-------------------------:
![Volatile Acidity - Before](wine%20grpahs/download%20(3).png) | ![Volatile Acidity - After](wine%20grpahs/download%20(4).png)

#### Citric Acid
- **Outliers:** Present (threshold: values > 0.95)
- **Data Cleaning:** Remove rows where citric acid > 0.95

**Before Transformation** | **After Transformation**
:-------------------------:|:-------------------------:
![Citric Acid - Before](wine%20grpahs/download%20(5).png) | ![Citric Acid - After](wine%20grpahs/download%20(6).png)

#### Residual Sugar
- **Outliers:** Present (threshold: values > 25)
- **Data Cleaning:** Remove rows where residual sugar > 25

#### Chlorides
- **Distribution:** Right-skewed
- **Transformation:** Log transformation recommended

**Before Transformation** | **After Transformation**
:-------------------------:|:-------------------------:
![Chlorides - Before](wine%20grpahs/download%20(7).png) | ![Chlorides - After](wine%20grpahs/download%20(8).png)

#### Free Sulfur Dioxide
- **Outliers:** Present (threshold: values > 120)
- **Distribution:** Right-skewed
- **Data Cleaning:** Remove rows where free sulfur dioxide > 120
- **Transformation:** Square root transformation (log transform ineffective)

**Before Transformation** | **After Square Root Transformation**
:-------------------------:|:-------------------------:
![Free SO2 - Before](wine%20grpahs/download%20(9).png) | ![Free SO2 - After](wine%20grpahs/download%20(11).png)

#### Total Sulfur Dioxide
- **Outliers:** Present (threshold: values > 280)
- **Data Cleaning:** Remove rows where total sulfur dioxide > 280

**Before Outlier Removal** | **After Outlier Removal**
:-------------------------:|:-------------------------:
![Total SO2 - Before](wine%20grpahs/download%20(12).png) | ![Total SO2 - After](wine%20grpahs/download%20(13).png)

#### Sulphates
- **Distribution:** Right-skewed
- **Transformation:** Log transformation recommended

#### pH
- **Distribution:** Normally distributed
- **Outliers:** None detected
- **Note:** Well-balanced distribution, no transformation needed

![pH Distribution](wine%20grpahs/download%20(14).png)

---

## Bivariate Analysis Results

### Feature Correlation Overview

The correlation heatmap below shows the relationships between all features and wine quality:

![Feature Correlation Matrix](wine%20grpahs/download%20(18).png)

### Feature-Quality Relationships

#### Strong Predictors (Keep)

**Volatile Acidity**
- **Relationship:** Negative correlation with quality
- **Pattern:** As volatile acidity increases, wine quality decreases

**Citric Acid**
- **Relationship:** Positive correlation with quality
- **Pattern:** Higher citric acid content associated with better quality

**Residual Sugar**
- **Relationship:** Complex non-linear pattern
- **Pattern:** High values for mid-quality wines (5-6 rating)
- **Note:** Very high residual sugar indicates either very high or very low quality

**Chlorides**
- **Relationship:** Strong negative correlation
- **Pattern:** Lower chlorides associated with higher quality wines

![Chlorides vs Quality](wine%20grpahs/download%20(19).png)

**Free Sulfur Dioxide**
- **Relationship:** Optimal range effect
- **Pattern:** 
  - Too high → Poor quality
  - Too low → Poor quality
  - Mid-level values → Good quality

![Free Sulfur Dioxide vs Quality](wine%20grpahs/download%20(20).png)

**Alcohol**
- **Relationship:** Positive correlation with quality
- **Pattern:** Higher alcohol content associated with better wine quality

![Alcohol vs Quality](wine%20grpahs/download%20(21).png)

#### Weak Predictors (Recommended for Removal)

**Fixed Acidity**
- **Correlation:** -0.08 (very weak)
- **Pattern:** Nearly constant across all quality levels
- **Recommendation:** Drop this feature

**Density**
- **Pattern:** No significant variation across quality levels
- **Recommendation:** Drop this feature

**pH**
- **Pattern:** Stable across different quality ratings
- **Relationship:** Wine quality not strongly dependent on pH
- **Recommendation:** Drop this feature

**Sulphates**
- **Pattern:** Similar values across most quality levels
- **Note:** Slightly lower for highest quality (rating 9)
- **Recommendation:** Drop this feature

## Data Preprocessing Recommendations

### 1. Outlier Removal
- Remove rows where `citric acid > 0.95`
- Remove rows where `residual sugar > 25`
- Remove rows where `free sulfur dioxide > 120`
- Remove rows where `total sulfur dioxide > 280`

### 2. Feature Transformations
- Apply **log transformation** to: fixed acidity, volatile acidity, chlorides, sulphates
- Apply **square root transformation** to: free sulfur dioxide
- Apply **scaling** to volatile acidity after log transformation

### 3. Feature Selection
**Keep these features:**
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- alcohol
- wine type (if categorical analysis supports retention)

**Remove these features:**
- fixed acidity
- density
- pH
- sulphates

## Final Dataset Characteristics

**Expected rows after cleaning:** < 6,497 (due to outlier removal)  
**Recommended features for modeling:** 7-8 features  
**Target variable:** quality (wine quality rating)

This preprocessing approach will result in a cleaner dataset with stronger predictive features for wine quality modeling.