import numpy as np
import scipy.ndimage
from skimage.transform import iradon

class ReconstructionModule:
    def __init__(self):
        self.projections = None
        self.angles = None
        self.image_size = None

    def load_projections(self, filename):
        self.projections = np.loadtxt(filename)
        self.angles = np.linspace(0, 179, self.projections.shape[0])

    def set_image_size(self, size):
        self.image_size = size

    def filtered_backprojection(self):
        return iradon(self.projections, self.angles, filter_name='ramp', output_size=self.image_size[0])

    def ART(self, iterations=10):
        reconstructed_image = np.ones(self.image_size)
        for _ in range(iterations):
            for i, angle in enumerate(self.angles):
                proj = self.projections[i, :]
                sim_proj = np.sum(scipy.ndimage.rotate(reconstructed_image, angle, reshape=False), axis=0)
                ratio = proj / (sim_proj + 1e-6)
                backproj_ratio = np.tile(ratio, (self.image_size[0], 1))
                rotated_backproj = scipy.ndimage.rotate(backproj_ratio, -angle, reshape=False)
                reconstructed_image *= rotated_backproj
            reconstructed_image /= np.max(reconstructed_image)
        return reconstructed_image

# Example usage
if __name__ == "__main__":
    recon = ReconstructionModule()
    recon.load_projections("projections.txt")
    recon.set_image_size((256, 256))

    fb_image = recon.filtered_backprojection()
    art_image = recon.ART(iterations=50)

    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].imshow(fb_image, cmap='gray')
    axs[0].set_title('Filtered Backprojection')
    axs[1].imshow(art_image, cmap='gray')
    axs[1].set_title('ART Reconstruction')
    plt.show()

