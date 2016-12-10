'''
This is just an experiment of mine to see if Tkinter is usable for out project.

Half-done.
'''

import tkinter as tk
import pandas as pd
import webbrowser

gt_df = pd.read_csv('gtd_wholedata_selected.csv', index_col = 'year').drop('eventid', 1)

# Architech the TK GUI
window = tk.Tk()
window.title('IVIS - Global Terrorism Analysis')
window.geometry('1000x1000')

# the value shown in lb2
var_info = tk.StringVar()
# Add all region names into the listbox
regions = tuple(gt_df.region.unique())
var_rg = tk.StringVar()
var_rg.set(regions)


def load_manual():
    # Need to change this url to UserManual's url
    webbrowser.open(r"http://nbviewer.jupyter.org/github/ICT4SD/Terrorism_Analysis/blob/master/IVIS/package/Final%20Draft%20-%20IVIS%20Project%20(Viola's%20Part).ipynb", new=2)
    var_info.set('UserManual has been opened in a new broswer window.')


lb = tk.Label(window, text='Welcome!', bg='pink', font=('Arial', 12),
              width=180, height=2).pack()

bt1 = tk.Button(window, text='See Manual',
               width=18, height=2, command=load_manual).pack()

lb2 = tk.Label(window, textvariable=var_info,
               bg='white', font=('Arial', 12),
               width=50, height=2)

#tx = tk.Text(window, height=2).pack()

ls = tk.Listbox(window, listvariable=var_rg)


def sel_region():
    name_rg = ls.get(ls.curselection())
    var_info.set('You have chosen the region: ' + name_rg)
    # Add all country names in chosen region
    countries = tuple(gt_df[gt_df.region==name_rg].country.unique())
    var_ctr = tk.StringVar()
    var_ctr.set(countries)
    ls_ctr = tk.Listbox(window, listvariable=var_ctr).pack()
    name_ctr = ls_ctr.get(ls_ctr.curselection())
    var_info.set('You have chosen the region: ' + name_ctr)


bt_re = tk.Button(window, text='Show Visualization',
               width=18, height=2, command=sel_region).pack()

lb2.pack()
ls.pack()

# def print_selection():
#     pass
#
# r1 = tk.Radiobutton(window, text='Option A',
#                     variable=var, value='A',
#                     command=print_selection)
# r2 = tk.Radiobutton(window, text='Option B',
#                     variable=var, value='B',
#                     command=print_selection)
# r3 = tk.Radiobutton(window, text='Option C',
#                     variable=var, value='C',
#                     command=print_selection)
# r1.pack()
# r2.pack()
# r3.pack()

window.mainloop()
