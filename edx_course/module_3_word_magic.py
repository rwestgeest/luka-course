def word_mixer(listt):
    listt.sort()
    new_word=[]
    while len(listt)>5:
        new_word.append(listt.pop(-5))
        new_word.append(listt.pop(0))
        new_word.append(listt.pop(-1))
    return(new_word)

words_list=lala.split()
for i in range(len(words_list)):
    word=words_list[i]
    if len(word) <= 3:
        words_list[i]=word.lower()
    elif len(word) >=7:
        words_list[i]=word.upper()

print(word_mixer(words_list))