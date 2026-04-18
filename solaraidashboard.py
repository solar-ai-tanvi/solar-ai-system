# import streamlit as st
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # -----------------------------
# # Title
# # -----------------------------
# st.title("☀️ Solar AI Dashboard")
# st.write("AI-Based Solar Power Prediction System")

# # -----------------------------
# # Data
# # -----------------------------
# data = {
#     'Temperature':[30,32,34,36,38,40],
#     'Sunlight':[2,4,6,8,10,12],
#     'Powergenerate':[100,200,300,400,500,600]
# }

# df = pd.DataFrame(data)

# # -----------------------------
# # Model Training
# # -----------------------------
# X = df[['Temperature','Sunlight']]
# y = df['Powergenerate']

# model = LinearRegression()
# model.fit(X,y)

# # -----------------------------
# # User Input
# # -----------------------------
# st.sidebar.header("Enter Input Values")

# temp = st.sidebar.slider("Temperature (°C)", 20, 50, 30)
# sun = st.sidebar.slider("Sunlight (hrs)", 1, 12, 5)

# # -----------------------------
# # Prediction
# # -----------------------------
# input_data = pd.DataFrame([[temp, sun]], columns=['Temperature','Sunlight'])
# prediction = model.predict(input_data)[0]

# st.subheader("🔮 Prediction Result")
# st.write(f"Predicted Power Generation: **{prediction:.2f}**")

# # -----------------------------
# # Efficiency Check
# # -----------------------------
# actual_power = st.number_input("Enter Actual Power Generated", min_value=0.0)

# if actual_power > 0:
#     efficiency = (actual_power / prediction) * 100
#     st.write(f"⚡ Efficiency: **{efficiency:.2f}%**")

#     if efficiency < 80:
#         st.error("⚠️ Fault Detected! Panel may be dirty/damaged")
#     elif efficiency < 95:
#         st.warning("⚠️ Moderate Performance")
#     else:
#         st.success("✅ System Working Efficiently")

# # -----------------------------
# # Graphs
# # -----------------------------

# st.subheader("📊 Data Visualization")

# st.line_chart(df.set_index('Sunlight')['Powergenerate'])

# st.scatter_chart(df[['Temperature','Powergenerate']])





# import streamlit as st
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import time
# import random

# # -----------------------------
# # Title
# # -----------------------------
# st.title("☀️ Solar AI System")
# st.caption("AI-Based Real-Time Solar Monitoring & Fault Detection")

# # -----------------------------
# # Project Description
# # -----------------------------
# st.markdown("""
# ### 🚀 About This Project
# This AI system predicts solar power using temperature and sunlight data.
# It also detects faults and calculates efficiency in real-time.
# """)

# # -----------------------------
# # Data
# # -----------------------------
# data = {
#     'Temperature':[30,32,34,36,38,40],
#     'Sunlight':[2,4,6,8,10,12],
#     'Powergenerate':[100,200,300,400,500,600]
# }

# df = pd.DataFrame(data)

# # -----------------------------
# # Model Training
# # -----------------------------
# X = df[['Temperature','Sunlight']]
# y = df['Powergenerate']

# model = LinearRegression()
# model.fit(X,y)

# # -----------------------------
# # Sidebar Input
# # -----------------------------
# st.sidebar.header("Enter Input Values")

# temp = st.sidebar.slider("Temperature (°C)", 20, 50, 30)
# sun = st.sidebar.slider("Sunlight (hrs)", 1, 12, 5)

# # -----------------------------
# # Prediction
# # -----------------------------
# input_data = pd.DataFrame([[temp, sun]], columns=['Temperature','Sunlight'])
# prediction = model.predict(input_data)[0]

# st.subheader("🔮 Prediction Result")
# st.write(f"Predicted Power Generation: **{prediction:.2f}**")

# # -----------------------------
# # Metrics (UI Upgrade)
# # -----------------------------
# st.subheader("📊 Live Metrics")

# col1, col2 = st.columns(2)
# col1.metric("Temperature", f"{temp} °C")
# col2.metric("Sunlight", f"{sun} hrs")

# st.metric("Predicted Power", f"{prediction:.2f}")

# # -----------------------------
# # Status
# # -----------------------------
# if prediction < 200:
#     st.error("🔴 Low Power Generation")
# elif prediction < 400:
#     st.warning("🟡 Moderate Performance")
# else:
#     st.success("🟢 Good Performance")

# # -----------------------------
# # Efficiency Check
# # -----------------------------
# st.subheader("⚡ Efficiency Check")

# actual_power = st.number_input("Enter Actual Power Generated", min_value=0.0)

# if actual_power > 0:
#     efficiency = (actual_power / prediction) * 100
#     st.write(f"Efficiency: **{efficiency:.2f}%**")

#     if efficiency < 80:
#         st.error("⚠️ Fault Detected! Panel may be dirty/damaged")
#     elif efficiency < 95:
#         st.warning("⚠️ Moderate Performance")
#     else:
#         st.success("✅ System Working Efficiently")

# # -----------------------------
# # Graph
# # -----------------------------
# st.subheader("📈 Power Trend")
# st.line_chart(df.set_index('Sunlight')['Powergenerate'])

# # -----------------------------
# # Live Monitoring Simulation
# # -----------------------------
# st.subheader("🔄 Live Monitoring")

# if st.button("Start Live Monitoring"):

#     for i in range(5):
#         temp_live = random.randint(30,45)
#         sun_live = random.randint(2,12)

#         input_live = pd.DataFrame([[temp_live, sun_live]],
#                                   columns=['Temperature','Sunlight'])

#         pred_live = model.predict(input_live)[0]

#         st.write("-----------------------------")
#         st.write(f"Temperature: {temp_live} °C")
#         st.write(f"Sunlight: {sun_live} hrs")
#         st.write(f"Predicted Power: {pred_live:.2f}")

#         time.sleep(1) 


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