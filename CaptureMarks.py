#Capture student test scores

num = int(input("How many score? ")) #4 
# score = [0,0,0,0,0] # a list of 4 scores set to zero values
scores = [] #an empty list
for x in range(num):
   # score[x] = int(input("Enter Score:")) #add to a static list
   print(x)
   m = int(input("Enter Score:"))
   scores.append(m) #append dynamically to a list
    
#print(score)#print the static list
print(scores)#print the dynamic list
