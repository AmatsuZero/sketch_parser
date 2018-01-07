from PIL import Image


def save_image(pic):
    try:
        image = Image.open(pic)
    except OSError as e:
        print(e)