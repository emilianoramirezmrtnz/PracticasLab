import base64


image = open('hola_mundo.c', 'rb')
image_read = image.read()
image_64_decode = base64.b64encode(image_read) 
image_result = open('c.txt', 'wb')
image_result.write(image_64_decode)
