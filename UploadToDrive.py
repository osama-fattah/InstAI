def UploadToDrive(path):  
  import cloudinary.uploader as cupload
  import cloudinary
  cloudinary.config( 
    cloud_name = "dbolacyvf", 
    api_key = "674276816373138", 
    api_secret = "DUchYV04RNTJjCUp_9YQ9hpuE30" 
  )

  # Specify the path of the image you want to upload
  image_path = path

  # Upload the image to Cloudinary
  response = cupload.upload(image_path)

  # Retrieve the URL of the uploaded image
  image_url = response['secure_url']
  return(image_url)