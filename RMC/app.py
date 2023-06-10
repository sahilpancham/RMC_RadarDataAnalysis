from flask import Flask, render_template, send_file
import os
import pyart
import matplotlib.pyplot as plt
import statistics as st
import csv
from tkinter import filedialog
from tkinter import Tk

app = Flask(__name__)

@app.route('/')

def start():


    return render_template('start.html')


@app.route("/start")
def index():
    # Open a Tkinter root window (it will be hidden)
    root = Tk()
    root.withdraw()

    # Prompt the user to select one or more files from a folder using a dialog box
    file_paths = filedialog.askopenfilenames(initialdir="D:/Raw", title="Select one or more files", filetypes=(("All files", "*.*"),))

    if file_paths:
        header = ['File name','Field Name', 'MIN', 'MAX', 'Mode']

        with open('Data.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)


            def find_freq(x):
                numpy_array = x.compressed()
                n_list=[]
        
                for i in numpy_array:  
                    if(i>=30 and i<=80):
                        n_list.append(i)
    
                if(len(n_list) > 0):  
                    return st.mode(n_list)
    
                else:
                    return 0

            for file_path in file_paths:
                # Extract the directory and file name
                directory = os.path.dirname(file_path)
                filename = os.path.basename(file_path)

                radar = pyart.io.read(file_path)
                # get the reflectivity data for the first sweep
                velo_data = radar.fields['velocity']['data']
                refl_data=radar.fields['reflectivity']['data']
                spectrum_data=radar.fields['spectrum_width']['data']
                total_power_data=radar.fields['total_power']['data']

                refl=[refl_data.min(),refl_data.max(),find_freq(refl_data)]
                velo=[velo_data.min(),velo_data.max(),st.mode(velo_data.compressed())]
                spect=[spectrum_data.min(),spectrum_data.max(),st.mode(spectrum_data.compressed())]
                totalP=[total_power_data.min(),total_power_data.max(),find_freq(total_power_data)]

                data = [[filename,'','','',''],['','reflectivity:',refl[0],refl[1],refl[2]],['','velocity:',velo[0],velo[1],velo[2]],['','spectrum_width:',spect[0],spect[1],spect[2]],['','total_power:',totalP[0],totalP[1],totalP[2]]]

                # write the data to the CSV file
                
                    # check if any value is empty or None, and replace it with ''

                writer.writerow(data[0])        
                writer.writerow(data[1])     
                writer.writerow(data[2])
                writer.writerow(data[3])
                writer.writerow(data[4])
                
                    # writer.writerow(row)

            message = "Data has been written to Data.csv."
            
    else:
        message = "No files selected. Exiting."

    with open('Data.csv', 'r') as f:
        data = list(csv.reader(f))

    return render_template("index.html", message=message, data=data)


@app.route('/download')
def download():   
    return send_file('Data.csv', as_attachment=True)


@app.route('/contact')

def contact():

    return render_template('contact.html')

if __name__ == "__main__":
    app.run()
