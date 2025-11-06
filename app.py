import streamlit as st
import pickle

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('SMS Spam Detection')
st.write('Enter an SMS message to check if it is Spam or Not Spam.')

user_input = st.text_area("Message")

if st.button("Check"):
    # Preprocess the input
    input_data = tfidf.transform([user_input]).toarray()
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("Spam.")
    else:
        st.write("Not Spam.")
