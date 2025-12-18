# 🧠 Trie Word Game

**Trie Word Game** is an engaging word puzzle built with **Python** and **Tkinter**. It demonstrates the power of the **Trie Data Structure** (Prefix Tree) for ultra-efficient word validation and prefix checking.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)

## 🎮 How it Works

1.  **Random Letters**: You are given a set of random letters (vowels and consonants).
2.  **Form Words**: Create valid English words using only the provided letters.
3.  **Trie Validation**: The game uses a custom **Trie Data Structure** to instantly verify if your word exists in the dictionary (`words.txt`).
4.  **Score & Time**:
    *   **Points**: Earn points based on word length.
    *   **Time Bonus**: Correct words grant you extra seconds! ⏳
    *   **High Stakes**: The game ends when the timer hits zero.

## ⚡ Technical Highlights

This project showcases the implementation of a **Trie (Prefix Tree)** from scratch:
*   **O(L) Lookups**: Word validation takes time proportional to the length of the word *L*, making it extremely fast compared to list searches.
*   **Memory Efficiency**: Compresses common prefixes to save space.
*   **Prefix Search**: Capable of quickly finding all words starting with a specific prefix (useful for hints).

## 🚀 How to Run

### Prerequisites
*   Python 3.x
*   Tkinter (usually included with Python)

### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/shayanRaza92/Trie_Word_Game.git
    ```
2.  Navigate to the directory:
    ```bash
    cd Trie_Word_Game
    ```
3.  **Run the Game**:
    ```bash
    python dsa_project.py
    ```

*(Note: Ensure `words.txt` is in the same directory as the script to load the dictionary.)*

## 🤝 Contributing
Want to improve the UI or add new game modes?
1.  Fork the repo.
2.  Make your changes.
3.  Submit a Pull Request!

