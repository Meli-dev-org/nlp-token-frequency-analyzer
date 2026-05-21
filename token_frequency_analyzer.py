import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# 1. Clean text
# -------------------------
def clean_text(text: str) -> str:
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# -------------------------
# 2. Tokenize text
# -------------------------
def tokenize(text: str):
    return text.lower().split()


# -------------------------
# 3. Count token frequencies
# -------------------------
def get_token_frequencies(tokens):
    return Counter(tokens)


# -------------------------
# 4. Create frequency table
# -------------------------
def create_frequency_table(counter, top_n=30):
    most_common = counter.most_common(top_n)
    return pd.DataFrame(most_common, columns=["Token", "Frequency"])


# -------------------------
# 5. Plot top tokens
# -------------------------
def plot_top_tokens(df, top_n=20):
    df = df.head(top_n)

    plt.figure(figsize=(10, 5))
    plt.bar(df["Token"], df["Frequency"])
    plt.xticks(rotation=45)
    plt.title("Top Token Frequencies")
    plt.xlabel("Tokens")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


# -------------------------
# 6. Load text from file
# -------------------------
def load_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# -------------------------
# MAIN PIPELINE
# -------------------------
def main():
    text = """
    This is a sample text. This text is for testing tokenization!
    Tokenization is fun. Fun fun fun!!!
    """

    # Optional: load from file instead
    # text = load_text_from_file("sample.txt")

    cleaned = clean_text(text)
    tokens = tokenize(cleaned)

    freq = get_token_frequencies(tokens)
    table = create_frequency_table(freq)

    print("\nTop Tokens Table:\n")
    print(table)

    print("\nTop 10 Tokens:\n")
    print(table.head(10))

    plot_top_tokens(table)


if __name__ == "__main__":
    main()