# Analyzing XRD Data
#### Video Demo:  <https://youtu.be/stXl3o5mQOY?si=rYf7aFsRzbL5xRHh>
#### Description:
This project is dedicated to the analysis of X-ray Diffraction (XRD) data using Python. The code in this project is designed to calculate various parameters related to crystal structures, such as crystal size, d-spacing, lattice parameter, and microstrain. These calculations are vital for material science research and are commonly used to analyze the properties and structure of crystalline materials.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Explained](#functions-explained)
- [Results](#results)
- [Future Work](#future-work)
- [Acknowledgments](#acknowledgments)

## Project Structure
The project consists of the following files:
- `project.py and test_project.py`: This is the main Python script containing all the functions and the main logic for the XRD data analysis, also test file of the project.
- `XRD.csv`: A sample CSV file containing XRD data (2θ and intensity values) that is used as input for the analysis.
- `README.md`: This README file that provides an overview and explanation of the project.
- `requirements.txt`: What libraries you need to install.

## Installation
To run this project, you need to have Python installed on your system. Additionally, you need to install the required libraries:
pip install pandas
pip install numpy
pip install scipy

## Usage
1. Place your XRD data file (CSV format) in the project directory.
2. Update the `file_path` variable in the `main` function to point to your XRD data file.
3. Run the `project.py` script to perform the analysis and generate results.

## Functions Explained
### 1. Crystal Size Calculation
The `calculate_crystal_size` function uses the Scherrer Equation to compute the crystal size based on the Full Width at Half Maximum (FWHM) and the Bragg angle (θ).

### 2. d-Spacing Calculation
The `calculate_d_spacing` function calculates the interplanar spacing (d-spacing) using Bragg's Law.

### 3. Lattice Parameter Calculation
For cubic crystal systems, the `calculate_lattice_parameter` function computes the lattice parameter using the d-spacing and the Miller indices (h, k, l).

### 4. Strain Calculation
The `calculate_strain` function determines the microstrain in the crystal based on the FWHM and the Bragg angle.

### Main Function
The `main` function:
- Loads the XRD data from a CSV file.
- Extracts the 2θ and intensity values.
- Detects peaks in the intensity data using `find_peaks`.
- Calculates the Full Width at Half Maximum (FWHM) for each peak using `peak_widths`.
- Performs various calculations for each detected peak and prints the results.
- Saves the detailed analysis results to a CSV file.

## Results
The script generates an output file (`xrd_full_analysis.csv`) that contains the detailed analysis results, including:
- Peak number
- 2θ value
- FWHM in degrees and radians
- Crystal size
- d-spacing
- Lattice parameter
- Strain

## Future Work
Future improvements to this project could include:
- Enhancing peak detection and analysis to handle more complex data sets.
- Implementing a graphical user interface (GUI) for easier interaction with the analysis tool.
- Including more advanced statistical analysis and visualization options.

## Acknowledgments
This project was inspired by the need for efficient and accurate XRD data analysis in materials science research. Special thanks to the creators of the libraries used in this project: pandas, numpy, and scipy.

Feel free to reach out if you have any questions or suggestions!
