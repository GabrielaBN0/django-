print ('Hello, Django girls')
if 3 > 2: print ('It works!')
if 5 > 2:
    print ('5 is indeed greater than 2')
else:
    print ('5 is not greater than 2')
name = 'Sonja'
if name == 'Ola':
    print ('Hey Ola!')
elif name == 'Sonja':
    print ('Hey Sonja!')
else:
    print ('Hey anonymus!')
volumen = 57
if volumen < 20:
    print ("It's nice for background music")
elif 20 <= volumen < 40:
    print ("Perfecy, I can hear all the datails")
elif 60 <= volumen < 80:
    print ("Nice for parties")
elif 80 <= volumen < 100:
    print ("A bit loud!")
else:
    print ("Me duelen las orejas! :()")
# Cambiar volumen si está muy alto o muy bajo 
if volumen < 20 or volumen > 80:
    print ("Mucho mejor!")

def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi(name):
    if name == 'Ola':
        print ('Hi Ola!')
    elif name == 'Sonja':
        print ('Hi Sonja')
    else:
        print('Hi anonymus!')

hi('Gabriela')

hi("Ola")
hi('Sonja')
def hi(name):
    print ('Hi ' + name + '!')
hi("Rachel")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Gabriela']
for name in girls:
    def hi (name):
        print('Hi '+ name + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Gabriela']
for name in girls:
    hi (name)
    print('Next girl')
for i in range(1, 6):
    print(i)