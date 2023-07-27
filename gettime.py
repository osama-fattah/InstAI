def gettime():  
  from datetime import datetime
  return(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))