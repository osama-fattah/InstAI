
def getPreviousPrompts():
  import pandas as pd
  with open('C:\MEGA\Projects\Django\AutoPoster\Posts.csv') as posts:
    q = pd.read_csv(posts)
    return(str(list(q["Image_text"])))