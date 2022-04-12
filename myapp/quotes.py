import random

def Quotes():
  QUOTE_DICT = {'learning' : ['The capacity to learn is a gift; the ability to learn is a skill; the willingness to learn is a choice. ~Brian Herbert', 'Consistency of effort over the long run is everything. ~Angela Duckworth', 'Learning is the only thing the mind never exhausts, never fears, and never regrets. ~Leonardo DaVinci', 'The expert at anything was once a beginner. ~Helen Hayes']}

  QUOTES = sorted(QUOTE_DICT['learning'], key=lambda k: random.random())

  return QUOTES