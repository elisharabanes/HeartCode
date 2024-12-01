def isAnagram(word1, word2):
  sortWord1 = sorted(word1) #sorts word1 into alphabethical order
  sortWord2 = sorted(word2) # sorts word2 alphabet order

   #checks if they are the same and returns whether or not is an   anagram
  if (sortWord1 == sortWord2): 
    print("True")
  else:
    print("False")
# test 1 
isAnagram('silent', 'listen')
# test 2 
isAnagram('maemae', 'elisha')