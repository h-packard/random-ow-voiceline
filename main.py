# from flask import Flask, request, redirect, render_template, session
# from random import choice
import re
import random

with open('ow-voice-lines.txt','r') as ow:
    lines = ow.read()

words = []
chain = {}
punctuation = ['.','?','!']
character = []
par_reg = r"\(.*\)"


#take out line breaks and append to list
lines = lines.replace('\r',' ').replace('\n',' ')
lines = re.sub(par_reg, '', lines)

new_words = lines.split(' ')
words = words + new_words
#takes out empty strings
words = [i for i in words if i]


for word in words:
    if word[len(word)-1] == ':':
        character.append(word)

corp_len = len(words)
for i,key1 in enumerate(words):
    if corp_len > (i+2):
        key2 = words[i+1]
        word = words[i+2]
        if (key1, key2) not in chain:
            chain[(key1,key2)] = [word]
        else:
            chain[(key1,key2)].append(word)

ow_sent = random.choice(character)
ran_int = random.randrange(0, len(words)-1)
ow_key = (words[ran_int],words[ran_int + 1])
ow_word = ow_sent + ow_key[0] + ' ' + ow_key[1]

while len(ow_sent) < 100:
    ow_word2 = random.choice(chain[ow_key])
    ow_sent += ' ' + ow_word2
    ow_key = (ow_key[1], ow_word2)

if ow_sent[-1] not in punctuation:
    ran_int = random.randrange(0, len(punctuation)-1)
    ow_sent += punctuation[ran_int]

print(ow_sent)
