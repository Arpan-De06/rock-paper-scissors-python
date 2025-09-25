''' 1 for rock
0 for paper 
-1 for scissor 
you can choose between = 'r' which is tock ,'p' which is paper , 's' which is scissor  '''
import random
computer=random.choice([1,-1,0])
print("🎮 Welcome to Rock-Paper-Scissors!")
print("Make your choice:")
print("Rules: r = Rock, p = Paper, s = Scissors")
your_choice=input('enter your choice: ')
your_choice_dict={'r':1 ,'p':0,'s':-1}
reverse_dict={1: 'Rock', 0: 'Paper', -1: 'Scissor'}
you=your_choice_dict[your_choice]
print(f"you chose {reverse_dict[you]}\ncomputer chose {reverse_dict[computer]}")
if(computer==you):
    print('draw')
elif(computer==0 and you==1):
    print('you win')   
elif(computer==0 and you==-1):
    print('computer win')   
elif(computer==1 and you==0):
    print('you win')   
elif(computer==1 and you==-1):
    print('computer win')   
elif(computer==-1 and you==0):
    print('you win')   
elif(computer==-1 and you==1):
    print("computer win")
else:
    print('something went wrong!\n please try again')    


print("Thanks for playing! 👋")