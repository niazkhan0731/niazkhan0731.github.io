# 📅 Event Tracker App  
**CS-499 Capstone – Milestone Two (Software Engineering & Design Enhancement)**  
Author: **Niaz Khan**  
Date: **August 2025**

---

## 📘 Project Overview
This project is an enhanced version of my **Event Tracker Android Application**, originally developed for **CS-360: Mobile Architecture and Programming** and later improved for the **CS-499 Computer Science Capstone**.  

The app allows users to **create, view, edit, and delete personal events** with details such as event name, date, time, and description. It also features **user login and registration**, persistent **SQLite data storage**, and **SMS-based reminders** for upcoming events.  

The goal of this enhancement was to strengthen the app’s software design, modularity, and data handling while ensuring an improved user experience and secure data persistence.

---

## 🧱 Technologies Used
- **Java (Android Studio)**
- **SQLite Database**
- **Android SDK**
- **XML for UI Layouts**
- **Android Manifest Permissions (SMS, Storage)**
- **MVVM Design Pattern**

---

## ⚙️ How to Run Locally
1. Open **Android Studio** (Arctic Fox or newer).  
2. Select **File → Open** and choose the folder containing the Event Tracker project.  
3. Let Gradle sync and build the project.  
4. Run the project on an emulator or connected Android device (API Level 30+ recommended).  
5. On first launch, register a new user and log in to access the event dashboard.  
6. Add, edit, and delete events using the event grid screen.  

---

## 🧩 Project Structure
.
├── MainActivity.java              # Handles login and registration logic  
├── EventDashboardActivity.java    # Displays event grid and CRUD operations  
├── AddEventActivity.java          # UI for adding and editing events  
├── DatabaseHelper.java            # SQLite helper class for persistent storage  
├── SMSHandler.java                # Handles SMS notification permissions and sending  
├── res/layout                     # XML layout files (UI)  
├── AndroidManifest.xml            # Permissions and activity declarations  
└── README.md                      # Documentation (this file)

---

## 🚀 Enhancements (CS-499 Milestone Two)
This milestone focused on demonstrating **software engineering and design principles**, emphasizing modularity, maintainability, and user experience.  

### In Java Code
- **Refactored DatabaseHelper Class**  
  Improved schema organization and added helper methods for reusable CRUD operations.  
- **Enhanced Activity Navigation**  
  Simplified transitions between Login, Registration, and Event Dashboard screens.  
- **Improved MVC / MVVM Separation**  
  Divided UI logic from data handling to promote cleaner, modular code.  
- **Input Validation**  
  Added form validation for event creation (empty fields, invalid dates, etc.).  
- **SMS Reminder Logic**  
  Implemented SMS permission checks and integrated Android’s SMSManager API for scheduled notifications.

### In UI Design
- **Visual Hierarchy Improvements**  
  Created a grid-based event display with clearer labels and balanced spacing.  
- **Consistent Color Palette & Typography**  
  Applied Material Design guidelines for a modern look and intuitive experience.  
- **Responsive Layouts**  
  Used constraint layouts and size attributes for adaptability across screen sizes.  

---

## 🧠 Learning Reflection
This enhancement strengthened my ability to apply **object-oriented programming**, **UI/UX principles**, and **software design patterns** to a mobile application.  
Refactoring the code base improved maintainability, and redesigning the interface enhanced usability and accessibility. I learned the importance of balancing functionality with user-centered design, as well as handling runtime permissions securely within Android’s evolving framework.  

I also became more comfortable using **SQLite** for persistent data management and applying the **MVVM architecture**, which aligns with real-world mobile development standards.

---

## 🖼 Evidence of Enhancement
Below are screenshots demonstrating the working app and enhancements:  

Figure 1. Login and registration screens  
Figure 2. Event dashboard showing event grid and CRUD operations  

(Screenshots are included in the Milestone 2 Narrative Word document.)

---

## 📦 Submission Notes
This repository corresponds to **Artifact 2 (Software Engineering & Design Enhancement)** for my **CS-499 Capstone ePortfolio**.  
All project files were verified to compile and run successfully in Android Studio with full CRUD and SMS functionality.

---

© 2025 Niaz Khan  
Southern New Hampshire University – Computer Science Capstone Project
