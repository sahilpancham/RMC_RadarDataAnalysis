import os
import pyart
import matplotlib.pyplot as plt
import csv
from tkinter import filedialog
from tkinter import Tk

# Open a Tkinter root window (it will be hidden)
root = Tk()
root.withdraw()

# Prompt the user to select one or more files from a folder using a dialog box
file_paths = filedialog.askopenfilenames(initialdir="D:/Raw", title="Select one or more files", filetypes=(("All files", "*.*"),))

if file_paths:
    header = ['File name','Field Name', 'MIN', 'MAX', 'AVERAGE']

    with open('Data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        for file_path in file_paths:
            # Extract the directory and file name
            directory = os.path.dirname(file_path)
            filename = os.path.basename(file_path)

            radar = pyart.io.read(file_path)
            # get the reflectivity data for the first sweep
            velo_data = radar.fields['velocity']['data'][0]
            refl_data=radar.fields['reflectivity']['data'][0]
            spectrum_data=radar.fields['spectrum_width']['data'][0]
            total_power_data=radar.fields['total_power']['data'][0]

            refl_min = refl_data.min()
            refl_max = refl_data.max()
            refl_mean = refl_data.mean()

            if refl_min < 30:
                refl_min = ''
            if refl_max < 30:
                refl_max = ''
            if refl_mean < 30:
                refl_mean = ''

            refl=[refl_min, refl_max, refl_mean]
            velo=[velo_data.min(),velo_data.max(),velo_data.mean()]
            spect=[spectrum_data.min(),spectrum_data.max(),spectrum_data.mean()]
            totalP=[total_power_data.min(),total_power_data.max(),total_power_data.mean()]

            data = [[filename,'reflectivity:',refl[0],refl[1],refl[2]],['','velocity:',velo[0],velo[1],velo[2]],['','spectrum_width:',spect[0],spect[1],spect[2]],['','total_power:',totalP[0],totalP[1],totalP[2]]]

            # write the data to the CSV file
            for row in data:
                # check if any value is empty or None, and replace it with ''
                row = [cell if cell is not None and cell != '' else '' for cell in row]
                writer.writerow(row)

        print("Data has been written to Data.csv.")
else:
    print("No files selected. Exiting.")
