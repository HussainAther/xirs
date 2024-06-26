import matplotlib.pyplot as plt
from mayavi import mlab

class VisualizationModule:
    def __init__(self):
        pass

    def plot_2d(self, image, title="Image"):
        plt.figure()
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.colorbar()
        plt.show()

    def plot_3d(self, image):
        mlab.figure(size=(800, 800))
        mlab.imshow(image)
        mlab.colorbar()
        mlab.show()

# Example usage
if __name__ == "__main__":
    from reconstruction import ReconstructionModule

    recon = ReconstructionModule()
    recon.load_projections("projections.txt")
    recon.set_image_size((256, 256))

    art_image = recon.ART(iterations=50)

    viz = VisualizationModule()
    viz.plot_2d(art_image, title="ART Reconstruction")
    viz.plot_3d(art_image)

