
# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import time
import random

# Step 1: Dataset (Realistic Solar Data)
data = {
    'Temperature': [20,22,25,28,30,32,35,38,40,42,45],
    'Sunlight':    [2,3,4,5,6,7,8,6,5,4,3],
    'Humidity':    [30,35,40,45,50,55,60,65,70,75,80],
    'DustLevel':   [10,15,20,25,30,35,40,50,60,70,80],
    'Powergenerate':[80,120,180,250,320,400,480,420,350,280,200]
}

df = pd.DataFrame(data)

# Step 2: Features (Input) & Target (Output)
X = df[['Temperature','Sunlight','Humidity','DustLevel']]
y = df['Powergenerate']

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Data:\n", X_train, y_train)
print("Testing Data:\n", X_test, y_test)

# Step 4: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: User Input
Temperature = float(input("Enter Temperature = "))
Sunlight = float(input("Enter Sunlight = "))
Humidity = float(input("Enter Humidity = "))
DustLevel = float(input("Enter Dust Level = "))

# Convert input into DataFrame
input_data = pd.DataFrame([[Temperature, Sunlight, Humidity, DustLevel]],
columns=['Temperature','Sunlight','Humidity','DustLevel'])

# Step 6: Prediction
predicted_Powergenerate = model.predict(input_data)[0]

print(f"\nPredicted Power = {predicted_Powergenerate:.2f}")

# Step 7: Condition Check
if predicted_Powergenerate < 200:
    print("Warning: Low Power Generation")
else:
    print("System Working Normally")

# Step 8: 3D Graph Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Temperature'], df['Sunlight'], df['Powergenerate'])

ax.set_xlabel('Temperature')
ax.set_ylabel('Sunlight')
ax.set_zlabel('Power')

plt.title("3D Solar Power Data")
plt.show()

# Step 9: Efficiency Calculation
actual_power = float(input("Enter actual power generated: "))
efficiency = (actual_power / predicted_Powergenerate) * 100

print(f"System Efficiency: {efficiency:.2f}%")

if efficiency < 80:
    print("Fault Detected: Panel may be dirty or damaged!")
elif efficiency < 95:
    print("Moderate performance, check system")
else:
    print("System working efficiently")

# Step 10: Sunlight vs Power Graph
plt.figure()
plt.plot(df['Sunlight'], df['Powergenerate'], marker='o', label="Actual Data")

# Predicted point show
plt.scatter(Sunlight, predicted_Powergenerate, label="Predicted", marker='x')

plt.xlabel("Sunlight Hours")
plt.ylabel("Power Generated")
plt.title("Sunlight vs Power")
plt.legend()

plt.show()

# Step 11: Real-Time Simulation
print("\n------ Solar AI Real-Time Monitoring ------")

plt.ion()

for i in range(10):

    # Random real-time values
    Temperature = random.randint(20,45)
    Sunlight = random.randint(2,8)
    Humidity = random.randint(30,80)
    DustLevel = random.randint(10,80)

    input_data = pd.DataFrame([[Temperature, Sunlight, Humidity, DustLevel]],
    columns=['Temperature','Sunlight','Humidity','DustLevel'])

    predicted_Powergenerate = model.predict(input_data)[0]

    print("\n-----------------------------")
    print(f"Temperature: {Temperature} C")
    print(f"Sunlight: {Sunlight} hrs")
    print(f"Humidity: {Humidity}")
    print(f"Dust Level: {DustLevel}")
    print(f"Predicted Power: {predicted_Powergenerate:.2f}")

    # Performance status
    if predicted_Powergenerate < 200:
        print("Critical: Very Low Power")
    elif predicted_Powergenerate < 400:
        print("Moderate Performance")
    else:
        print("Good Performance")

    # Live graph update
    plt.clf()
    plt.scatter(Temperature, predicted_Powergenerate)
    plt.xlabel("Temperature")
    plt.ylabel("Power")
    plt.title("Live Solar Monitoring")

    plt.pause(1)
    time.sleep(2)

plt.ioff()
plt.show()