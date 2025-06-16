# Space Race Analysis
This project analyzes and visualizes global space missions data to understand trends how different countries, organisations, and technologies have contributed to the space race over time.

## Dataset
- File: space_missions.csv
- Location: data/space_missions.csv
- Contains: Organisation, Location, Date, Rocket Status, Mission Status

## Visualizations
- Launches per Year (Line Chart)
- Launches by Countries (Bar Chart)
- Launches by Organisations (Bar Chart)
- Mission Status: Success vs Failure (Stacked Bar Chart)
- Rocket Status: Active vs Retired (Pie Chart)

## Power BI Dashboard
A separate interactive dashboard built in Power BI showcases different angles of the space missions dataset.
1. Slicers Included:
 - Organisation (Dropdown)
 - Year, Mission Status (Dropdown)  
 - Year (Sliding Range)

2. Visuals in Dashboard:
- KPI Cards: Mission Performance Overview
  - Active/Retired Rockets  
  - Mission Success Rate   
- Missions over the Years (Line Chart)
- Complete space mission data table with slicer filtering (Table)
- Mission Outcomes by Organisation (Horizontal Bar Chart) 
- Top 10 Launch Locations (Clustered Bar Chart) 
- Rocket Status Distribution (Stacked Bar Chart)
- Mission Outcome Distribution (Donut Pie Chart)  
- Global Launch Locations (Map Visual)
  
## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- VS Code
- Power BI

## How to Run
1. Install required libraries:
   pip install pandas matplotlib seaborn
2. Run the Python script
   python space_race.py

## Output
All charts are automatically saved in the `visuals/` folder.
Open the visuals/ folder to view the charts and snapshot of PowerBI Dashboard!
Raw PowerBI Dashboard file (.pbix) and Python analysis notebook are both included in this repository.

