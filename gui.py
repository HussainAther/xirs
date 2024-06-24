from PyQt5 import QtWidgets
from simulation import SimulationModule
from reconstruction import ReconstructionModule
from visualization import VisualizationModule

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("X-Ray Imaging and Reconstruction Suite (XIRS)")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize modules
        self.simulation_module = SimulationModule()
        self.reconstruction_module = ReconstructionModule()
        self.visualization_module = VisualizationModule()
        
        # Setup GUI layout
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QtWidgets

