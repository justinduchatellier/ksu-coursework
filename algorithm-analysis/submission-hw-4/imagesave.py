"""
Author: Justin Duchatellier
For: HW 4 with Prof Kretlow, Betty (Kennesaw State University)
Used code listed on ocw.mit.edu in Introduction to Algorithms
"""
from PIL import Image


class SeamError(Exception):
    # if exception handle and continue
    pass


def distance(pixel_a, pixel_b):
    """A distance metric between two pixels, based on their colors."""
    ans = 0
    for i in range(len(pixel_a)):
        value_a = pixel_a[i]
        value_b = pixel_b[i]
        ans += abs(value_a - value_b)
    return ans


class ImageSave(dict):
    # takes image and saves pixels in a dictionary
    def __init__(self, image):
        super().__init__()
        if not isinstance(image, Image.Image):
            image = Image.open(image)
            image = image.convert("RGB")
        self.width, self.height = image.size
        pixels = iter(image.getdata())
        for j in range(self.height):
            for i in range(self.width):
                self[i, j] = next(pixels)

    def remove_color_seam(self, seam):
        # remove the color seam by shifting all pixels to right
        for i, j in seam:
            for ii in range(i, self.width - 1):
                self[ii, j] = self[ii + 1, j]
            del self[self.width - 1, j]
        self.width -= 1

    def save(self, *args, **kwargs):
        self.image().save(*args, **kwargs)

    def image(self):
        # Returns a PIL Image that is represented by self.
        image = Image.new('RGB', (self.width, self.height))
        image.putdata(
            [self[i, j] for j in range(self.height) for i in range(self.width)])
        return image

    def energy(self, i, j):
        """Given coordinates (i,j), returns an energy, or cost associated
        with removing that pixel."""
        if i == 0 or j == 0 or i == self.width - 1 or j == self.height - 1:
            # For simplicity, return an arbitrarily large value on the edge.
            return 10000
        else:  # I think this is equivalent to the Sobel gradient magnitude.
            return distance(self[i - 1, j], self[i + 1, j]) + \
                   distance(self[i, j - 1], self[i, j + 1]) + \
                   distance(self[i - 1, j - 1], self[i + 1, j + 1]) + \
                   distance(self[i + 1, j - 1], self[i - 1, j + 1])
