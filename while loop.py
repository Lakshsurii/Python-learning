secret_code='laksh123'
count=1
user_guess=input('enter your guess')
if user_guess==secret_code:
    print('congrats')
else:
    

    while (secret_code!= user_guess):
          print('try again')
          user_guess=input('enter your guess')
          count=count+1
          if count>=3:
             print('no more attempts left')
             break
             print('congratulations')    
