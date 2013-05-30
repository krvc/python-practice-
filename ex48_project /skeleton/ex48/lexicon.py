dictionary = {
              'direction' : ['north', 'south', 'east'],
              'verb'      : ['go', 'kill', 'eat'],
              'stop'      : ['the', 'in', 'of'],
              'noun'      : ['bear', 'princess']
             }

def scan(sentence):
  response = []
  words = sentence.split()

  for word in words:
    found_in_dictionary = False
    for key in dictionary.keys():

      if word in dictionary[key]:
        response.append((key, word))
        found_in_dictionary = True
        continue

    if not found_in_dictionary:
      try:
        response.append(('number', int(word)))
      except ValueError:
        response.append(('error', word))

  return response
