# Nextword--LSTM

A next-word prediction project built using an **LSTM (Long Short-Term Memory)** neural network with **TensorFlow/Keras**.

The project uses a FAQ-style text corpus about the **CampusX Data Science Mentorship Program**. The model learns word sequences from the text and predicts the most likely next word given an input sequence.

##  Live Demo

Live:

 **[Next Word Prediction using LSTM](https://nextword--lstm.streamlit.app/)**

---

##  Project Overview

This project demonstrates how an LSTM-based language model can be used for **next-word prediction**.

The complete workflow includes:

1. Preparing the text corpus
2. Tokenizing the text using Keras `Tokenizer`
3. Converting words into integer sequences
4. Creating supervised training sequences
5. Padding the input sequences
6. Building an LSTM-based neural network
7. Training the model
8. Predicting the next word
9. Saving the trained model and tokenizer
10. Deploying the model using Streamlit

---

##  Model Architecture

```text
Input Sequence
      ↓
Embedding Layer
      ↓
LSTM (150 units)
      ↓
LSTM (150 units)
      ↓
Dense Layer
      ↓
Softmax
      ↓
Predicted Next Word
```

### Model Configuration

- **Embedding dimension:** 100
- **First LSTM:** 150 units
- **Second LSTM:** 150 units
- **Input sequence length:** 56
- **Output vocabulary:** 283 words
- **Activation function:** Softmax
- **Framework:** TensorFlow / Keras

---

##  Repository Structure

```text
Nextword--LSTM/
│
├── Data
├── LSTM
├── screenshots/
│   ├── prediction_1.png
│   ├── prediction_2.png
│   └── prediction_3.png
├── Nextword.ipynb
├── nextword_lstm.keras
├── tokenizer.pkl
├── app.py
├── requirements.txt
└── README.md
```

### File Description

| File | Description |
| --- | --- |
| `Nextword.ipynb` | Complete notebook containing data preparation, tokenization, training, and prediction |
| `nextword_lstm.keras` | Trained LSTM model |
| `tokenizer.pkl` | Saved Keras tokenizer used during training |
| `app.py` | Streamlit application for next-word prediction |
| `requirements.txt` | Python dependencies required to run the application |
| `Data` | Dataset/text corpus used for training |
| `LSTM` | Model-related working directory |
| `screenshots/` | Screenshots showing prediction examples |

---

##  How It Works

The input text is first passed through the tokenizer. For example:

```text
what is the fee
```

The tokenizer converts the words into integer IDs, which are padded and passed to the trained model:

```text
Text
 ↓
Tokenizer
 ↓
Integer Sequence
 ↓
Padding
 ↓
LSTM Model
 ↓
Probability Distribution
 ↓
Predicted Word
```

The model then selects the word with the highest predicted probability.

---

## 💻 Example Predictions

The trained model is deployed as a Streamlit application.

### Example 1

**Input:**

```text
what
```

**Predicted next word:**

```text
is
```

---

### Example 2

**Input:**

```text
what is the fee
```

**Predicted next word:**

```text
of
```

---

### Example 3

**Input:**

```text
what is the fee of the
```

**Predicted next word:**

```text
mentorship
```

---

##  Streamlit Application

The model has been deployed using **Streamlit**. The application allows users to:

- Enter a text sequence
- Tokenize the input
- Convert it into the required sequence format
- Pad the sequence
- Pass it through the trained LSTM model
- Display the predicted next word

### Example

```text
Input:
what is the fee of the

Output:
mentorship
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Streamlit
- Jupyter Notebook

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/Vivek-ML001/Nextword--LSTM.git
cd Nextword--LSTM
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\\Scripts\\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

##  Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📓 Run the Notebook

To run the training notebook:

```bash
jupyter notebook Nextword.ipynb
```

The notebook contains the complete process for:

```text
Text Corpus
    ↓
Tokenization
    ↓
Sequence Generation
    ↓
Padding
    ↓
LSTM Training
    ↓
Next Word Prediction
```

---

##  Model and Tokenizer

The trained model is saved as:

```text
nextword_lstm.keras
```

The tokenizer used during training is saved as:

```text
tokenizer.pkl
```

Both are required for inference because the model expects the same vocabulary and token mapping used during training.

---

##  Limitations

This model is trained on a small domain-specific corpus. Therefore, its predictions are primarily useful for text patterns similar to the training data. It should not be considered a general-purpose language model.

---

##  License

This project does not currently include a license.

If you plan to distribute or modify the project publicly, consider adding an appropriate open-source license.

