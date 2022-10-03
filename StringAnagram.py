#Problem Statement
#A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
#The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. You need to determine this number.
#Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings. The strings a and b consist of lowercase English alphabets.
#Example

#a = 'cde'

#b = 'dcf'

#Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.
#Function Description
#Create a makeAnagram function below.
#Inputs:
#string a: a string
#string b: another string
#Output:
#int: the minimum total characters that must be deleted

a = 'cdee'
b = 'dcffge'

def makeAnagram(stringA,stringB):

  #fetching max char string
  if len(stringA)>len(stringB):
    max_len_str = stringA
    min_len_str = stringB
  else:
    max_len_str = stringB
    min_len_str = stringA
  
  #creating dict to store char as key and their count as values
  max_d = {}
  min_d= {}

  for char in max_len_str:          # string 1 dict
    if char in max_d.keys():
      max_d[char]+=1
    else:
      max_d[char]=1
  
  for char in min_len_str:          # string 2 dict
    if char in min_d.keys():
      min_d[char]+=1
    else:
      min_d[char]=1

  print(max_d)
  print(min_d)

  # counting the difference in the frequncy of chars by taking max char string
  x = 0                               # frequncy diff b/w common chars present in str1 and str2
  for i in max_d.keys():
    for n in min_d.keys():
      if i == n:
        if max_d[i] >= min_d[n]:
          c = max_d[i]-min_d[n]
        else:
          c = min_d[n]-max_d[i]
      
  x+=c
  
  z=0                                # frequncy of char present in str1 but not in str 2
  for i in max_d.keys():
    if i not in min_d.keys():
      z+= max_d[i]

  y=0                                # frequncy of char present in str2 but not in str 1
  for i in min_d.keys():
    if i not in max_d.keys():
      y+= min_d[i]

  total_freq_diff = x+z+y           # sum of all the frequncies to be deleted

  print(f'Total no. of characters to be deleted is: {total_freq_diff}')

makeAnagram(a,b)
