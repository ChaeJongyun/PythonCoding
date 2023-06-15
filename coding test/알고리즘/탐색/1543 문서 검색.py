import sys
input = sys.stdin.readline

document =input()
word =input()

index=0
result=0

while len(document) - index >= len(word):
    if document[index : index+len(word)] == word:
        index += len(word)
        result +=1
    else:
        index+=1
        
print(result)        