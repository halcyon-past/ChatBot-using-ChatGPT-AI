from dotenv import load_dotenv
import openai
import os
from tkinter import *

def configure():
    load_dotenv()
    openai.api_key = os.getenv('key_api')

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

bot_name = "Xeverus"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Xeverus")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=750, height=700, bg=BG_COLOR)
        self.window.iconbitmap('icon.ico')

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                            text="ChatBot using ChatGPT - Aritro Saha", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=1)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                            command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)

        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {self.get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    #chatbot response
    def get_response(self, msg):
        output = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role":"user","content":msg}]
        )

        bot_response = output.choices[0]['message'].content

        return bot_response.strip()



if __name__ == "__main__":
    configure()
    app = ChatApplication()
    app.run()
    