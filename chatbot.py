import datetime
import wikipedia
import pyjokes
greetings={'hi':'Hi! I am peaches.','how are you':'Pretty Good','are you a robot?':'Yes I’m a robot but I’m a smart one!','bye':'Good Bye,Come back Soon!!',
           'date':datetime.date.today(),'time':datetime.datetime.now().time(),'thank you':'Glad to help!!'}
#you=input('You:')
#print(f'Peaches:{greetings[you]}')
while True:
    you=input('You:')
    if(you=='tell a joke'):
        print(pyjokes.get_joke())
        print('\n')
    elif you!='bye' and you in greetings:
        # you=input('You:')
        print(f'Peaches:{greetings[you]}')
        print('\n')
    elif you=='bye':
        print(f'Peaches:{greetings[you]}')
        break
    
    elif you not in greetings and you!='tell a joke':
        d={'wiki':(lambda x:wikipedia.summary(you,2))}
        print(d['wiki'](you))
        print('\n')
    