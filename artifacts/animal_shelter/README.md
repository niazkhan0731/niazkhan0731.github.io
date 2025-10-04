# 🐾 Animal Shelter CRUD and Dashboard  
**CS-499 Capstone – Milestone Four (Database Enhancement)**  
Author: **Niaz Khan**  
Date: **October 2025**

---

## 📘 Project Overview
This project is an enhanced version of my Animal Shelter CRUD and Dashboard, originally developed for CS-340: Client/Server Development and later expanded for the CS-499 Computer Science Capstone. The system connects to a MongoDB database containing animal shelter records from the Austin Animal Center dataset. It provides full CRUD (Create, Read, Update, Delete) functionality through a Python module (animal_shelter.py) and visualizes data interactively in a Dash dashboard (ProjectTwoDashboard.ipynb).

---

## 🧱 Technologies Used
- Python 3.9+
- MongoDB (local instance)
- PyMongo
- Dash / Plotly
- Dash-Leaflet (for maps)
- Pandas
- Jupyter Notebook

---

## ⚙️ How to Run Locally
1. Clone or download this repository.  
2. Open Terminal and navigate to the folder:  
   cd ~/Desktop/"Animal Shelter - Artifact 3"
3. Create and activate a virtual environment:  
   python3 -m venv venv  
   source venv/bin/activate
4. Install dependencies:  
   pip install pymongo pandas dash dash-leaflet jupyter-dash plotly
5. Start MongoDB (must be running locally on port 27017).  
6. Launch Jupyter Notebook:  
   jupyter notebook
7. Open ProjectTwoDashboard.ipynb and select Run All.  
   The app will appear inline or at http://127.0.0.1:8051/

---

## 🧩 Project Structure
.
├── animal_shelter.py          # CRUD class with validation, advanced filters, aggregation  
├── ProjectTwoDashboard.ipynb  # Dash app with DataTable, chart, and map  
├── aac_shelter_outcomes.csv   # Dataset for seeding MongoDB  
├── Grazioso Salvare Logo.png  # Branding asset  
└── README.md                  # Documentation (this file)

---

## 🚀 Enhancements (CS-499 Milestone Four)
This milestone focused on demonstrating database management expertise and improving data access, flexibility, and performance.  

### In animal_shelter.py
- Input Validation & Field Whitelisting – Ensures only valid fields are inserted or updated; prevents malformed data.  
- Advanced Filtering (read_advanced) – Supports multi-criteria queries (outcome type, age range, sex, partial breed name).  
- Aggregation Function (aggregate_adoption_stats) – Groups and counts animals by type or outcome for analytical charts.  
- Index Creation – Added indexes on key fields (animal type, outcome, sex, age, breed) to improve query speed.  
- Local MongoDB Configuration – Modified connection string to work with a local MongoDB instance rather than Apporto.  

### In ProjectTwoDashboard.ipynb
- Integrated new filtering and aggregation methods into the interactive dashboard.  
- Added dropdowns, range sliders, and breed text filters for dynamic data queries.  
- Improved table rendering and map interactivity using Dash-Leaflet.  
- Resolved Dash version compatibility by pinning stable versions (dash==2.11.1, jupyter-dash==0.4.2).  

---

## 🧠 Learning Reflection
This enhancement strengthened my understanding of database design, data validation, and backend–frontend integration. Migrating from a remote MongoDB instance to a local configuration improved deployment control, while adding advanced filters and aggregations enhanced the user’s ability to analyze shelter data interactively. Version control through GitHub ensured the project’s reproducibility and professional presentation in my ePortfolio.

---

## 🖼 Evidence of Enhancement
Below are example screenshots demonstrating the working dashboard:  

Figure 1. DataTable filtered by outcome type and breed  
Figure 2. Map and bar chart visualization of animal type distribution  

(Screenshots are included in the Milestone 4 Narrative Word document.)

---

## 📦 Submission Notes
This repository corresponds to Artifact 3 (Database Enhancement) for my CS-499 Capstone ePortfolio. All project files were verified to run locally with a functional dashboard connected to a live MongoDB database.

---

© 2025 Niaz Khan  
Southern New Hampshire University – Computer Science Capstone Project
