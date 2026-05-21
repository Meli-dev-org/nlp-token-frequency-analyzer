# NLP Token Frequency Analyzer

A lightweight Python project for text preprocessing, tokenization, word frequency analysis, and visualization.

## Features

- Text cleaning (removes punctuation and extra whitespace)
- Tokenization (converts text into words)
- Word frequency analysis using Counter
- Tabular representation using pandas
- Visualization of most frequent tokens using matplotlib

## Project Structure

.
├── token_frequency_analyzer.py
└── README.md

## Requirements

pip install pandas matplotlib

## How to Run

python token_frequency_analyzer.py

## Output

- Prints a frequency table
- Shows top 10 tokens
- Displays a bar chart visualization

## Custom Input

Edit text inside main():

text = "Your custom text here..."

Or load from file:

text = load_text_from_file("sample.txt")

## Purpose

A beginner-friendly NLP project for text preprocessing and basic data analysis in Python.

## License

MIT
