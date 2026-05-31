# DAY 2 — Scikit-learn Setup + Dataset Basics

# Learning Objectives

# आजको दिनमा तिमीले:

# Scikit-learn को setup बुझ्ने

# Dataset के हो बुझ्ने

# Features र Target राम्रोसँग बुझ्ने

# CSV file के हो सिक्ने


# Pandas प्रयोग गरेर dataset load गर्न सिक्ने

# Dataset inspect गर्न सिक्ने

# 1. Dataset भनेको के हो?

# Machine Learning मा Dataset भनेको data को collection हो।

# उदाहरण:

# | Study Hours | Attendance | Marks |
# | ----------- | ---------- | ----- |
# | 2           | 80         | 35    |
# | 4           | 90         | 60    |
# | 6           | 95         | 85    |


# यो एउटा dataset हो।

# 2. Features र Target



# Machine Learning मा data लाई दुई भागमा विभाजन गरिन्छ।

# Features (X)

# Input data

# उदाहरण:

# Study Hours
# Attendance

# यी model ले हेर्ने data हुन्।

# Target (y)

# Output data

# उदाहरण:

# Marks

# Model ले predict गर्ने value।

# Example


# | Study Hours | Attendance | Marks |
# | ----------- | ---------- | ----- |
# | 2           | 80         | 35    |
# | 4           | 90         | 60    |
# | 6           | 95         | 85    |


# Features:

# X = [
#     [2, 80],
#     [4, 90],
#     [6, 95]
# ]
# Target:

# y = [35, 60, 85]


3. CSV File के हो?

CSV = Comma Separated Values

Data store गर्ने सबैभन्दा common format हो।

Example:

students.csv

StudyHours,Attendance,Marks
2,80,35
4,90,60
6,95,85
4. Pandas Installation

Terminal मा:

pip install pandas

Check:

import pandas as pd

print(pd.__version__)

5. Dataset Load गर्ने

students.csv file:

StudyHours,Attendance,Marks
2,80,35
4,90,60
6,95,85
8,98,95

Python code:

import pandas as pd

data = pd.read_csv("students.csv")

print(data)
Line by Line Explanation
Line 1
import pandas as pd

Pandas library import गर्यो।

Line 2
data = pd.read_csv("students.csv")

CSV file read गर्यो।

Line 3
print(data)

Dataset display गर्यो।

6. Head Function

Dataset को माथिका rows हेर्न।

print(data.head())

Specific rows:

print(data.head(2))

Output:

   StudyHours  Attendance  Marks
0           2          80     35
1           4          90     60
7. Tail Function

Dataset को अन्तिम rows हेर्न।

print(data.tail())

Specific rows:

print(data.tail(2))
8. Dataset Shape

Rows र Columns संख्या हेर्न।

print(data.shape)

Output:

(4, 3)

Meaning:

4 rows
3 columns
9. Column Names
print(data.columns)

Output:

Index(['StudyHours', 'Attendance', 'Marks'], dtype='object')
10. Dataset Information
print(data.info())

Output Example:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries
Data columns (total 3 columns)

यसले dataset को structure देखाउँछ।

11. Statistical Summary
print(data.describe())