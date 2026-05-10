# 🔥 1️⃣ Apply Function (apply())

# 👉 apply() = प्रत्येक row/column मा function लगाउने method

# 📊 Example
# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Ram", "Hari", "Sita"],
#     "marks": [80, 90, 85]
# })
# 🔥 Marks pass/fail बनाउने
# df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
# print(df)
# 🧠 Meaning

# 👉 80 भन्दा माथि → Pass
# 👉 तल → Fail