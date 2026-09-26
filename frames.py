import picture

def frame(img):
  return

# load image
image = picture.load_image("crayons.jpg")

# set up dimension variables
width = picture.image_width(image)
height = picture.image_height(image)

# draw image onto canvas
picture.new_picture(width, height)
picture.draw_image(0, 0, image)

# save picture (show in different tab of codespace)
picture.save_picture("framed_crayons.jpg")