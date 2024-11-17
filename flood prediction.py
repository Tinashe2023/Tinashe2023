#Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

#Load the dataset
file_path ="C:/Users/BRENDON/Downloads/flood.csv/flood.csv"
df = pd.read_csv(file_path)

#Display the first few rows of the dataset
print(df.head())

# Display basic statistics
print(df.describe())

#Correlation Analysis
# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=[np.number])

#Compute the correlation matrix
corr_matrix = numeric_df.corr()

#Plot the heatmap
plt.figure(figsize=(12, 9))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

#Predicting Flood Probability
#Define the features and target variable
X = numeric_df.drop(columns=['FloodProbability'])
y = numeric_df['FloodProbability']

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

#Make predictions on the test set
y_pred = model.predict(X_test)

#Calculate the prediction accuracy
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)


