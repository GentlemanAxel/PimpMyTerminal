import tkinter as tk
import os
from pyfiglet import Figlet


def create_batch_file(title, banner, user_input):
    script = '@echo off\ntitle {}\nmode 87, 30\nchcp 65001 >nul\ncd %homedrive%%homepath% >nul\n'.format(title)
    script += '\necho.\necho.\n{}\necho.\necho.\necho.\n'.format(banner)
    script += 'for /f %%A in (\'"prompt $H &echo on &for %%B in (1) do rem"\') do set BS=%%A\n:input\necho.\nset /p cmd=" {} "\necho.\n%cmd%\ngoto input'.format(user_input)
    with open('custom_cmd.bat', 'w') as file:
        file.write(script)
    os.startfile('custom_cmd.bat')


window = tk.Tk()
window.title("Pimp My Terminal")
window.geometry('800x100')


window.resizable(False, False)


window.configure(bg='black')


top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)
top_frame.configure(bg='black')


button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, pady=5)
button_frame.configure(bg='cyan')


title_label = tk.Label(top_frame, text='Title:')
title_label.pack(side=tk.LEFT, padx=5, pady=5)
title_entry = tk.Entry(top_frame)
title_entry.pack(side=tk.LEFT, padx=5, pady=5)


banner_label = tk.Label(top_frame, text='Banner:')
banner_label.pack(side=tk.LEFT, padx=5, pady=5)
banner_entry = tk.Entry(top_frame)
banner_entry.pack(side=tk.LEFT, padx=5, pady=5)


input_label = tk.Label(top_frame, text='User Input:')
input_label.pack(side=tk.LEFT, padx=5, pady=5)
input_entry = tk.Entry(top_frame)
input_entry.pack(side=tk.LEFT, padx=5, pady=5)


def update_banner(selected_font, space=30):
    # Use Figlet to create the ASCII banner with the selected font
    figlet = Figlet(font=selected_font)
    banner_lines = figlet.renderText(banner_entry.get()).split('\n')
    banner = '\n'.join(['echo.' + " " * space + line for line in banner_lines])
    return banner


ascii_options = ['3-d', '5lineoblique', 'banner', 'letters', 'alligator', 'bulbhead']
banner_font_var = tk.StringVar(value='slant')
banner_font_menu = tk.OptionMenu(top_frame, banner_font_var, *ascii_options, command=update_banner)
banner_font_menu.pack(side=tk.LEFT, padx=5, pady=5)


button2 = tk.Button(button_frame, text="Create & Preview Terminal", command=lambda: create_batch_file(title_entry.get(), update_banner(banner_font_var.get()), input_entry.get()))
button2.pack(side=tk.LEFT)


window.mainloop()
