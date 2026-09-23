import streamlit as st
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# -----------------------------
# Load model and tokenizer
# -----------------------------

model = load_model("nextword_lstm.keras")

with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)


MAX_SEQUENCE_LEN = 56


# -----------------------------
# Prediction function
# -----------------------------

def predict_next_word(text):

    token_list = tokenizer.texts_to_sequences([text])[0]

    if len(token_list) == 0:
        return None

    token_list = pad_sequences(
        [token_list],
        maxlen=MAX_SEQUENCE_LEN,
        padding="pre"
    )

    predicted = model.predict(token_list, verbose=0)

    predicted_word_id = np.argmax(predicted, axis=-1)[0]

    for word, index in tokenizer.word_index.items():

        if index == predicted_word_id:
            return word

    return None


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("Next Word Prediction using LSTM")

st.write(
    "Enter some text and the LSTM model will predict the next word."
)

text = st.text_input(
    "Enter your text:",
    placeholder="For example: what is"
)


if st.button("Predict Next Word"):

    if text.strip():

        next_word = predict_next_word(text)

        if next_word:
            st.success(f"Predicted next word: **{next_word}**")
        else:
            st.warning("Could not predict a word.")

    else:

        st.warning("Please enter some text.")
