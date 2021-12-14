class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


# Avoid loading the image if you are not going to draw it
# Don't load image upon creation of bitmap
class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None # empty Bitmap object

    def draw(self):
        if not self._bitmap: # if the Bitmap object is empty
            self._bitmap = Bitmap(self.filename) # then create/initialize it
        self._bitmap.draw() # dont create new Bitmap object for unnecessary loading

def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')

if __name__ == '__main__':
    # bmp = Bitmap('facepalm.jpg')
    bmp = LazyBitmap('facepalm.jpg')
    draw_image(bmp)
    draw_image(bmp) # call twice but image only loads once
