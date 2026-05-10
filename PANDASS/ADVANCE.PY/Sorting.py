🔥 SORTING in Pandas (FULL DETAILS 🔥)

👉 Sorting = data लाई order मा मिलाउने process

Simple मा:

सानो → ठूलो
ठूलो → सानो
A → Z
Z → A
🧠 Why Sorting Important?

👉 Real world मा:

highest marks खोज्न
top salary
latest sales
ranking system

सबैमा sorting use हुन्छ 🔥

📊 Example Dataset
import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)

print(df)
📤 Output
   name  marks  age
0   Ram     80   20
1  Hari     90   21
2  Sita     85   19
3  Gita     70   22
🔥 1️⃣ Sort by One Column
👉 Ascending (small → big)
df.sort_values(by="marks")
📤 Output
   name  marks
3  Gita     70
0   Ram     80
2  Sita     85
1  Hari     90
🧠 कसरी भयो?

👉 marks ascending order मा arrange भयो:

70<80<85<90

🔥 2️⃣ Descending Sort

👉 ठूलो → सानो

df.sort_values(by="marks", ascending=False)
📤 Output
   name  marks
1  Hari     90
2  Sita     85
0   Ram     80
3  Gita     70
🧠 Meaning

👉 highest marks first 🔥


⚡ Important Parameter

| Parameter       | Meaning               |
| --------------- | --------------------- |
| by              | कुन column sort गर्ने |
| ascending=True  | small → big           |
| ascending=False | big → small           |


🔥 3️⃣ Multi-column Sorting

👉 multiple columns अनुसार sort

df.sort_values(by=["age", "marks"])
🧠 Meaning

👉 first:

age अनुसार sort

👉 same age भए:

marks अनुसार sort
🔥 4️⃣ Sort by Name (Alphabetical)
df.sort_values(by="name")
📤 Output
Gita
Hari
Ram
Sita
🧠 Meaning

👉 A → Z sorting

🔥 5️⃣ Permanent Sorting

👉 default मा original df change हुँदैन ❌

❌ Temporary
df.sort_values(by="marks")
✅ Permanent
df.sort_values(by="marks", inplace=True)
🧠 Meaning

👉 अब original DataFrame पनि sorted हुन्छ

🔥 6️⃣ Sort Index
df.sort_index()
🧠 Meaning

👉 index number अनुसार sort

📊 Real Life Example

👉 School:

top students rank

👉 Company:

highest salary employees

👉 Shop:

top selling products

⚡ Most Important Sorting Methods


| Method          | Use         |
| --------------- | ----------- |
| sort_values()   | column sort |
| ascending=False | descending  |
| sort_index()    | index sort  |


🧪 Practice 🔥
Q1

Sort marks ascending

Q2

Sort marks descending

Q3

Sort by age and marks

Q4

Sort names alphabetically