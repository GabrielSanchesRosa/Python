def string_clean(s):
  string = "123456789"
  newstring = "".join([i for i in string if not i.isdigit()])
  return newstring