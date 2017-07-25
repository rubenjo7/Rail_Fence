def cipher(text, rails):
  m = (rails - 1) * 2
  out = ''
  for i in range(rails):
    if i % (rails - 1) == 0:
      # outer rail
      out += text[i::m]
    else:
      # inner rail
      char_pairs = zip(text[i::m], list(text[m-i::m]) + [''])
      out += ''.join(map(''.join, char_pairs))
  return out


