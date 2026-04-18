import joblib
import pandas as pd

#step 01 Load the Model
model=joblib.load('model.pkl')

#step 02 Prompt with Dataframe
input_data=pd.DataFrame({
    "sales_lag_1":[112000],
    "sales_lag_2":[180000],
    "sales_lag_3":[100300],
    "sales_lag_12":[70000],
})

#step 03 Get Prediction for next Month
next_month_sales=model.predict(input_data)
print(next_month_sales)









