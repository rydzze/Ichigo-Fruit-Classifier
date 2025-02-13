# 🍓 Ichigo: Intelligent Multi-Fruit Classification and Quality Analysis System  

## 📌 Introduction

Traditional fruit classification methods are **labor-intensive and error-prone**. **Ichigo** is an **AI-driven system** that utilizes deep learning models like **CNN, ResNet-50, and VGG-16** to classify fruits as **fresh or rotten**. By integrating machine learning with advanced image processing, **Ichigo** enhances food quality control, reduces waste, and optimizes supply chains. Designed to be **scalable and accessible**, it serves **small farms and large food industries** alike.  

## ❗ Problem Statements  

Despite advances in **computer vision and AI**, challenges persist in fruit classification:  

🔸 **Manual inspection is prone to inconsistencies** – Human judgment can be subjective, leading to quality control issues.  
🔸 **Limited datasets hinder classification accuracy** – AI models struggle with underrepresented fruit types.  
🔸 **Scalability for real-time processing** – Many systems fail to handle large-scale, high-speed operations efficiently. 

## 🎯 Objectives  

The **Ichigo** system aims to:

✅ **Enhance classification accuracy** using deep learning.  
✅ **Enable real-time quality assessment** for efficient sorting.  
✅ **Ensure scalability** for farms, supermarkets, and industries.   

## 🔥 System Features  

🚀 **Deep Learning-Based Classification** – Uses **CNN, ResNet-50, and VGG-16**.  
🖥️ **Web-Based Interface** – Built with **Flask, HTML, CSS, and JavaScript**.  
📊 **Data Preprocessing Techniques** – Image **enhancement, sharpening, and edge detection**.  
🔍 **Real-Time Object Detection** – Segmentation and bounding box.  

## 📊 Model Performance  

### 📌 Public Dataset Performance (Without Preprocessing)  

| Model   | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |  
|---------|-------------|-------------|------------|-------------|  
| **CNN** | 72.50      | 74.50       | 72.75      | 70.84       |  
| **ResNet50** | **98.75** | **98.76** | **98.71** | **98.72** |  
| **VGG16** | 97.03 | 97.08 | 96.92 | 96.96 |  

### 📌 Public Dataset Performance (With Preprocessing)  

| Model   | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |  
|---------|-------------|-------------|------------|-------------|  
| **CNN** | 72.81      | 73.01       | 72.70      | 71.88       |  
| **ResNet50** | **99.22** | **99.21** | **99.20** | **99.20** |  
| **VGG16** | 97.81 | 97.69 | 97.68 | 97.65 |  

#### 🔗 Public Dataset Used

> Sultana, Nusrat; Jahan, Musfika; Uddin, Mohammad Shorif (2022), “Fresh and Rotten Fruits Dataset for Machine-Based Evaluation of Fruit Quality”, Mendeley Data, V1, doi: [10.17632/bdd69gyhv8.1](https://doi.org/10.17632/bdd69gyhv8.1)

### 📌 Self-Collected Dataset Performance (Without Preprocessing)  

| Model   | Accuracy 1 (%) | Accuracy 2 (%) | Average (%) |  
|---------|--------------|--------------|------------|  
| **CNN** | 26.00       | 24.27       | 25.14      |  
| **ResNet50** | **71.00** | **78.64** | **74.82** |  
| **VGG16** | 52.50 | 55.83 | 54.17 |  

### 📌 Self-Collected Dataset Performance (With Preprocessing)  

| Model   | Accuracy 1 (%) | Accuracy 2 (%) | Average (%) |  
|---------|--------------|--------------|------------|  
| **CNN** | 18.00       | 12.62       | 15.31      |  
| **ResNet50** | **53.00** | **55.83** | **54.42** |  
| **VGG16** | 47.50 | 58.25 | 52.88 |  

#### 🔗 Self-Collected Dataset Used (Dataset 1)

> Refer to the end of this README.

## 🛠️ Installation Guide  

### 📌 Prerequisites  

Ensure you have the following installed:  
- 🐍 **Python 3.9+**  

### ⚙️ Steps to Install and Run  

1️⃣ **Clone the repository** 🖥️  

```bash  
git clone https://github.com/rydzze/Ichigo-Fruit-Classifier.git
cd Ichigo  
```

2️⃣ **Install dependencies** 📦  

```bash  
pip install -r requirements.txt  
```  

3️⃣ **Run the application**  

```bash  
python run.py  
```  

4️⃣ **Access the system:** 🌍  

```  
http://localhost:686  
```  

## 📸 Screenshots of User Interface

![image](https://github.com/user-attachments/assets/aff93e40-9f9b-4371-a68b-cf41996380c1)

![image](https://github.com/user-attachments/assets/b8ee89c4-a8fe-41fb-9c69-4137f4cbf459)

![image](https://github.com/user-attachments/assets/598c28ba-8d99-46b4-bad8-eec560420235)

## 🏆 **Contribution**

We would like to express our gratitude to the following individuals for their contributions to Ichigo:

- [Muhammad Ariff Ridzlan](https://github.com/rydzze)
- [Muhammad Hafiz](https://github.com/IbnAsmuni)
- [Siti Nur Aisyah](https://github.com/ayesharizani)
- [Nurul Hurul Aini](https://github.com/ainiharis)

Your dedication and expertise have been instrumental in the development of this system. 🚀💡

## 💻 Google Drive Link (Alternative)

> [Ichigo](https://drive.google.com/drive/folders/1AcXk4rswDTDdUeTO1zVb6PG-ohWoQWai?usp=sharing), including the self-collected dataset and .h5 model files.
