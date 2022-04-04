#Write a script to enter any sentence and print those word which is palindrom. Also print total number of palindrom word.
i=[]
str=input("Enter any sentence:")
for word in str.split():
    if word==word[::-1]:
        print(word)
        i.append(word)       
print("total number of palingdrome words in a sentence:",len(i))        
        
        
