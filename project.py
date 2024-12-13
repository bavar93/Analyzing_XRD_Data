import pandas as pd  # For data handling
import numpy as np  # For mathematical operations
from scipy.signal import find_peaks, peak_widths  # For peak detection and FWHM calculation



# Define constants
K = 0.9  # Scherrer constant
WAVELENGTH = 0.15406  # X-ray wavelength for Cu Kα (in nm)


# 1. Function for Crystal Size Calculation
def calculate_crystal_size(fwhm_rad, theta):
    """
    Calculate crystal size using the Scherrer Equation.
    Parameters:
        fwhm_rad: Full Width at Half Maximum (FWHM) in radians
        theta: Bragg angle (θ) in radians
    Returns:
        Crystal size in nanometers (nm)
    """
    if fwhm_rad > 0:
        return (K * WAVELENGTH) / (fwhm_rad * np.cos(theta))
    return None


# 2. Function for d-Spacing Calculation
def calculate_d_spacing(theta):
    """
    Calculate interplanar spacing (d-spacing) using Bragg's Law.
    Parameters:
        theta: Bragg angle (θ) in radians
    Returns:
        d-spacing in nanometers (nm)
    """
    return WAVELENGTH / (2 * np.sin(theta))


# 3. Function for Lattice Parameter Calculation (for cubic systems)
def calculate_lattice_parameter(d_spacing, h, k, l):
    """
    Calculate the lattice parameter for cubic systems.
    Parameters:
        d_spacing: Interplanar spacing in nanometers
        h, k, l: Miller indices
    Returns:
        Lattice parameter in nanometers (nm)
    """
    if h + k + l > 0:
        return d_spacing * np.sqrt(h**2 + k**2 + l ** 2)
    return None


# 4. Function for Strain Calculation
def calculate_strain(fwhm_rad, theta):
    """
    Calculate microstrain in the crystal.
    Parameters:
        fwhm_rad: Full Width at Half Maximum (FWHM) in radians
        theta: Bragg angle (θ) in radians
    Returns:
        Strain (unitless)
    """
    return fwhm_rad / (4 * np.tan(theta))

def main():
    # Load XRD data
    file_path = "C:/Users/S. MR. B/PycharmProjects/pythonProject1/venv/XRD.csv"
    data = pd.read_csv(file_path)

    # Extract 2θ and intensity values
    angles = data["Angle"].values  # 2θ values
    intensities = data["Intensity"].values  # Intensity values

    # Detect peaks in the intensity data
    peaks, _ = find_peaks(intensities, height=100)  # Adjust height threshold as needed
    results_half = peak_widths(intensities, peaks, rel_height=0.5)  # FWHM

    # Define Miller indices for lattice parameter calculation (adjust as needed)
    miller_indices = [(1, 0, 0), (1, 1, 1), (2, 0, 0)]  # Example for cubic systems

    # Perform calculations for each peak
    results = []
    print("\nDetailed Calculations:")
    print(
        f"{'Peak':<6} {'2θ (deg)':<10} {'θ (rad)':<10} {'FWHM (rad)':<12} {'Crystal Size (nm)':<16} {'d-spacing (nm)':<14} {'Lattice Param (nm)':<18} {'Strain':<10}")
    for i, peak_idx in enumerate(peaks):
        peak_angle = angles[peak_idx]  # 2θ value at the peak
        theta = np.radians(peak_angle / 2)  # θ (half of 2θ) in radians
        fwhm_deg = results_half[0][i] * (angles[1] - angles[0])  # FWHM in degrees
        fwhm_rad = np.radians(fwhm_deg)  # Convert FWHM to radians

        # Call functions for calculations
        crystal_size = calculate_crystal_size(fwhm_rad, theta)
        d_spacing = calculate_d_spacing(theta)
        h, k, l = miller_indices[i] if i < len(miller_indices) else (0, 0, 0)
        lattice_param = calculate_lattice_parameter(d_spacing, h, k, l)
        strain = calculate_strain(fwhm_rad, theta)

        # Append results to the list
        results.append({
            "Peak Number": i + 1,
            "2θ (deg)": peak_angle,
            "FWHM (deg)": fwhm_deg,
            "FWHM (rad)": fwhm_rad,
            "Crystal Size (nm)": crystal_size,
            "d-spacing (nm)": d_spacing,
            "Lattice Parameter (nm)": lattice_param,
            "Strain": strain
        })

        # Print results
        print(
            f"{i + 1:<6} {peak_angle:<10.2f} {theta:<10.4f} {fwhm_rad:<12.4f} {crystal_size:<16.2f} {d_spacing:<14.4f} {lattice_param:<18.4f} {strain:<10.4e}")

    # Save results to a CSV file
    results_df = pd.DataFrame(results)
    output_file = "xrd_full_analysis.csv"
    results_df.to_csv(output_file, index=False)
    print(f"\nDetailed analysis saved to '{output_file}'")




if __name__ == "__main__":
    main()
