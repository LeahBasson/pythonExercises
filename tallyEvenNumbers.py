numbers = [12,7,9,24,15,8,5] #given list
numOdds = 0
numEvens = 0
for x in range(7):
  numbers[x] = int(input("Enter Numbers: ")) #user enters the list values

#stores numbers
#numbers is a list
for x in numbers: #for heading
    if(x % 2) == 0:
        print("Even number found", x) #print(x % 2)
        numEvens += 1 #numEvens = numEvens + 1
    else:
        print("Odd number skipped:")
        numOdds += 1 #numOdds = numOdds + 1
        
print(x) #prints the last number.
print("Total Even Numbers: ",numEvens)
print("Total Odd Numbers: ",numOdds)