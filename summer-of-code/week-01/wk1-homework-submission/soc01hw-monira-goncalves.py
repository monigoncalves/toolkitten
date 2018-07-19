## Exercises Day 1

#1 - Hours in a year
print(24*365)

#2 - Minutes in a decade
print(24*365*10*60)

#3 - My age in seconds
print(360*24*365*27)

#4 - Someone aged 48618000s. How old?
print(48618000/(360*24*365))

#5 - 32-bit system. Days to timeout?
print((2**32-1)/100/60/60/24)

#6 - 64-bit system. Days to timeout?
print((2**64-1)/100/60/60/24) 
 

## Exercises Day 3

#greetings

print('Hey')
input()

print('who is there?')
input()
name1 = input('Tell me ya name: ')
name2 = input('Middle name? ')
name3 = input('Surely there is a last name: ')

print('Great meeting you, ' + name1 + str(' ') + name2 + str(' ') + name3 + str('!'))



#better and bigger

print('Hello! Lets play a game')
input()
print('It is called "Tell me your fav number"')
input()

number = input('Say it: ')
number2 = int(number) + 1

print(str(number2) + ' >>> mine is better and bigger than yours!')


# angry boss

print('SAY IT')
angry = input()

print('WHAT DOYA MEAN WITH ' + str(angry) + ' ??? YOU ARE FIIIIIRED!!!')
input()

print('WHAT IS THAT AGAIN?')
angry2 = input()

print('WHAAAT??? ' + str(angry2) + ' ??? YOU ARE FIIIIIRED!!!')



# table of content
print('Hello! How may I help you?')
find = input('What topic are you looking for?')

print(str(find) + ' is at Chapter 4, page 267')
