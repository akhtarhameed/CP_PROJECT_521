def load_image(name):
    """Load image and return an aimage object"""

    fullname= name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print "Error: couldn't load image: ",fullname
        raise SystemExit, message
    return (image, image.get_rect())