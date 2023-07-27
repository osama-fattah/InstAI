
def getCurrentAffairs():
  from GoogleNews import GoogleNews
  googlenews = GoogleNews(lang='en', region='US')
  googlenews.enableException(True)
  googlenews.set_lang('en')
  googlenews.set_period('1d')
  googlenews.set_time_range('02/01/2020','02/28/2020')
  googlenews.set_encode('utf-8')
  googlenews.get_news('mental health')
  return str(googlenews.get_texts()[0:20])