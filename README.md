
# Shine – AI-Powered Makeup Recommendation Website

## 📌 Overview
**Shine** is an intelligent web platform that provides personalized makeup recommendations based on clothing colors and facial images (or selected face shapes) using **AI and image processing**.  
Users can upload a photo of their outfit and a face image (or choose a face shape), and the system will extract the dominant clothing color, then suggest makeup that matches the outfit, skin tone, and preferred makeup style (Natural or Bold).

---

## ✨ Features
- **Accurate clothing color extraction** using a custom AI model.
- **Makeup template selection** via the AMCT algorithm.
- **Realistic makeup application** with the CSD-MT model, preserving facial details.
- **Privacy options**: Upload a real face image or choose a predefined face shape.
- **Style selection**: Natural or Bold, with undertone options (Fair, Medium, Dark).
- **Interactive experience**: View the final result instantly.
- **Feedback and rating system** to collect user opinions.
- **Image privacy**: All uploaded images are deleted immediately after processing.

---

## 🛠 Technologies Used
- **Front-end:** HTML, CSS, JavaScript
- **Back-end:** PHP
- **AI & ML Models:** Python, TensorFlow, Keras
- **Database:** MySQL (phpMyAdmin)
- **Development Tools:** Google Colab, VS Code, XAMPP
- **Version Control:** Git & GitHub

---

## 🎯 AI Models
1. **Custom Outfit Color Extraction Model**  
   
2. **Makeup Transfer Model (CSD-MT)**  
   - Based on the *Content-Style Decoupled Makeup Transfer* algorithm.
   - Source: [CSD-MT GitHub Repository](https://github.com/Snowfallingplum/CSD-MT/tree/main/quick_start)

3. **AMCT (Analyze Makeup Color Template)**  
   - Custom internal algorithm that combines clothing color + skin tone + makeup type to select the best template.

---


## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/Shine.git
cd Shine
```

### 2️⃣ Setup XAMPP
- Ensure **Apache** and **MySQL** are running.
- Place the project folder inside the `htdocs` directory of XAMPP.

### 3️⃣ Import Database
- Open `phpMyAdmin`.
- Create a new database named `shine`.
- Import the `database/feedback.sql` file.

### 4️⃣ AI Model Setup
- Ensure **Python 3.9+** is installed.
- Install required dependencies:
```bash
pip install tensorflow keras flask pillow
```
- Run the AI model server:
```bash
python models/run_model.py
```
(Make sure the port matches the settings in PHP/JS)

### 5️⃣ Run the Website
- Open your browser and navigate to:
```
http://localhost/Shine/index.php
```

---

## 🔒 Privacy & Security
- All uploaded images are deleted immediately after displaying the result.
- No personal data or images are stored on the server.

---

## 👥 Authors
- [Fatima alzhrani]
- [Reham alotibi]
- [lana aljuaid]
- [asma alasmri]
