# Importing Image and ImageChops module from PIL package   
from PIL import Image, ImageChops  
from pwn import xor
     
# creating a image1 object  
im1 = Image.open(r"/home/b00130900/College/Secure-Communications/crytoHack/HEX/flag_7ae18c704272532658c10b5faad06d74.png") .convert("1") 
     
# creating a image2 object  
im2 = Image.open(r"/home/b00130900/College/Secure-Communications/crytoHack/HEX/lemur_ed66878c338e662d3473f0d98eedbd0d.png") .convert("1") 
     
# applying logical_xor method  
im3 = ImageChops.logical_xor(im1, im2)  
     
im3.save("/home/b00130900/College/Secure-Communications/crytoHack/HEX/lemur_decode.png")
im3.show()
ibytes = ImageChops.invert(im3)
ibytes.show()

import io
output = io.BytesIO()
im3.save(output, format="png")
image_as_string = output.getvalue()

print(str(image_as_string.decode))

print(xor(str(image_as_string),'crypto{'.encode()))
#print(xor('test'.encode(),'crypto{'.encode()))

