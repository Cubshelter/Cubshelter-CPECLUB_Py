import random
number = random.randint(1, 50)
my_secret_number = number;
trial = 3
my_trial = 0

while(my_trial != trial):
   guess = int( input("Guess Number: "))
   my_trial += 1

   if(guess == my_secret_number):
      print("Correct. You're a genuis.")
      break
   elif(guess > my_secret_number):
      print("Nah. Too high!")
   elif(guess < my_secret_number):
       print("ughh. Too low!")
   else:
      print("Time up. The number was, end" "")
      print(my_secret_number) 
      break
  # my_trial += 1
   if (my_trial == trial) and (guess != my_secret_number):
      print("Time up. The number was...", (my_secret_number) )
print("Game over")
