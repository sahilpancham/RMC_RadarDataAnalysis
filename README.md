# RMC_RadarAnalysis

This project aims to develop a weather forecasting tool that can process a folder of radar files as input and generate a CSV file as output. The CSV file will contain the minimum, maximum, and mode values for each factor, including reflectivity, velocity, spectrum width, and power.

          The goal of this weather forecasting tool is to provide meteorologists with a powerful and efficient tool that can help them make more accurate weather predictions. The tool takes a folder of radar files as input, which contain data about reflectivity, velocity, spectrum width, and power of precipitation. The radar data is processed using advanced data processing techniques to extract relevant information and calculate the required parameters.

		

  


Radar Data Analysis Flask Application
This Flask application is designed to perform analysis on radar data files. It allows users to select one or more radar data files and extract various statistical measures from the data, such as minimum, maximum, and mode values. The analysis is performed on fields like reflectivity, velocity, spectrum width, and total power.

Installation
To run the application, follow these steps:

Clone the repository or download the source code files.
Install the required dependencies by running pip install -r requirements.txt.
Make sure you have Tkinter and its dependencies installed. If not, install them based on your operating system.
Set the initial directory in the filedialog.askopenfilenames function to the desired location of your radar data files.
Start the Flask application by running python app.py.
Open a web browser and access the application at http://localhost:5000.
Usage
Upon accessing the application, you will be presented with the home page.
Click on the "Start" button to select radar data files using the file dialog.
After selecting the files, the application will analyze each file and generate a CSV file named "Data.csv" containing the statistical measures for each field in the radar data.
Once the analysis is complete, you will see a message confirming that the data has been written to "Data.csv".
You can download the generated CSV file by clicking on the "Download" link.
Navigate to the "Contact" page to find contact information for any support or inquiries.
Configuration
The initial directory for file selection can be configured by modifying the initialdir parameter in the filedialog.askopenfilenames function.
Ensure that the necessary radar data files are located in the specified directory.
Contact
For any questions or support related to this application, please contact Sahil Pancham at sahilpancham10@gmail.com.
