# 🚦 Smart Traffic Control System  
**AI-Powered Real-Time Traffic Monitoring & Dynamic Signal Optimization**

A smart, AI-assisted system designed to analyze traffic flow in real time using live or recorded video feeds. The system provides an interactive control dashboard that displays traffic density, vehicle types, flow trends, and estimated waiting times — enabling smarter decision-making for traffic operators and improving intersection efficiency.

---

## 📌 Project Overview  
This project simulates an intelligent traffic monitoring platform capable of:

- Counting vehicles in each direction  
- Estimating traffic density and congestion levels  
- Measuring average waiting times  
- Analyzing vehicle type distribution (cars, trucks, buses)  
- Displaying real-time charts and live video  
- Supporting navigation between regions, cities, and intersections  

> Note: Current version uses simulation data. The system is designed for future integration with real AI models such as YOLOv8.

---

## 🎯 System Objectives  
- Reduce traffic congestion at intersections  
- Dynamically optimize green-signal times  
- Provide a live dashboard for traffic control centers  
- Improve decision-making using real-time insights  
- Support emergency and public transport prioritization in future versions  
- Establish a scalable foundation for city-wide traffic intelligence  

---

## 🧠 How the System Works  
The system is designed around four main layers:

1. **Video Input**  
   A live traffic camera or pre-recorded video feed representing a real road segment.

2. **Processing Layer (Python + Streamlit Simulation)**  
   Generates traffic metrics such as vehicle count, flow rate, and congestion status.

3. **Interactive Dashboard Layer**  
   Displays live charts, density metrics, and video playback inside the traffic control view.

4. **Navigation User Interface (Frontend HTML)**  
   Enables selecting regions, cities, and intersections through a clean visual interface.

These components work together to create an end-to-end intelligent traffic monitoring solution.

---

## 📂 Project Structure (Explained Simply)

- **app.py**  
  Backend dashboard built with Streamlit, generating live traffic simulation data.

- **demo.mp4**  
  Video displayed inside the Streamlit dashboard.

- **output_final.mp4**  
  Video displayed inside the frontend dashboard (HTML).

- **requirements.txt**  
  Specifies Python dependencies.

- **deploy.yml**  
  GitHub Actions configuration for deploying the frontend via GitHub Pages.

- **index.html**  
  Landing page for the system.

- **regions.html**  
  Region selection interface.

- **cities.html**  
  City selection interface.

- **dashboard.html**  
  Main traffic dashboard with charts and video preview.

---

## 🌐 Frontend Interface Overview

### 1) **index.html**
Landing page containing the project title and “Start Monitoring” button.

### 2) **regions.html**
Allows selecting a geographic region.  
(Only Riyadh is active in this version.)

### 3) **cities.html**
Displays Riyadh’s cities and governorates.  
(Riyadh City is active and leads to the dashboard.)

### 4) **dashboard.html**
The main data dashboard featuring:
- Live video  
- Vehicle type distribution chart  
- Flow rate chart (last hour)  
- Directional density bar chart  
- Auto-updated metrics  
- Buttons to switch intersections or return to city list  

---

## 📊 Backend Overview (Streamlit — app.py)

The backend performs:
- Playback of a live/demo video  
- Randomized vehicle count generation  
- Randomized waiting-time simulation  
- Congestion classification  
- Automatic chart updates  

Example functionalities inside `app.py`:
- `st.video()` to display the traffic feed  
- `st.metric()` for dynamic statistics  
- `st.line_chart()` for flow simulation  

This serves as a prototype for a future AI-powered real implementation.

---

## 🛠️ Technologies Used  
| Technology | Purpose |
|-----------|---------|
| Python | Backend logic and data simulation |
| Streamlit | Real-time dashboard rendering |
| HTML / CSS | User interface components |
| JavaScript + Chart.js | Interactive charts and animations |
| GitHub Pages | Hosting frontend pages |
| GitHub Actions | Automated deployment (CI/CD) |
| YOLOv8 (Future) | Vehicle detection & classification |

---

## ▶️ Running the Project Locally

### 1) Install dependencies:
