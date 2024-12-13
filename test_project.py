import unittest
import numpy as np
from project import (  # Import functions from your main script
    calculate_crystal_size,
    calculate_d_spacing,
    calculate_lattice_parameter,
    calculate_strain
)


class TestXRDCalculations(unittest.TestCase):
    # Constants for testing
    WAVELENGTH = 0.15406  # X-ray wavelength for Cu Kα (nm)
    K = 0.9  # Scherrer constant

    def test_calculate_crystal_size(self):
        """Test the crystal size calculation."""
        fwhm_rad = np.radians(0.2)  # Example FWHM in radians
        theta = np.radians(20)  # Example theta in radians
        expected = (self.K * self.WAVELENGTH) / (fwhm_rad * np.cos(theta))
        result = calculate_crystal_size(fwhm_rad, theta)
        self.assertAlmostEqual(result, expected, places=4)

    def test_calculate_d_spacing(self):
        """Test the d-spacing calculation."""
        theta = np.radians(20)  # Example theta in radians
        expected = self.WAVELENGTH / (2 * np.sin(theta))
        result = calculate_d_spacing(theta)
        self.assertAlmostEqual(result, expected, places=4)

    def test_calculate_lattice_parameter(self):
        """Test the lattice parameter calculation for cubic systems."""
        d_spacing = 0.2  # Example d-spacing in nanometers
        h, k, l = 1, 1, 1  # Example Miller indices
        expected = d_spacing * np.sqrt(h**2 + k**2 + l ** 2)
        result = calculate_lattice_parameter(d_spacing, h, k, l)
        self.assertAlmostEqual(result, expected, places=4)

    def test_calculate_strain(self):
        """Test the strain calculation."""
        fwhm_rad = np.radians(0.2)  # Example FWHM in radians
        theta = np.radians(20)  # Example theta in radians
        expected = fwhm_rad / (4 * np.tan(theta))
        result = calculate_strain(fwhm_rad, theta)
        self.assertAlmostEqual(result, expected, places=4)


# Run the tests
if __name__ == "__main__":
    unittest.main()
