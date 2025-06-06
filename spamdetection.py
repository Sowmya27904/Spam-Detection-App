import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Load the dataset
data = pd.read_csv("spam.csv", encoding='latin1')

# Clean the data
data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])

# Separate features and labels
mess = data['Message']
cat = data['Category']

# Train-test split
mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.2)

# Vectorize text
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

# Train the model
model = MultinomialNB()
model.fit(features, cat_train)

# Define prediction function
def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result[0]

# Streamlit UI
st.title('📨 Spam Detection App')
st.write('This app uses Machine Learning to detect whether a message is **Spam** or **Not Spam**.')

input_mess = st.text_input('Enter your message here:')

if st.button('Validate'):
    output = predict(input_mess)
    st.markdown(f'### 🟢 Result: **{output}**')
