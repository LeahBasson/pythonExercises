#Calculate the average score given 4 Tests written and display the result
#input - accept 4 test scores
#Calculate the average
#Display the average

line= "====================================="
t1 = int(input("Test score1: "))  #int() is a function that converts a string to an integer 
t2 = int(input("Test score2: "))
t3 = int(input("Test score3: "))
t4 = int(input("Test score4: "))
print(t1,t2,t3,t4)
print(type(t1),type(t2))

aveScore = (t1+t2+t3+t4)/4
print(line)
print(line)
print("The average score is", aveScore)
print(f"The average score is {aveScore:.2f}") #:.2f is the formatting you give it. Without the f it prints the literal value, a string.