import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

#step 01 Load the Data Set
df = pd.read_csv('sales.csv')

#step 02 Data set formating and sorting
df["date"] = pd.to_datetime(df["date"])
df=df.sort_values("date")

#step 03 Create Lag Features
df["sales_lag_1"]=df["sales"].shift(1)
df["sales_lag_2"]=df["sales"].shift(2)
df["sales_lag_3"]=df["sales"].shift(3)
df["sales_lag_12"]=df["sales"].shift(12)

#step 04 Missing value Drop
df = df.dropna()

#step 05 Input(X) and Target(Y)
X=df[["sales_lag_1", "sales_lag_2", "sales_lag_3", "sales_lag_12"]]#Promt
Y=df['sales']#Ans

#step 06 Train-Test Split
train_size = int(0.8*len(df))
X_train=X[:train_size]
X_test=X[train_size:]

Y_train=Y[:train_size]
Y_test=Y[train_size:]

#step 07 Create Model and Train
model = LinearRegression()
model.fit(X_train, Y_train)

#step 08 Model Train Accuracy
y_pred = model.predict(X_test)
mae = mean_absolute_error(Y_test, y_pred)
print(mae)
print("Model MAE:",round(mae,2))

#step 09 Save the Model
joblib.dump(model, 'model.pkl')

print("Model Trained Successfully")
print("Model Saved Successfully")















