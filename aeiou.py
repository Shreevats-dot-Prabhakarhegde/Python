import random
char_list=['a','e','i','o','u']
random.shuffle(char_list)# every time changes (bcz string operation)
print(''.join(char_list))#Concatenate any number of strings