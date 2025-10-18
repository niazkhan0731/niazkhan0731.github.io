# 🐾 Animal Shelter CRUD and Dashboard  
**CS-499 Capstone – Artifact 3 (Database Enhancement)**  
**Author:** Niaz Khan  
**Date:** October 2025

---

## 📘 Project Overview  
This project is an enhanced version of my Animal Shelter CRUD and Dashboard, originally developed during **CS-340: Client/Server Development** and expanded for the **CS-499 Computer Science Capstone**. It connects to a **MongoDB** database containing Austin Animal Center intake and outcome data.

It includes:
- A Python module (`animal_shelter.py`) with full **CRUD operations**
- A Dash dashboard (`ProjectTwoDashboard.ipynb`) with **interactive data analysis**, charts, and maps

This artifact demonstrates my ability to manage real datasets, enforce data validation, and design analytical tools that support decision-making.

---

## 🎯 Why I Selected This Artifact  
I chose this artifact because it represents my growth in **database systems and data visualization**. It shows how I evolved beyond simple query execution to building a complete database interface with secure input handling, advanced filtering, aggregation, and a user-focused dashboard—skills that align with professional roles in data engineering and full-stack development.

---

## 🧱 Technologies Used  
- Python 3.9+  
- MongoDB (Local Instance)  
- PyMongo  
- Dash / Plotly  
- Dash-Leaflet  
- Pandas  
- Jupyter Notebook  

---

## ⚙️ How to Run Locally  

1️⃣ Navigate to the project directory  
2️⃣ Create and activate a virtual environment  
3️⃣ Install dependencies using `pip`  
4️⃣ Ensure MongoDB is running locally on port `27017`  
5️⃣ Open `ProjectTwoDashboard.ipynb` in Jupyter Notebook and **Run All**

The dashboard will load inline or at:  
`http://127.0.0.1:8051/`

---

## 🚀 Key Enhancements (CS-499 Database Focus)

### 🔧 Backend Enhancements – `animal_shelter.py`
- Added **input validation and field whitelisting** to protect database integrity  
- Implemented **advanced filtering (`read_advanced`)** for breed, sex, age, and outcome-based querying  
- Developed **aggregation functions** for adoption/outcome analytics  
- Optimized database using **indexes** for performance  
- Migrated from hosted to **secure local MongoDB setup**

### 📊 Dashboard Enhancements – `ProjectTwoDashboard.ipynb`
- Added **interactive UI controls** (dropdowns, sliders, search filters)  
- Integrated **live charts and metrics** using aggregation outputs  
- Implemented **geolocation mapping** using Dash-Leaflet  
- Standardized environment using stable Dash and compatibility fixes

---

## 🧠 Reflection and Growth  
This enhancement deepened my experience with **real-world database challenges**, including validation, performance tuning, and integration with front-end visualization tools. Migrating the project to a local instance required solving connection, environment, and data-loading issues.

Transforming static records into an interactive dashboard reinforced how backend systems can power meaningful insights—an essential capability in enterprise and analytics roles.

---

## 🎓 Course Outcomes Demonstrated  

- **CO2 – Communication:** Built a visual dashboard that communicates data insights clearly  
- **CO3 – Algorithmic/Data Methods:** Applied advanced filtering and aggregation logic in MongoDB  
- **CO4 – Tools & Technologies:** Used PyMongo, Dash, and data pipelines to create a full solution  
- **CO5 – Security Mindset:** Implemented safe query practices and controlled data validation

---

## 📦 Capstone Submission Notes  
This repository represents **Artifact 3: Database Enhancement** for my CS-499 Capstone. It demonstrates my ability to build secure, scalable, and data-driven applications using real-world datasets.

---

© 2025 **Niaz Khan**  
Southern New Hampshire University – Computer Science Capstone
