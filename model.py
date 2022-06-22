def get_generation(year):
  if year >= str(2013) and year <= str(2022):
    return "You are Gen Alpha"
  elif year >= str(1997) and year <= str(2012):
    return "You are Gen Z"
  elif year >= str(1981) and year <= str(1996):
    return "You are a Millennial"
  elif year >= str(1965) and year <= str(1980):
    return "You are Gen X"
  elif year >= str(1946) and year <= str(1964):
    return "You are a Boomer"
  elif year >= str(1928) and year <= str(1945):
    return "You belong to the Post War Generation"
  elif year >= str(1922) and year <= str(1927):
    return "You belong to the World War II Generation"
  elif year > str(2022):
    return "You are not born yet."
  else:
    return "You are old."