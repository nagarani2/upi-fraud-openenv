# 💳 UPI Fraud Detection OpenEnv

## 📌 Project Overview
This project simulates a real-world UPI fraud detection system using the OpenEnv API.  
An AI agent interacts with the environment to classify transactions as **fraud** or **safe**.

---

## ⚙️ OpenEnv API Implementation

The environment follows standard OpenEnv functions:

- `reset()` → Initializes a new transaction
- `state()` → Returns current transaction details
- `step(action)` → Evaluates agent decision and returns reward

---

## 🧠 Fraud Detection Logic

A transaction is marked as **fraud** if 2 or more of the following conditions are true:

- 💰 Amount greater than 30,000  
- 🌙 Transaction time is late night (before 5 AM)  
- 🌍 Location is a new city  
- 📱 Device is unknown  

Otherwise, it is considered **safe**.

---

## 🎯 Reward System

- ✅ Correct prediction → +10  
- ❌ Wrong prediction → -10  
---

## ▶️ How to Run

1. Open terminal in project folder  
2. Run the following command:
3. Enter action:

---

## 🚀 Features

- Real-world inspired fraud detection system  
- OpenEnv API compatible  
- Interactive terminal-based simulation  
- Extendable for AI training  

---

## 📌 Future Improvements

- Add machine learning model  
- Increase dataset size  
- Deploy full web app  

---

## 👩‍💻 Author
Kondapuram  Nagarani
---

## 📂 Project Structure
