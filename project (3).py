import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the dataset
df = pd.read_csv("Crime_Incidents_in_2024.csv") 
#objective 1 :
top_crimes = df['OFFENSE'].value_counts().head(5)
print("Top 5 Most Frequent Crime Types:")
print(top_crimes)

#objective 2:
df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'])
df['Month'] = df['REPORT_DAT'].dt.month
monthly_crimes = df.groupby('Month').size()
print("Number of Crimes by Month:")
print(monthly_crimes)

#objective 3:
top_areas = df['NEIGHBORHOOD_CLUSTER'].value_counts().head(5)
print("Top 5 Neighborhood Clusters by Crime Count:")
print(top_areas)

#objective 4:

df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'], errors='coerce')
df['DayOfWeek'] = df['REPORT_DAT'].dt.day_name()
day_crime_counts = df['DayOfWeek'].value_counts()
print("Crime Counts by Day of the Week:")
print(day_crime_counts)
#objective 5:
# Normalize column names to avoid casing/whitespace issues
df.columns = df.columns.str.strip().str.upper()

# Print all column names to verify
print("Available columns:", df.columns.tolist())

# Check if 'ARREST' column exists and print value counts
if 'ARREST' in df.columns:
    arrest_counts = df['ARREST'].value_counts()
    print("Arrest vs Non-Arrest Counts:")
    print(arrest_counts)
else:
    print("The column 'ARREST' was not found. Please check column names above.")

'''# Convert date and clean columns
df.columns = df.columns.str.strip().str.upper()
df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'], errors='coerce')

# Create useful time columns
df['DAY_OF_WEEK'] = df['REPORT_DAT'].dt.day_name()
df['HOUR'] = df['REPORT_DAT'].dt.hour

# --- 1. BAR PLOT: Crimes by day of the week ---
plt.figure(figsize=(8, 5))
df['DAY_OF_WEEK'].value_counts().loc[
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
].plot(kind='bar', color='skyblue')
plt.title('Crime Counts by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()

# --- 2. HISTOGRAM: Crimes by hour ---
plt.figure(figsize=(8, 5))
df['HOUR'].dropna().plot(kind='hist', bins=24, rwidth=0.8, color='orange')
plt.title('Crime Incidents by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Frequency')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# --- 3. BOXPLOT: Distribution of crime incidents per day ---
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='DAY_OF_WEEK', y='HOUR', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title('Boxplot of Crime Hours by Day')
plt.ylabel('Hour of Day')
plt.xlabel('Day of Week')
plt.tight_layout()
plt.show()



# --- 4. PIE CHART: Top 5 Crime Types ---
if 'OFFENSE' in df.columns:
    top5_crimes = df['OFFENSE'].value_counts().head(5)
    plt.figure(figsize=(6, 6))
    plt.pie(top5_crimes, labels=top5_crimes.index, autopct='%1.1f%%', startangle=140)
    plt.title('Top 5 Crime Types')
    plt.tight_layout()
    plt.show()
else:
    print("Column 'OFFENSE' not found. Pie chart skipped.")
'''
