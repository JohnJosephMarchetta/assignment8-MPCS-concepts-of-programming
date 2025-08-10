
# My approach is to use all possible keys to decypher the message, then compare the decyphered
# message for each key to the list of common words. The message with the most common words 
# corresponds to the correct key. 
# I assume that there are common words in this sentence and that only one key will produce 
# a phrase with sufficent words, let alone common words.

#I import functions which decrypt messages and parse the txt file into the contents of a list
# Each decrypted message is stored as a dictionary key and everytime a common appears in the 
# phrase its value increase by one. The dictionary is sorted by highest value to find the phrase.


from problem3 import caesar_decrypt
from problem4 import process_file
print("The message, ' mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp' is decrypted to be: ")
puzzle = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
messages=[]
for i in range(26):
    messages.append(caesar_decrypt(i,puzzle))
(filename, items, lines) = process_file("common_words.txt")
#dictionary to store key= (decyrpted message), and value=(number of common words)
dic={}
for i in messages:
    test= i.split()
    points=0
    for j in items:
        for k in test:
            if j==k:
                points+=1
    dic[i]=points
#Sort the dictionary by highest key, reverse the sorted function which takes asending order
sorted_dict= dict(sorted(dic.items(), key= lambda x: x[1],reverse=True))
print(list(sorted_dict)[0])
