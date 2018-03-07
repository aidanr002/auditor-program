sourcelist = []
f = open('words.txt','r')
opened_file = f
for word in opened_file:
    word = word.strip()
    word = word.lower()
    sourcelist.append(word)
f.close()
inputlist = []
user = input("Enter item: ")
while user:
    inputlist.append(user)
    user = input("Enter item: ")
print ('Not Found:')
for item in sourcelist:
    if item not in inputlist:
        print (item)
print ('Error - Not on list:')
for item in inputlist:
    if item not in sourcelist:
        print (item)

while 1==1:
    user = input('Enter command: ')
    if user == 'exit':
        exit()
