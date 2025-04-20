import time
import random
import tkinter as tk
from tkinter import messagebox

def insert_word(trie, word, score=0):
    node = trie
    for i in word:
        if i not in node:
            node[i] = {}
        node = node[i]
    node['is_end_of_word'] = True
    node['score'] = score

def search_word(trie, word):
    node = trie
    for i in word:
        if i not in node:
            return False
        node = node[i]
    if 'is_end_of_word' in node:
        return True
    else:
        return False


def generate_random_letters(length):
    vowels = ["a","e","i","o","u"]
    consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
        
    random_vowels = random.sample(vowels, length // 2)
    random_consonants = random.sample(consonants, length - len(random_vowels))
    
    random_letters = random_vowels + random_consonants
    random.shuffle(random_letters)
    return random_letters


def is_valid_word(word, letters):
    for i in word:
        if i not in letters:
            return False
    return True

def load_words_from_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespace and newline characters
            words.append(word)
    return words

def start_game(words_file, time_limit):
    words = load_words_from_file(words_file)
    trie = {}
    for word in words:
        insert_word(trie, word)
    
    total_points = 0
    start_time = time.time()
    random_letters=generate_random_letters(10)
    entered_words = []

    def _submit_word():
        nonlocal total_points
        nonlocal start_time
        word = entry.get().lower()
        if word in entered_words:
            messagebox.showwarning("Error", "Word already entered.")
        elif is_valid_word(word, random_letters):
            if search_word(trie, word):
                if word not in entered_words:
                    entered_words.append(word)
                    word_score = len(word) * 10  # Points based on word length
                    total_points += word_score
                    messagebox.showinfo("Success", "Valid word! You earned " + str(word_score) + " points.")

                    # Add time to the timer equal to the length of the entered word in seconds
                    start_time += len(word)
                else:
                    messagebox.showwarning("Error", "Word already entered.")
            else:
                messagebox.showwarning("Error", "Word is not in the dictionary.")
        else:
            messagebox.showwarning("Error", "Invalid word. Use only the given letters.")
        score_label.config(text="Score: " + str(total_points))
        entry.delete(0, tk.END)

    def _update_time():
        nonlocal start_time
        time_remaining = time_limit - int(time.time() - start_time)
        if time_remaining > 0:
            time_label.config(text="Time remaining: " + str(time_remaining) + " seconds")            
            window.after(1000, _update_time)
        else:
            messagebox.showinfo("Time's up!", "Your final score: " + str(total_points))
            window.quit()

    window = tk.Tk()
    window.title("Word Game")

    # Set the size of the window
    window.geometry("800x600")  # Width x Height

    # Increase font size for labels
    label_font = ("Helvetica", 20)

    letters_label = tk.Label(window, text=f"Letters: {' '.join(random_letters)}", font=label_font)
    letters_label.pack()

    entry = tk.Entry(window, font=label_font)
    entry.pack()

    submit_button = tk.Button(window, text="Submit", command=_submit_word, font=label_font)
    submit_button.pack()

    score_label = tk.Label(window, text="Score: 0", font=label_font)
    score_label.pack()

    time_label = tk.Label(window, text=f"Time remaining: {time_limit} seconds", font=label_font)
    time_label.pack()

    _update_time()

    window.mainloop()

start_game('words.txt',60)

