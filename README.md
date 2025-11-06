# 📩 Spam Detection System using Naive Bayes

This project is a **Spam Detection System** built with **Python** and **Machine Learning**, capable of classifying messages as **Spam** or **Ham (Non-Spam)**.  
It uses **TF-IDF vectorization** with a **Multinomial Naive Bayes** model — achieving an impressive **Precision Score of 1.00** 🎯.

---

## 🚀 Project Overview

The main goal of this project was to build an efficient and accurate text classification model that can automatically detect spam messages from real ones.

### 🔍 Key Steps in the Pipeline
1. **Data Cleaning:**  
   Removed unwanted characters, punctuation, stopwords, and converted all text to lowercase.  

2. **Exploratory Data Analysis (EDA):**  
   Visualized spam vs ham message distribution using `matplotlib`, `seaborn`, and `wordcloud`.

3. **Data Preprocessing:**  
   Tokenization, stopword removal, and text normalization using **NLTK**.  
   Text converted into numerical form using **TF-IDF Vectorizer**.

4. **Model Building:**  
   Implemented and compared models, selecting **Multinomial Naive Bayes** due to superior performance with text features.

5. **Model Evaluation:**  
   Evaluated with metrics like **Precision**, **Recall**, **F1-Score**, and **Accuracy**.  
   Final precision: **1.00** ✅

6. **Deployment:**  
   Built a user-friendly **Streamlit** web app for real-time spam detection.

---

## 🧠 Model Used

- **Algorithm:** Multinomial Naive Bayes  
- **Feature Extraction:** TF-IDF Vectorizer  
- **Reason:** Achieved the highest precision score (1.00), ensuring minimal false positives.

---

## 🧰 Libraries Used

| Library | Purpose |
|----------|----------|
| **NumPy** | Numerical operations |
| **Pandas** | Data manipulation |
| **Scikit-learn** | ML modeling & metrics |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical plotting |
| **NLTK** | Natural language preprocessing |
| **WordCloud** | Visual word analysis |
| **Streamlit** | Web app deployment |

---

## 💻 How to Run Locally

```bash
# Clone this repository
git clone https://github.com/Zubii07/spam-detection-system.git
cd spam-detection-system

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
