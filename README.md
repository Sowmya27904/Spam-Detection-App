# 📨 Spam Detection App

This is a simple yet powerful **Spam Detection Web App** built using **Machine Learning** and **Streamlit**.  
It classifies text messages as either **Spam** or **Not Spam**.

---

## ✅ Features

- ✅ Built using Python
- ✅ Uses Naive Bayes Classifier
- ✅ Trained on SMS Spam dataset
- ✅ Interactive Streamlit UI
- ✅ Real-time prediction of messages

---

## 📁 Files Included

```
Spam-Detection-App/
├── spamdetection.py   # Main Python app
├── spam.csv           # Dataset file
└── README.md          # Project documentation
```

---

## 🚀 How to Run

1. Clone the repository or download the files
2. Make sure Python is installed
3. Install dependencies:
```bash
pip install pandas scikit-learn streamlit
```

4. Run the app:
```bash
streamlit run spamdetection.py
```

---

## 🧠 Model Used

- **Algorithm**: Multinomial Naive Bayes
- **Vectorization**: CountVectorizer (with English stop words)
- **Data Split**: 80% Training, 20% Testing

---

## 📊 Dataset

This project uses a simple version of the **SMS Spam Collection Dataset**.  
The dataset has two columns:
- `Category` → Spam or Ham
- `Message` → The actual text message

---

## 🙌 Credits

Inspired by YouTube tutorials and beginner ML projects.
