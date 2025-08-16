# 🩺 Skin Disease Detection using CNN

## 📌 Overview
This project leverages **Convolutional Neural Networks (CNNs)** to detect and classify common skin diseases from images.  
The model provides an **initial diagnostic aid** for dermatology by identifying the type of skin condition, helping patients and healthcare professionals with early detection.  

## 🎯 Objectives
- Build a CNN-based deep learning model to classify skin diseases.  
- Achieve high accuracy and reliable predictions using real-world datasets.  
- Provide an easy-to-use application (web/app) for uploading skin images and receiving predictions.  

## 🧪 Detected Diseases
The model currently detects the following conditions:
1. **Enfeksiyonel (Infectious)**
2. **Ekzama (Eczema)**
3. **Akne (Acne)**
4. **Pigment Disorders**
5. **Benign Tumors**
6. **Malignant Tumors**

## ⚙️ Tools & Technologies
- **Programming & ML:** Python, TensorFlow, Keras  
- **Data Handling:** NumPy, Pandas  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Flask / Django (for web app), Streamlit (optional)  

## 📂 Project Workflow
1. **Data Preprocessing** – Image resizing, normalization, and augmentation.  
2. **Model Building** – CNN/VGG-19 architecture for feature extraction & classification.  
3. **Training & Validation** – Achieved ~87% accuracy on test dataset.  
4. **Prediction** – Upload an image and receive disease classification.  

## 🚀 Results
- Model achieved **87% accuracy** on the test dataset.  
- Provides **real-time prediction** of skin diseases with a simple user interface.  

## 🏆 Highlights
- Selected as a **major academic project** showcasing the application of AI in healthcare.  
- Demonstrates potential for **early screening and dermatological support tools**.  

## 📌 Future Improvements
- Improve dataset diversity for better generalization.  
- Integrate with **mobile applications** for wider accessibility.  
- Add explainability features (Grad-CAM, Heatmaps) for **transparent AI predictions**.  

## 📎 How to Run
    ```bash
    # Clone the repository
    git clone https://github.com/rajesh147r/Skin_Disease_Detection.git

# Navigate to the project directory
    ```bash
    cd Skin_Disease_Detection

# Install dependencies
    ```bash
    pip install -r requirements.txt
# Run the application
```bash
python app.py
