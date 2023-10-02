import math

def cosine_similarity(text1, text2):

  vocab = sorted(set((text1 + ' ' + text2).split(' ')))
  #print(vocab)
  #print(text1, text2)

  n = 0
  d1 = 0
  d2 = 0
  for i in vocab:
    c1 = text1.count(i)
    c2 = text2.count(i)

    #print(i)
    #print(c1, c2)

    n += (c1 * c2)

    d1 += c1**2
    d2 += c2**2

    #print()

  d = math.sqrt(d1) * math.sqrt(d2)
  #print(n, '/', d)
  print(n/d)

cosine_similarity("Hello World", "Hello")
cosine_similarity("I love Troll 2", "I love Gymkata")

