# LED Matrix Transformation Script

This little Python Script made for transforming Images (png, jpg, etc.) and image sequences into Arduino Code. The program is made for the LEDTable by Nicco Kunzmann (https://github.com/niccokunzmann/ledtable).

To use the Script, just add the filenames of the image files (located in the same directory as the script) in Line 3 as well as the output file name (that must end with .ino) in line 4 and the size of the image in line 5 and 6. The images have to be maximum the size of the LED Matrix, though they can be smaller. You can also modify the delay of the images in an image sequence by editing the delay variable in line 7 (note this has to be in milliseconds).

After adding the information, just run the script and you get a fully operating Arduino Project you just have to compile and run.
