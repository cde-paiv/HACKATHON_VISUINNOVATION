# Drone Control System – Hackathon Visuinnovation Project

## Overview
A comprehensive **autonomous drone control and monitoring system** built in Python. Designed for waypoint-based navigation and delivery missions, this system offers automated flight, real-time monitoring, safety validation, weather integration, and detailed logging.

---

## 📌📋 Summary from the experience

The hackathon had the duration of 3 months, from august until final of november, in which we had constant contact with the company to develop an application (frontend and backend) that would make 
the management of a drone between two points in a map.

In order to develop it, we needed to strength our knowledge in:
- **Drone system, flight and components**, 
- **Database management** **(CRUD)**,
- **Validation of technical requirements**,
- **API usage** (connect the versel application to the backend),
- **Embeeded Systems**,
- **Waypoint and locaiton management**,
- **Handling of DTO** sent by the weather API,
- **Log creation**,

Before the delivery, in which we got to test it with the drone, we were making the test through a drone simulator (arducopter) sending the personalized instructions via ardupilot controls, same ones received by the drone 
we were going to use in the final demonstration. 

Objective achieved on the simulator:
- Make the drone fly between multiple points making landings in all of them and returning to home,
- Writing logs of position during the flight,
- Refreshing the database for the management of users, waypoints and drones,
- Safety checks before/during the flyight,


---

## Division of labour

 - Backend -> [Eduardo Vasconcelos]() [Christofer]
 - Frontend ->  []




---

## Core Functionality
- **Autonomous Flight** – Fully automated flight from takeoff to landing
- **Real-Time Monitoring** – Telemetry, battery, and environmental condition tracking
- **Weather Integration** – Live weather data with flight safety assessments
- **Safety Management** – Pre-flight and in-flight parameter checks
- **Mission Management** – Waypoint-based flight planning and execution
- **Dual Logging** – Simple and detailed flight record logs
- **Database Integration** – User and waypoint data managed via Supabase

---

## System Architecture

### 🔧 Core Classes
- `Drone` – Handles telemetry, battery, location, and drone status
- `Mission` – Manages mission planning and execution logic
- `Monitoring` – Performs real-time checks and safety validations
- `Weather` – Integrates weather APIs and evaluates conditions
- `Location` – Handles geographic data and calculations
- `Waypoint` – Manages destinations and coordinates
- `User` – Controls account management and permissions
- `Package` – Tracks delivery package details
- `Route` – Plans the optimal flight path

### 📦 Key Modules
- `main.py` – Application entry point with CLI
- `Log.py` – Logging system for mission data
- `Database.py` – Handles Supabase database operations
- `Ideal_Params.py` – Defines safety parameters

---

## Technologies Used

### 🐍 Python Libraries
- `mavsdk` – Drone communication and control
- `pymavlink` – MAVLink protocol support
- `asyncio` – Async programming for concurrency
- `requests` – Weather API communication
- `supabase` – Cloud database interface
- `python-dotenv` – Environment variable loader

### 📚 Standard Libraries
- `datetime`, `csv`, `math`, `os`, `sys`

### 🌐 External Services
- **OpenWeatherMap API** – Real-time weather updates
- **Supabase** – Cloud DB for users and waypoints
- **MAVLink** – Industry-standard drone communication protocol

---

## Key Features

### ✈️ Flight Control
- Automated takeoff and landing
- Waypoint navigation
- Return-to-launch (RTL)
- Live GPS tracking

### 🛡️ Safety System
- Pre-flight checks
- In-flight parameter monitoring
- Weather analysis
- Battery and altitude limits

### 📊 Monitoring & Logging
- Telemetry data recording
- Dual-mode logging (simple & detailed)
- GPS and mission status tracking

### 🌦️ Weather Integration
- Live data: temperature, humidity, wind, visibility
- Condition-based flight approval

### 🗃️ Database Management
- User & waypoint CRUD operations
- Mission planning and record-keeping

---

## Safety Parameters

### 🌡️ Weather Limits
- **Humidity:** ≤ 80%
- **Wind Speed:** ≤ 10 m/s
- **Visibility:** ≥ 100 m
- **Temperature:** 278K–318K (5°C–45°C)

### 🔋 Battery Requirements
- **Takeoff:** ≥ 80%
- **In-flight:** ≥ 30%
- **Temperature:** 283K–333K (10°C–60°C)

### 🚫 Flight Limitations
- **Max Absolute Altitude:** 4500 m
- **Relative Altitude Range:** 10–120 m
- **Max Base Distance:** 8000 m
- **Max Takeoff Mass:** 29.0 kg

---



## Usage

### Command Line Interface
```bash
# Start a flight mission
python main.py fly [username] [waypoint_name]

# Get current drone data
python main.py data
```

### 🧭 Flight Process
1. **Pre-flight Checks** – Validates weather, battery, and safety limits
2. **Mission Planning** – Loads waypoints and calculates route
3. **Takeoff** – Launch sequence initiated
4. **Navigation** – Autonomous flight to destination
5. **Return** – Drone returns to base
6. **Landing** – Final automated descent

---

## File Structure

### 🗂️ Core System
- `main.py` – CLI entry point
- `Drone.py` – Drone operations and telemetry
- `Mission.py` – Mission logic
- `Monitoring.py` – Safety monitoring

### 🔧 Support Modules
- `Weather.py` – Weather integration
- `Log.py` – Logging system
- `Database.py` – Supabase connection
- `Location.py` – Location and distance calculations

### 🧱 Data Models
- `User.py` – User account logic
- `Waypoint.py` – Waypoint management
- `Package.py` – Package tracking
- `Route.py` – Flight route planner
- `Ideal_Params.py` – Safety configurations

---

## Project Status
A functional autonomous drone system built for delivery and waypoint-based navigation. Includes robust safety checks, live monitoring, logging, and integration with MAVLink-compatible drones. Supports local CSV and Supabase cloud storage.

---

## 🛠️ Installation
```bash
pip install mavsdk pymavlink requests supabase python-dotenv
```

## ⚙️ Configuration
- OpenWeatherMap API key
- Supabase project URL & API key
- MAVLink-compatible drone (default: UDP port `14550`)
