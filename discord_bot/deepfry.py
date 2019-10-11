from PIL import Image, ImageOps, ImageEnhance

def deepfry(image):
    image = Image.open(image)
    image = image.convert('RGB')
    width, height = image.width, image.height
    image = image.resize((int(width ** .9), int(height ** .75)), resample=Image.LANCZOS)
    image = image.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    image = image.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    image = image.resize((width, height), resample=Image.BICUBIC)
    image = ImageOps.posterize(image, 4)

    r = image.split()[0]
    r = ImageEnhance.Contrast(r).enhance(50.0)
    r = ImageEnhance.Brightness(r).enhance(3)
    r = ImageOps.colorize(r, (255, 0 , 0), (255, 255, 0))
    image = Image.blend(image, r, 0.75)
    image = ImageEnhance.Sharpness(image).enhance(0.0)
    
    return image