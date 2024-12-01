def isAnagram(word1, word2):
  sortWord1 = sorted(word1) #sorts word1 into alphabethical order
  sortWord2 = sorted(word2) # sorts word2 alphabet order

  return sortWord1 == sortWord2 #checks if they are the same
