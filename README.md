# Salary_Prediction_Model (XGboost - R2 of 93%)

# Methodology

- A structured machine learning approach was adopted to predict employee salary. The dataset was first explored using exploratory data analysis (EDA) to understand feature distributions, relationships, and potential data quality issues. Missing values in selected numerical variables were handled using appropriate imputation techniques to preserve dataset size.
- Categorical variables (e.g., Department and Education Level) were encoded using one-hot encoding, while numerical variables were scaled using standardisation. These preprocessing steps were integrated into a unified pipeline to ensure consistency and prevent data leakage.
- Multiple models, including Linear Regression, Decision Tree, Random Forest, and XGBoost, were evaluated using 5-fold cross-validation. Model performance was assessed using Mean Absolute Error (MAE) and R2. The best-performing model (XGBoost) was selected and further improved using hyperparameter tuning via GridSearchCV.
- Additionally, a log transformation of the target variable was applied using TransformedTargetRegressor to reduce the influence of extreme values and improve model stability.

# Results

The tuned XGBoost model achieved the strongest performance among all evaluated models.

- R2 Score: ~0.93
- MAE: 8040.408671875

Residual analysis showed that errors were generally evenly distributed around zero, with reduced variance compared to earlier models. The predicted vs actual plot indicated strong alignment with the ideal prediction line, confirming high model accuracy.
Feature importance analysis revealed that department, education level, performance rating, and years of experience were the most influential predictors of salary.

# Model Interpretation
The results indicate that salary prediction is strongly influenced by job role (department), level of education, and individual performance, with experience also playing a significant role. The dominance of categorical variables suggests that structural factors (such as job function) are key drivers of salary differences.
The application of a log transformation improved model stability by reducing the impact of extreme salary values, leading to more consistent predictions across the salary range. Although a slight reduction in R2 was observed in some cases, the overall robustness and generalisation of the model improved.
The final XGBoost model demonstrates strong predictive capability, with high accuracy and good generalisation performance. Minor deviations at higher salary levels suggest some remaining difficulty in modelling extreme values, which is typical in real-world salary data.

# Conclusions

- The model generally informed us that Salary is a function of department (role type), education, performance, and experience.

- The model was implemented using a pipeline, which ensures a cleaner and more consistent workflow by integrating preprocessing and modelling steps. Additionally, cross-validation was applied to achieve more reliable performance evaluation across multiple data splits.

- The target variable was also log-transformed to reduce the influence of extreme values and improve model stability, particularly for higher salary ranges

- Four different models were compared, XGboost seems to be the best (the pipeline were kept, even tho XGboost will still perform well without scaling)

- Hyperparamer tunning of XGboost enhanced its performace.

- The model demonstrates good generalisation on the test data, despite the relatively small dataset size, indicating that it captures the underlying patterns effectively.
