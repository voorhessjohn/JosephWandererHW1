import random
main = []
parts = [['verbs', 4],['adjectives', 9], ['animals', 1], ['nouns', 6], ['holidays', 1], ['locations', 2 ], ['body parts', 2 ], ['adverbs', 3]]
item = []
for i in range(len(parts)):
   for j in range(parts[i][1]):  
       item.append(input('Type some ' + str(parts[i][0]) + ':'))
       print('Here\'s your list of ' + str(parts[i][0]) + ':')
       print(item)
   main.append(item)
   item = []


print(main)

v = main[0] #verbs
a = main[1] #adjectives
a2 = main[2] #animals
n = main[3] #nouns
h = main[4] #holidays
l = main[5] #locations
b = main[6] #body parts
a3 = main[7] #adverbs

random.shuffle(v)
random.shuffle(a)
random.shuffle(a2)
random.shuffle(n)
random.shuffle(h)
random.shuffle(l)
random.shuffle(b)
random.shuffle(a3)


print('I want to ' + v[0] + ' you like a ' + a[0] + ' ' + a2[0])
print('None of the ' + a[0] + ' ' + a2[0] + ' that I\'ve encountered in my ' + a[1] + ' life could ever hope to match the ' + n[0] +
      ' of one ' + a[2] +' lady. Well, maybe ' + a[2] + ' isn\'t quite the right word. ' + a[3] + '. That lady was ' + a[3] +
      '. I remember how during Canadian ' + h[0] + ', the most ' + a[4] + ' of occasions, that ' + a[3] + ' lady taught me how to ' + v[0] +
      ' while ' + v[1] + 'ing without making it seem too ' + a[5] + '. Not ' + a3[0] + ', of course, but ' + a3[1] +
      ' nonetheless. There was a contest being held at ' + l[0] + ' for all the ' + n[1] + ' the children had found in ' + l[1] +
      ' since Tuesday. All I needed to do was ' + v[2] + '; ' + v[2] + ' like my ' + n[2] + ' was on the line, because it was. My ' + b[0] +
      ' felt like a ' + n[3] + ' and my ' + b[1] + ' itched ' + a3[2] + '. But then I saw that very ' + a[3] + ', not quite ' + a[2] +
      ' lady ' + v[3] + ', and I felt ' + a[6] + '. The ' + a[7] + ' folk of that ' + a[8] + ' ' + n[4] + ' will forevermore tell tales of the ' + n[5] +
      ' that can appear when a ' + a[3] + ' lady will ' + v[3] + ' and someone like me will, in response, commence to ' + v[2] + ' for the ages.')

#I have hashed out the code above until I change the references from the original lists to the new mutiple-key dictionary.
