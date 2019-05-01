# Univs = []
# Techs = ["MIT","CalTech"]
# Ivys = ["Harvard","Yale","Brown"]
#
# Univs.append(Techs)
# print("Univs = " + str(Univs))
#
# Univs.append(Ivys)
# print("Univs = " + str(Univs))

L1 =  [2]
x = 2
L2 = [L1,L1]
L2 = [x,x]
print("L2 = " + str(L2))

L1[0] = 3
x = 3
print("L2 = " + str(L2))

L2[0] = "a"
print("L2 = " + str(L2))

L1 = [2]
print("L2 = " + str(L2))

# def copy_list(l_source,l_dest):
#     for e in l_source:
#         l_dest.append(e)
#         print("l_dest " + str(l_dest))
#
# L1 = [1,2,3]
# L2 = []
#
# copy_list(L1,L1)
#
# print("L2 " + str(L2))

# EtoF = {'bread': 'du pain', 'wine': 'du vin',\
#        'eats': 'mange', 'drinks': 'bois',\
#        'likes': 'aime', 1: 'un',\
#        '6.00':'6.00'}
#
# def translate_word(word,dictionary):
#     if word in dictionary:
#         return dictionary[word]
#     else:
#         return word
#
# def translate_sentence(sentence):
#     translated_sentence = ''
#     word = ''
#     for c in sentence:
#         if c != ' ':
#             word += c
#         else:
#             translated_sentence  += ' ' + translate_word(word,EtoF)
#             word = ''
#
#     return translated_sentence[1:]  + " " +  translate_word(word,EtoF)
#
# print(translate_sentence('John eats bread'))

# l = [1,2,3,4]
# a = 5
#
# def change_list(input_list,i,e):
#     input_list[i] = e
#
# change_list(l,1,100)
#
# print(l)
#
#
# def change_value(input_var,new_value):
#     inpur_var = new_value
#
# change_value(a,20)
#
# print(a)
