# 🧠 Image Alteration Detection: Deep Learning & Web App

This project investigates the detection of **GAN-generated (fake)** vs **real images** using deep learning techniques. We implemented multiple models including a **Custom CNN**, **ResNet50**, and **MobileNetV2**, and developed a real-time web interface using **Django** that leverages the MobileNetV2 model for predictions.

---

## 📦 Repository Structure

```bash
Image-Alteration-Detection/
├── notebooks/
│   ├── pretrained_cnn_MobileNetV2.ipynb
│   ├── pretrained_cnn_ResNet50.ipynb
│   └── custom_cnn.ipynb
│
├── webapp/
│   ├── manage.py
│   ├── detection/
│   ├── main/
│   │   ├── views.py
│   │   └── templates/
│   └── model/
│       └── mobilenetv2_model.h5
│
├── pre-trained weights/
│
├── dataset/
│   ├── train/
│   │   ├── real/
│   │   └── fake/
│   └── test_mixed/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Deep Learning Models

We trained and compared the following models:

### 1. 🧱 Custom CNN
- Built from scratch with Conv2D, MaxPooling, Dense layers.
- Served as a baseline model.
- Trained with basic data augmentation.

### 2. 🏋️ ResNet50 (Pretrained)
- Initialized with ImageNet weights.
- Fine-tuned for binary classification (real vs fake).
- Achieved high accuracy and generalization.

### 3. 🚀 MobileNetV2 (Pretrained)
- Lightweight and optimized for speed.
- Selected for **deployment** in the web application.
- Trained with frozen base layers and custom classification head.

> 📊 **Detailed metrics and plots are available in each notebook inside the `/notebooks` folder.**

---

## 🖼️ Dataset Description

The dataset is structured as:

```
dataset/
├── train/
│   ├── real/
│   └── fake/
└── test_mixed/
```

- `train/`: Used for model training (contains labeled `real` and `fake` folders).
- `test_mixed/`: Used for evaluation and predictions (unlabeled mixed set).

## 📌 Note

For higher accuracy, you may consider replacing the dataset with [140k-real-and-fake-faces dataset on Kaggle](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces).
---

## 🌐 Django Web App

A simple Django web interface built to upload an image and classify it using the trained **MobileNetV2** model.

### ✅ Features:
- Drag-and-drop and file upload support.
- Displays uploaded image preview and classification result.
- Real-time inference using the trained MobileNetV2.

### 🔧 Run the Web App Locally

```bash
# Clone repo
git clone https://github.com/esmatullah-adel/Image-Alteration-Detection.git
cd Image-Alteration-Detection/webapp/

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r ../requirements.txt

# Run Django server
python manage.py runserver
```

> Visit `http://127.0.0.1:8000/` to use the app.

---

## 📊 Model Comparison Summary

| Model        | Accuracy | Notes                      |
|--------------|----------|----------------------------|
| Custom CNN   | ~85%     | Simple model, fast to train|
| ResNet50     | ~95%     | Very accurate, heavy model |
| MobileNetV2  | ~94%     | Lightweight, web-deployed  |

---

## 📚 Dependencies

> All required libraries are listed in `requirements.txt`.