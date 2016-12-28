from PIL import Image, ImageFilter

imageNames = list(['Katze.png','Katze2.png'])
filename = 'KatzeGross.ino'

imageCount = len(imageNames)

RGBValues = list()
	
sizeX = 7
sizeY = 14

imageNumber = 0
while imageNumber < imageCount:
    image = Image.open(imageNames[imageNumber])
    RGBImage = image.convert('RGB')
    i = 0
    while i < sizeY:
        j = 0
        while j < sizeX:
            r, g, b = RGBImage.getpixel((j,i))
            RGBValues.append(r)
            RGBValues.append(g)
            RGBValues.append(b)
            j += 1
        i += 1
    imageNumber += 1
file = open(filename, 'w')
file.write('#include <Adafruit_NeoPixel.h>' + "\n")
file.write('#include <ledtable.h>' + "\n")
file.write('#define DELAY 50' + "\n")
file.write('LEDTable ledtable = LEDTable(6, 20, 14, PIXELORDER<mirror_horizontally,double_spiral>);' + "\n")
file.write('#define IMAGES ' + str(imageCount) + "\n")
file.write('int mImageNumber = 0;')

file.write('void setup() {\n')
file.write('Serial.begin(9600);\n')
file.write('ledtable.begin();\n')
file.write('ledtable.brightness(20);\n')
file.write('}\n')

file.write('void image() {' + "\n")
imageNumber = 0
while imageNumber < imageCount:
    file.write('if (mImageNumber == ' + str(imageNumber) + ') {' + "\n")
    i = 0
    while i < sizeY:
        j = 0
        while j < sizeX:
            if (imageNumber == 0) or (RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * imageNumber * 3] != RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * (imageNumber - 1) * 3]) or (RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * imageNumber * 3 + 1] != RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * (imageNumber - 1) * 3 + 1]) or (RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * imageNumber * 3 + 2] != RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * (imageNumber - 1) * 3 + 2]):
                file.write('ledtable.fill(' + str(j) + ', ' + str(i) + ', RGB(' + str(RGBValues[(i * sizeX + j) * 3 + sizeX * sizeY * imageNumber * 3]) + ', ' + str(RGBValues[(i * sizeX + j) * 3 + 1 + sizeX * sizeY * imageNumber * 3]) + ', ' + str(RGBValues[(i * sizeX + j) * 3 + 2 + sizeX * sizeY * imageNumber * 3]) + '));' + "\n")
            j += 1
        i += 1
    imageNumber += 1
    file.write('}' + "\n")

file.write('}' + "\n")
file.write('void loop() {' + "\n")

file.write('image();' + "\n")
file.write('mImageNumber = mImageNumber + 1;' + "\n")
file.write('ledtable.show();\n')
file.write('if (mImageNumber == IMAGES) {' + "\n")
file.write('mImageNumber = 0;' + "\n")
file.write('}' + "\n")
file.write('delay(1000);' + "\n")
file.write('}' + "\n")

file.close()
