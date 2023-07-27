from combine import combine
from genImage import genImage
from genPrompts import genPrompts
from genCaption import genCaption
from getCurrentAffairs import getCurrentAffairs
from postOnInsta import postOnInsta
from getPreviousPrompts import getPreviousPrompts
from logPost import logPost
from gettime import gettime
from UploadToDrive import UploadToDrive


previous_prompts = getPreviousPrompts()

image_prompt = ""

texts = []

try:
  currentAffairs = getCurrentAffairs()
except:
  currentAffairs = ""

main_prompt = """generate a single statement/sentence that is to be posted on instagam as an image
This should be a small statement/sentence which helps in promoting mental health and mental wellness and can be helpful for the user

be creative, think about a unique topic
DO NOT generate statements/sentences similar to these list of sentences (in curly brackets)
{"""+previous_prompts+"""}

The output shoud single lined"""

image_text = genPrompts(main_prompt)

print(image_text)

caption_prompt = "Generate a caption (with multiple relevant hastags) for an instagram post which says:- '"+image_text+"'"

caption_text = genCaption(caption_prompt)

print(caption_text)

image_prompt = "A serene scenery"

image = genImage(image_prompt)

print(image)

combine(image, image_text)

combined_image = "C:\MEGA\Projects\Django\AutoPoster\modified_image.png"

final_image = UploadToDrive(combined_image)

flag = input("post? (y/n): ")

post_link = 'None'

if(flag == 'y'):
  postLink = postOnInsta(combined_image, caption_text)
time = gettime()
logPost(image, caption_text, image_text, main_prompt, caption_prompt, time, final_image, post_link, flag)

