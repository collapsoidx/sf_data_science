# Project 4. Machine Learning - Classification Task


### Description of the project
The technical challenge for a Data Scientist to build a machine learning model that predicts whether or not a customer will take advantage of a deposit offer based on the suggested characteristics.

### What case are we solving?
Business task: to determine the characteristics that can be used to identify customers who are more likely to open a deposit at a bank, and thereby increase the effectiveness of the marketing campaign.

**Competition conditions:**
Find finest solution based on metric.

**Quality metric:**
The results are evaluated by Accuracy metric.

**What we practice:**
This project involved a full-scale Data Science analysis, which included solving a Classification Task using the Scikit-learn library.


### Brief information about the data
We have been given data on the last marketing campaign that the bank ran: the task was to attract customers to open a deposit. You need to analyze this data, identify a pattern, and find the decisive factors that influenced the customer to invest in this particular bank. If you can do this, you will raise the bank's revenues and help you understand the target audience that needs to be attracted through advertising and various offers.



### Stages of work on the project
1. Primary Data Processing
2. Exploratory Data Analysis (EDA)
3. Feature selection and transformation
4. Solving the classification task: logistic regression and solving trees
5. Solving the classification task: ensembles of models and forecasting


### Results:

Stacking ensemble based on Decision Tree Classifier, Random Forest Classifier and Gradient Boosting Classifier with Logistic Regression as final estimator.

Best score:
* Train Accuracy score: 0.85
* Train Recall score: 0.86
* Test Accuracy score: 0.83
* Test Recall score: 0.83

### Conclusions:

In this project, a full range of assignments was conducted on a real Data Science case. I completed data exploration and cleansing by removing outliers and null values. For Exploratory Data Analysis, I used descriptive statistics for both quantitative and qualitative variables. During the feature engineering phase, I encoded and converted features. After checking for correlation, I normalized and selected the most valuable features. I created several models to achieve the best results by searching for hyperparameters. The best result in metrics was obtained by using a Stacking ensemble based on a Decision Tree Classifier, Random Forest Classifier, and Gradient Boosting Classifier with Logistic Regression as the final estimator.


If the information on this project seems interesting or useful to you, then I will be very grateful to you if you mark the repository and profile ⭐️⭐️⭐️-dami