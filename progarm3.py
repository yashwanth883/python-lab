#A Sentence Statistics
sentence = input("Enter a sentence : ")
wordList = sentence.split(" ")
print("This sentence has", len(wordList), "words")
digCnt = upCnt = loCnt = 0
for ch in sentence:
 if '0' <= ch <= '9':
 digCnt += 1
 elif 'A' <= ch <= 'Z':
 upCnt += 1
 elif 'a' <= ch <= 'z':
 loCnt += 1
print("This sentence has", digCnt, "digits", upCnt, "upper case letters", loCnt,
"lower case letters")

#B String Similarity
str1 = input("Enter String 1 \n")
str2 = input("Enter String 2 \n")
if len(str2) < len(str1):
    short = len(str2)
    long = len(str1)
else:
    short = len(str1)
    long = len(str2)

matchCnt = 0
for i in range(short):
    if str1[i] == str2[i]:
        matchCnt += 1
print("Similarity between two said strings:")
print(matchCnt / long