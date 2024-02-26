import tkinter as tk
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY=''
#enter your api key
#https://aistudio.google.com/ - get api key
genai.configure(api_key=GOOGLE_API_KEY)

#select any of the following models from the list of models provided by the google
model = genai.GenerativeModel('gemini-1.0-pro-latest')


def generate_response():
    input_text = text_field1.get()
    response = model.generate_content(input_text)
    result = response.text
    text_field2.delete(0, tk.END)  # Clear previous text
    text_field2.insert(0, result)  # Insert response into the second text field

# Create the main Tkinter window
root = tk.Tk()
root.title("AI Local")
root.geometry("1000x600")

# Create and place widgets

text_field1 = tk.Entry(root)
text_field1.config(width=550)
text_field1.pack(padx=10, pady=30)

button = tk.Button(root, text="Generate Response", command=generate_response)
button.pack(pady=10)


text_field2 = tk.Entry(root)
text_field2.config(width=5550)
text_field2.pack(padx=10, pady=20)

# Run the Tkinter event loop
root.mainloop()