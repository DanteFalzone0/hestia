#!/usr/bin/env python3
import tkinter as tk
from tkinter import Button


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hestia [pre-alpha]")
        self.root.geometry("640x480")

        self.send_button = Button(
            self.root,
            text="Send message",
            bg="black", fg="#00FF44",
            command=self.display_message,
            width=640,
            anchor=tk.S
        )
        self.send_button.pack(side="bottom", anchor="sw")

        self.entry_field = tk.Entry(
            self.root, fg="#00FF44", bg="black",
            width=640
        )
        self.entry_field.pack(side="bottom", anchor="w")

        self.left_half = tk.Entry(
            self.root, width=320,
            bg="black", fg="#00FF44"
        )
        self.left_half.pack(side="left", anchor="nw")

        self.right_half = tk.Frame(self.root, width=320, border=5, bg="red")
        self.right_half.pack(side="right", anchor="ne")

        self._messages = []

        self.mainloop = self.root.mainloop

    def display_message(self, text=None):
        if text:
            self._messages.append(text)
        else:
            self._messages.append(
                "default-user > " + self.entry_field.get()
            )
        self.left_half.insert(len(self._messages), "\n".join(self._messages))
        self.entry_field.insert(0, "default-user > ")


def main(window):
    window.mainloop()

if __name__ == "__main__":
    main_window = MainWindow()
    main(main_window)
