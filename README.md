# Nextword--LSTM

A simple next-word prediction project built using an LSTM model in TensorFlow/Keras. The project uses a FAQ-style text corpus about the CampusX Data Science Mentorship Program and demonstrates how to tokenize text, create input sequences, and train an LSTM to predict the next word.

## Project Overview

This repository contains a Jupyter notebook that walks through:

- Preparing text data
- Tokenizing words using `Tokenizer`
- Creating sequences for supervised learning
- Training an LSTM-based language model
- Predicting the next word from a sequence

## Repository Contents

- `Nextword.ipynb` — main notebook with the full implementation and experiments
- `Data` — FAQ dataset used for training
- `LSTM` — placeholder/working file for model-related code or extension

## What the Notebook Does

The notebook:

1. Defines a text corpus from FAQ-style content.
2. Fits a `Tokenizer` on the text.
3. Converts sentences into integer token sequences.
4. Builds training examples as sliding-window sequences.
5. Trains an LSTM model to learn word-to-word dependencies.
6. Demonstrates sequence generation for next-word prediction.

## Tech Stack

- Python
- TensorFlow / Keras
- Jupyter Notebook
- NumPy

## Setup

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install tensorflow jupyter notebook numpy
```

## Run

Open the notebook in Jupyter:

```bash
jupyter notebook Nextword.ipynb
```

Then run all cells to:

- load the dataset
- tokenize the text
- build sequences
- train the LSTM model
- inspect generated next-word predictions

## Example Use Case

This project is a beginner-friendly example of NLP sequence modeling and can be extended for:

- text generation
- chatbot response suggestions
- autocomplete systems
- next-token prediction for small corpora

## Notes

This is a learning project and intentionally uses a small dataset for educational purposes. It is a good starting point for understanding how recurrent neural networks can model language patterns.

## License

This project does not currently include a license file. If you plan to share or distribute it publicly, consider adding an appropriate open-source license.
