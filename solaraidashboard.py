
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("☀️ Solar AI Dashboard")

# ✅ Updated Dataset (Realistic)
data = {
    'Temperature': [20,22,25,28,30,32,35,38,40,42,45],
    'Sunlight':    [2,3,4,5,6,7,8,6,5,4,3],
    'Humidity':    [30,35,40,45,50,55,60,65,70,75,80],
    'DustLevel':   [10,15,20,25,30,35,40,50,60,70,80],
    'Powergenerate':[80,120,180,250,320,400,480,420,350,280,200]
}

df = pd.DataFrame(data)

# ✅ Model Training
X = df[['Temperature','Sunlight','Humidity','DustLevel']]
y = df['Powergenerate']

model = LinearRegression()
model.fit(X,y)

# 🎯 User Inputs (NEW)
st.sidebar.header("Enter Conditions")

temp = st.sidebar.slider("Temperature", 20, 50, 30)
sun = st.sidebar.slider("Sunlight", 1, 10, 5)
hum = st.sidebar.slider("Humidity", 20, 90, 50)
dust = st.sidebar.slider("Dust Level", 0, 100, 30)

# ✅ Prediction (Fixed Warning also)
input_data = pd.DataFrame([[temp, sun, hum, dust]],
columns=['Temperature','Sunlight','Humidity','DustLevel'])

prediction = model.predict(input_data)[0]

# ✅ Output
st.subheader("🔋 Predicted Power")
st.success(f"{prediction:.2f} Units")

# ✅ Condition Check
if prediction < 200:
    st.error("⚠️ Low Power Generation")
elif prediction < 400:
    st.warning("⚠️ Moderate Performance")
else:
    st.success("✅ Good Performance")

# ✅ Graph (Improved)
st.subheader("📊 Sunlight vs Power")

chart_data = df[['Sunlight','Powergenerate']]
st.line_chart(chart_data)

# ✅ Show Prediction Point
st.write("📍 Current Input vs Prediction")
st.write(input_data) 
