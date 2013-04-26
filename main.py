import Tkinter as tk
import ttk
import xml.etree.ElementTree as ET
import tkFileDialog
import os
import re
import string
import zipfile


class App:
    def __init__(self, master):

        #self.search_dir = os.getcwd()
        self.search_dir = '/home/mmealman/hl_data'
        frame = tk.Frame(master)
        master.title('Hero Lab Search')
        frame.grid()

        self.entry_input = ttk.Entry(frame, width=50)
        self.entry_input.grid(row=1, column=1)
        self.entry_input.insert(0, self.search_dir)

        self.button_ask_input = ttk.Button(frame, text='Search Directory', command=self.ask_input)
        self.button_ask_input.grid(row=1, column=0)

        ttk.Label(frame, text='Name Search:').grid(row=2, column=0)
        self.search_name = ttk.Entry(frame, width=20)
        self.search_name.grid(row=2, column=1, sticky=tk.W)

        self.button_process = ttk.Button(frame, text="Search Files", command=self.search_files)
        self.button_process.grid(row=3, column=0, padx=5, pady=5)

        self.button_quit = ttk.Button(frame, text="Quit", command=frame.quit)
        self.button_quit.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

    def ask_input(self):
        result = tkFileDialog.askdirectory(initialdir=self.search_dir)
        if result:
            self.search_dir = result
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, result)

    def progress_close(self):
        tk.Toplevel.destroy(self.progressFrame)
        self.button_process['state'] = tk.NORMAL

    def search_files(self):

        self.button_process['state'] = tk.DISABLED

        self.progressFrame = tk.Toplevel()
        self.progressFrame.title('Search Progress')

        self.progressFrame.sbar = tk.Scrollbar(self.progressFrame)
        self.progressFrame.text = tk.Text(self.progressFrame, relief=tk.SUNKEN)
        self.progressFrame.text.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.progressFrame.sbar.config(command=self.progressFrame.text.yview)
        self.progressFrame.text.config(yscrollcommand=self.progressFrame.sbar.set)
        self.progressFrame.sbar.grid(row=0, column=1, sticky=tk.N + tk.S + tk.NE + tk.SE)
        self.progressFrame.text.insert(tk.INSERT, 'Processing files...\n\n')
        self.progressFrame.button_done = ttk.Button(self.progressFrame, text="Close",
                                                    command=self.progress_close)
        self.progressFrame.button_done.grid(row=1, column=0, columnspan=2, sticky=tk.S)

        self.progressFrame.button_done['state'] = tk.DISABLED

        tk.Grid.rowconfigure(self.progressFrame, 0, weight=1)
        tk.Grid.columnconfigure(self.progressFrame, 0, weight=1)
        self.progressFrame.update()

       # Parse Por/Stock files
        for filename in os.listdir(self.search_dir):
            if re.match('.*\.stock|.*\.por', filename):
                try:
                    lab_zip = zipfile.ZipFile(self.search_dir + '/' + filename, 'r')
                    for name in lab_zip.namelist():
                        if re.search('statblocks_xml.*\.xml', name):
                            xml_file = lab_zip.open(name)
                            tree = ET.parse(xml_file)
                            xml_file.close()
                            root = tree.getroot()

                            for char in root.iter('character'):
                                minions = char.find('minions')
                                char.remove(minions)
                                self.search(filename, char)

                                for minion in minions.iter('character'):
                                    self.search(filename, minion)
                    self.progressFrame.update()
                    lab_zip.close()
                except zipfile.BadZipfile:
                    pass

        self.progressFrame.text.insert(tk.INSERT, '\nCompleted')
        self.progressFrame.text.see(tk.END)
        self.progressFrame.button_done['state'] = tk.NORMAL

    def search(self, lab_file, char):
        lab_file = string.replace(lab_file, '.stock', '')
        lab_file = string.replace(lab_file, '.por', '')

        # Search name
        if re.search(self.search_name.get(), char.get('name'), re.IGNORECASE):
            self.progressFrame.text.insert(tk.INSERT, lab_file + ': ' + char.get('name') + '\n')
            self.progressFrame.text.see(tk.END)


root = tk.Tk()
app = App(root)
root.mainloop()
