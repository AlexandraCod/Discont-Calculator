import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os
import webbrowser

def calculate_discount():
    try:
        original_price = eval(original_price_var.get())
        discounted_price = eval(discounted_price_var.get())
        discount_percentage = ((original_price - discounted_price) / original_price) * 100
        discount_percentage_var.set(f'{discount_percentage:.2f}%')

        calculated_price_label.config(text=f'= {original_price:.2f}')
    except (ValueError, ZeroDivisionError, SyntaxError):
        pass

def toggle_topmost():
    global is_topmost
    is_topmost = not is_topmost
    root.attributes("-topmost", is_topmost)
    if is_topmost:
        topmost_button.config(image=topmost_v2_image,)
    else:
        topmost_button.config(image=topmost_v1_image)

def callback(url):
    webbrowser.open_new(url)

def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.resizable(False, False)
    about_window.iconbitmap(os.path.join("Discont Calculator", "icon.ico"))
    about_background_label = tk.Label(about_window, bg="#D5E9F2")
    about_background_label.place(relwidth=1, relheight=1)
    
    lbl_name = tk.Label(text="Developer - Alexandra", master=about_window, bg="#D5E9F2")
    lbl_name.grid(row=0, column=0)

    lbl_github = tk.Label(text="Github- https://github.com/AlexandraCod", master=about_window, fg="blue", cursor="hand2", bg="#D5E9F2")
    lbl_github.grid(row=1, column=0)
    lbl_github.bind("<Button-1>", lambda e: callback("https://github.com/AlexandraCod"))

    buy_coffee = tk.Button(text="If you like it, pls Buy me a coffee!", master=about_window, bg="#FCA7AA")
    buy_coffee.grid(row=2,column=0,pady=3)
    buy_coffee.bind("<Button-1>", lambda e: callback("https://www.buymeacoffee.com/alexandracode"))

    lbl_name = tk.Label(
        text="How to use\n1. Enter the original value in the 'Original Price' field.\n2. Enter the discounted value in the 'Discounted Price' field.\n3. The tool will automatically calculate the discount percentage and display it in the 'Price Discount %' field.\n4. Click the pushpin button in the top right corner to keep the window on top.\n5. The tool not only calculates discounts. Enter a number in 'Discounted Price', and then input a mathematical expression in 'Original Price' field,  the result will appear above 'Price Discount %:'.\n\nNote:\n- Please enter valid numbers.\n- The input value should be greater than zero.",
        master=about_window, 
        bg="#D5E9F2",
        anchor='w',  
        justify='left'  
    )
    lbl_name.grid(row=3, column=0)


                 
root = tk.Tk()
root.title("Discount Calculator")
root.resizable(False, False)
root.iconbitmap(os.path.join("Discont Calculator", "icon.ico"))

topmost_v1_image = ImageTk.PhotoImage(Image.open(os.path.join("Discont Calculator", "pushpin v1.png")))
topmost_v2_image = ImageTk.PhotoImage(Image.open(os.path.join("Discont Calculator", "pushpin v2.png")))

background_label = tk.Label(root, bg="#D5E9F2")
background_label.place(relwidth=1, relheight=1)

# Original price entry
original_price_label = tk.Label(root, text="Original Price:", bg="#ace0f9")
original_price_label.grid(row=0, column=0,padx=(18, 0))
original_price_var = tk.StringVar()
original_price_var.trace_add("write", lambda *args: root.after_idle(calculate_discount))
original_price_entry = tk.Entry(root, textvariable=original_price_var)
original_price_entry.grid(row=0, column=1)

# Display original price result
calculated_price_label = tk.Label(root, text="Original Result", bg="#ace0f9")
calculated_price_label.grid(row=0, column=2)

# Add label for discounted price
discounted_price_label_var = tk.StringVar()
discounted_price_label = tk.Label(root, textvariable=discounted_price_label_var)
discounted_price_label.grid(row=1, column=1)
discounted_price_label_var.set("Discounted Price: ")

# Discounted price entry
discounted_price_label = tk.Label(root, text="Discounted Price:", bg="#ace0f9")
discounted_price_label.grid(row=1, column=0)
discounted_price_var = tk.StringVar()
discounted_price_var.trace_add("write", lambda *args: root.after_idle(calculate_discount))
discounted_price_entry = tk.Entry(root, textvariable=discounted_price_var)
discounted_price_entry.grid(row=1, column=1)

# Discount percentage display box
discount_percentage_label = tk.Label(root, text="Price Discount %:", bg="#FCA7AA")
discount_percentage_label.grid(row=1, column=2)
discount_percentage_var = tk.StringVar()
discount_percentage_entry = tk.Entry(root, textvariable=discount_percentage_var, state='readonly')
discount_percentage_entry.grid(row=1, column=3)

# Keep on top button
is_topmost = False
topmost_v1_image = PhotoImage(file=os.path.join("Discont Calculator", "pushpin v1.png"))
topmost_v2_image = PhotoImage(file=os.path.join("Discont Calculator", "pushpin v2.png"))
topmost_button = tk.Button(root, image=topmost_v1_image, command=toggle_topmost, borderwidth=0, highlightthickness=0, bg="#D5E9F2")
topmost_button.grid(row=0, column=3, padx=(90, 0))

about_button = tk.Button(root, text="About", command=show_about, bg="#D5E9F2")
about_button.grid(row=0, column=3, padx=(0, 50))

root.mainloop()
