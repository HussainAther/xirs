## X-Ray Imaging and Reconstruction Suite (XIRS)

Welcome to the X-Ray Imaging and Reconstruction Suite (XIRS)! This comprehensive software suite is designed to integrate simulation, reconstruction, and analysis tools for advanced X-ray imaging projects. It combines various algorithms and visualization techniques to provide a robust platform for researchers and practitioners in medical imaging and related fields.

---

### Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Modules Overview](#modules-overview)
5. [Example Workflow](#example-workflow)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

---

### Features

- **Simulation Module**:
  - Integration with TOPAS for detailed X-ray simulation.
  - Configurable geometry for X-ray source, detector, and object.
  - Easy modification of simulation parameters.

- **Reconstruction Module**:
  - Implementation of various reconstruction algorithms: Filtered Backprojection, ART, SIRT, and MARt.
  - Deconvolution techniques including Wiener filtering and Richardson-Lucy deconvolution.
  - Support for iterative reconstruction and deconvolution processes.

- **Visualization and Analysis Module**:
  - 3D visualization of reconstructed images.
  - Quantitative analysis tools: SNR, MSE, PSNR.
  - Side-by-side comparison of different reconstruction methods.

- **User Interface**:
  - Interactive GUI for ease of use.
  - Scriptable interface for advanced automation and customization.

- **Data Management**:
  - Project management for saving configurations, raw data, and results.
  - Export and import functionality for interoperability.

---

### Installation

#### Prerequisites

- Python 3.x
- TOPAS (for X-ray simulation)
- The following Python libraries:
  - NumPy
  - SciPy
  - Matplotlib
  - Seaborn
  - PyQt5
  - VTK
  - Mayavi
  - HDF5

#### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/XIRS.git
   cd XIRS
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure TOPAS is installed and properly configured on your system.

---

### Usage

1. **Run the main script**:
   ```bash
   python main.py
   ```

2. **Navigate the GUI**:
   - Use the Simulation Module to set up and run X-ray simulations.
   - Import projection data into the Reconstruction Module to apply various reconstruction algorithms.
   - Visualize and analyze the reconstructed images using the Visualization Module.

---

### Modules Overview

#### Simulation Module

Handles the integration with TOPAS for X-ray simulations. Users can define the geometry of the imaging system, modify simulation parameters, and run simulations to generate projection data.

#### Reconstruction Module

Implements various reconstruction algorithms (e.g., Filtered Backprojection, ART, SIRT, MARt) and deconvolution techniques (e.g., Wiener filtering, Richardson-Lucy deconvolution). Supports iterative reconstruction for enhanced image quality.

#### Visualization and Analysis Module

Provides tools for 3D visualization of reconstructed images, quantitative analysis (e.g., SNR, MSE, PSNR), and comparison of different reconstruction methods.

#### User Interface

Built with PyQt5, the interactive GUI allows users to easily interact with the software, while a scriptable interface enables advanced automation and customization.

---

### Example Workflow

1. **Simulation**:
   - Define the X-ray source, detector, and object geometry in the Simulation Module.
   - Run simulations in TOPAS and generate projection data.

2. **Reconstruction**:
   - Import the projection data into the Reconstruction Module.
   - Apply reconstruction algorithms and refine the results with iterative deconvolution.

3. **Visualization and Analysis**:
   - Visualize the reconstructed images in 3D.
   - Perform quantitative analysis to assess image quality.
   - Compare different reconstruction methods.

---

### Contributing

We welcome contributions from the community! If you would like to contribute to XIRS, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request with a detailed description of your changes.

---

### License

XIRS is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contact

If you have any questions, issues, or suggestions, please contact:

- **Syed Hussain Ather**
- **Mikhail Mazuritskiy**
- **Richard Gordon**

You can also open an issue on the GitHub repository.

Thank you for using XIRS! We hope this software helps advance your X-ray imaging and reconstruction projects.

