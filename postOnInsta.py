def postOnInsta(image_path, caption):
  from PIL import Image
  from instagrapi import Client

  # Instantiate the Instagram client
  client = Client()
  username = "bliss.admin"
  password = "MindOkay@2022"

  # Log in to your Instagram account
  client.login(username, password)

  # Open the image file
  image = Image.open(image_path)

  # Resize the image
  new_size = (1080, 1080)  # Set the desired resolution
  resized_image = image.resize(new_size)

  # Convert the image to RGB mode
  rgb_image = resized_image.convert("RGB")

  # Save the converted image as a JPEG file
  resized_image_path = 'C:\MEGA\Projects\Django\AutoPoster\modified_image.jpg'
  rgb_image.save(resized_image_path, "JPEG")

  # Upload the resized image
  media = (client.photo_upload(resized_image_path, caption=caption))

  # Log out of the Instagram account
  client.logout()

  return media
