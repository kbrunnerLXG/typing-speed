from tkinter import *
import requests
import time
from random import choice
from timer import Stopwatch


class TypingSpeedTest:
    def __init__(self, window):
        self.window = window
        self.window.title('Typing Speed')
        self.bg_col = '#DAF7A6'
        self.window.config(height=800, width=800, pady=15, padx=15, bg=self.bg_col)
        self.typing_test_texts = [
            "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet at least once, making it a perfect example for typing practice. Speed and accuracy are crucial when it comes to improving your typing skills. Keep practicing regularly to see noticeable improvements in your typing speed.",
            "In a small village nestled between two mountains, there was a quaint little bakery known for its delicious pastries. Every morning, the aroma of freshly baked bread filled the air, attracting villagers from near and far. The baker, an old man with a kind smile, took pride in his craft and loved seeing the joy his creations brought to others.",
            "Technology has revolutionized the way we live, work, and communicate. From smartphones to artificial intelligence, advancements continue to shape our world in unprecedented ways. Embracing these changes can lead to greater efficiency and new opportunities. However, it's also important to remain mindful of the ethical implications and strive for a balance between progress and responsibility.",
            "Once upon a time, in a land far away, there was a kingdom ruled by a wise and benevolent king. The kingdom flourished under his reign, with peace and prosperity touching every corner. The people were happy and content, living in harmony with one another. This idyllic state was maintained through the king's fair and just governance, which prioritized the welfare of his subjects above all else.",
            "Learning a new language can be both challenging and rewarding. It opens up a world of opportunities, allowing you to connect with people from different cultures and backgrounds. The key to mastering a new language is consistent practice and immersion. Whether through reading, writing, speaking, or listening, engaging with the language regularly will help you build fluency and confidence."
        ]
        self.sample_text = choice(self.typing_test_texts)
        self.start_time = None
        # ---------------------Labels---------------------------------------------#
        self.title = Label(window, text='Typing Speed test', fg='Black', bg=self.bg_col, font=("Aerial", 40, "bold"))
        self.title.grid(row=0, column=1, columnspan=3)
        self.sample_text_label = Label(window, text=self.sample_text, fg='Black', bg=self.bg_col, wraplength=650,
                                       font=("Aerial", 10))
        self.sample_text_label.grid(row=2, column=1, columnspan=3)
        self.result_label = Label(window, text='', font=("Aerial", 14), bg=self.bg_col)
        self.result_label.grid(columnspan=3, row=5, column=1)
        # ---------------------Text Entry-----------------------------------------#
        self.user_entry = Text(window, height=10, width=60, wrap=WORD)
        self.user_entry.grid(column=1, row=3, columnspan=3)
        self.user_entry.bind("<Return>", self.calculate_speed)
        # ---------------------Buttons---------------------------------------------#
        self.start_button = Button(window, text='Start Typing', font=("Aerial", 15), command=self.start_test)
        self.start_button.grid(column=1, row=4, columnspan=3)

    def start_test(self):
        self.user_entry.delete(1.0, END)
        self.user_entry.focus()
        self.start_time = time.time()
        self.result_label.config(text="")

    def calculate_speed(self, event):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        typed_text = self.user_entry.get(1.0, END)

        word_count = len(typed_text.split())
        wpm = (word_count / elapsed_time) * 60
        self.result_label.config(text=f'WPM:{wpm:.2f}')


# -----------------------UI Setup-----------------------------------------#
if __name__ == "__main__":
    window = Tk()
    typing_test = TypingSpeedTest(window)
    window.mainloop()
