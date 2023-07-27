def logPost(Image_url, caption, Image_text, main_prompt, caption_prompt, time, final_image, post_link, flag):
  import pandas as pd
  df = pd.read_csv(r'C:\MEGA\Projects\Django\AutoPoster\Posts.csv')
  new_row = {'Image_url':str(Image_url),
            'caption':str(caption),
            'Image_text':str(Image_text),
            'main_prompt':str(main_prompt),
            'caption_prompt':str(caption_prompt),
            'time':str(time),
            'final_image':str(final_image),
            'post_link':str(post_link),
            'flag':str(flag)}
  df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
  df.to_csv('C:\MEGA\Projects\Django\AutoPoster\Posts.csv')