import keyword
import builtins

categories = {
  'keywords' : {
      'colour' : "#F92672",
      'matches': [x for x in keyword.kwlist if x is not 'def' and x is not 'class']
  },

  'builtins' : {
      'colour' : "#A6E22E",
      'matches': dir(builtins)
  },

  'defclass' : {
      'colour' : "#66D9EF",
      'matches': ["def", "class"]
  }
}

numbers = {
    'colour' : "#AE81FF",
}

strings = {
    'colour' : "#E6DB74",
}

commentlines = {
    'colour' : "#75715E",
}

commentblocs = {
    'colour' : "#75715E",
}
