import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the data
df = pd.read_csv("data/space_missions.csv")

#Converting 'Date' column to proper datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

#Extracting year from date
df['Year'] = df['Date'].dt.year

#Launches per year (Line Chart)
launches_per_year = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.lineplot(x=launches_per_year.index, y=launches_per_year.values, marker="o")
plt.title("Launches Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Launches")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/launches_per_year.png")
plt.close()

#Launches by countries (Bar Chart)
df['Country'] = df['Location'].apply(lambda x: x.split(',')[-1].strip())
country_counts = df['Country'].value_counts()
plt.figure(figsize=(10,5))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title("Launches by Country")
plt.xticks(rotation=45)
plt.ylabel("Number of Launches")
plt.tight_layout()
plt.savefig("visuals/launches_by_country.png")
plt.close()

#Launches by organisations (Bar Chart)
org_counts = df['Organisation'].value_counts()
plt.figure(figsize=(10,5))
sns.barplot(x=org_counts.index, y=org_counts.values)
plt.title("Launches by Organisation")
plt.xticks(rotation=90)
plt.ylabel("Number of Launches")
plt.tight_layout()
plt.savefig("visuals/launches_by_organisation.png")
plt.close()

#Mission status (Stacked Bar Chart)
mission_status = df['Mission Status'].value_counts()
plt.figure(figsize=(6,6))
sns.barplot(x=mission_status.index, y=mission_status.values, palette="muted")
plt.title("Mission Status: Success vs Failure")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("visuals/mission_status.png")
plt.close()

#Rocket status (Pie Chart)
rocket_status = df['Rocket Status'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(rocket_status.values, labels=rocket_status.index, autopct='%1.1f%%', startangle=90)
plt.title("Rocket Status: Active vs Retired")
plt.tight_layout()
plt.savefig("visuals/rocket_status_pie.png")
plt.close()