from PIL import Image # type: ignore

# Open the image
my_image = Image.open('Sky.jpg')

# Resize the image to a smaller size (16x16 pixels)
small_image = my_image.resize((80, 80), Image.BILINEAR)

# Scale it back to the original size
result_image = small_image.resize(my_image.size, Image.NEAREST)

# Save the result
result_image.save('GG2.png')