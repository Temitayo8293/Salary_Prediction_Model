# Salary_Prediction_Model (XGboost - R2 of 93%)
This is a salary predictor regression model

- The model generally informed us that Salary is a function of department (role type), education, performance, and experience.

- The model was implemented using a pipeline, which ensures a cleaner and more consistent workflow by integrating preprocessing and modelling steps. Additionally, cross-validation was applied to achieve more reliable performance evaluation across multiple data splits.

- The target variable was also log-transformed to reduce the influence of extreme values and improve model stability, particularly for higher salary ranges

- Four different models were compared, XGboost seems to be the best (the pipeline were kept, even tho XGboost will still perform well without scaling)

- Hyperparamer tunning of XGboost enhanced its performace.

- The model demonstrates good generalisation on the test data, despite the relatively small dataset size, indicating that it captures the underlying patterns effectively.

