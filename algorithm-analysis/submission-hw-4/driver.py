from compress import Compress


def open_file():
    filename = "water-stays-saved.jpeg"
    try:
        image = Compress(filename)
        seam = image.best_seam()
        image.remove_color_seam(seam)
        image.save("water.jpeg")
    except Exception:
        raise


open_file()
