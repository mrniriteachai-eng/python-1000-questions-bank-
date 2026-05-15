import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data (price history + weather + season)
df = pd.read_csv("veg_prices_nepal.csv")

# Features
features = ["day_of_year", "season_code", "rain_flag", "demand_score", "price_lag1"]
X = df[features]
y = df["price_trend"]  # 0=down,1=stable,2=up

model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

# Predict for tomorrow
new_input = [[250, 2, 1, 4, 85]]  # day 250, rainy season, rain today, high demand, yesterday price
prediction = model.predict(new_input)