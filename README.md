# 📰 Fake News Detector
A lightweight Streamlit app that classifies news headlines as real or fake using a PyTorch model.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit)

![Model Accuracy](https://img.shields.io/badge/Accuracy-94%25-brightgreen)

👉 [Try it live - on GokulAIx](https://gokulaix-fake-news-detector.streamlit.app)

Dataset: [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

import kagglehub
path = kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset")

## 5. How It Works / Model Overview

Model type (3-layer feedforward neural network)

Input size, output, activation functions

Preprocessing (MiniLM sentence embedding)

Accuracy: 94%

## 6. App Features
   
Input a headline

Get prediction with confidence %

Color-coded output for real, fake, or unsure(Maybe)

## 7. How to Run Locally

Simple terminal steps:

# First, fork this repository to your own GitHub account

# Then, clone it from your own GitHub account

<pre> <code> ```bash 
  git clone https://github.com/&lt;your-username&gt;/Fake_News_Detector.git 
``` </code> </pre>

cd Fake_News_Detector

pip install -r requirements.txt

streamlit run app.py

## 8. Example Inputs

Show a few real and fake examples (for users and evaluators to test).

✅ Real: "India launches Gaganyaan..."

❌ Fake: "Government replaces Rupee with Bitcoin"


## 9. Project Structure

├── app.py

├── Fake_News_Detection.pth

├── requirements.txt

├── .gitignore

└── README.md

## 10. Contact Info

## Contact Information
- **Name:** P Gokul Sree Chandra  
- **Email:** polavarapugokul@gmail.com  
- **LinkedIn:** [Gokul Sree Chandra](https://www.linkedin.com/in/gokulsreechandra/)  
- **Portfolio:** [GokulAIx](https://soft-truffle-eada3e.netlify.app/)
## 11. License
# This project is licensed under the [MIT License](LICENSE).
