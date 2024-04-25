import os
import sys
input_path = 'words.txt'
explain = "wordle guesser prints a word and you tell the script of any of the letter are in word or are in the exact place ex: plane\n p -1(isn't in the word) \n p 0(is in the word but in the wrong place)\n p 1(is in the word and the right place)\n if the word is correct write correct"
wrong_letters = {}
right_letters_wrong_position = {}
right_letters_right_position = {}
d = []
def check_input(lists, word, guessed_letters):
    if len(lists) != 2:
        print("wrong input")
        return 0
    if lists[1] == "-1" or lists[1] == "0" or lists[1] == "1":
        if len(lists[0]) != 1:
            print("wrong input")
            return 0   
        if lists[0] in word:
            if(lists[0] in guessed_letters):
                print("letter already mentioned")
                return 0
            else:
                return 1
        else:
            print("wrong input")
            return 0
    print("wrong input")
    return 0


def update_wr_l(letter, word):
    wrong_letters[letter] = 1

def update_wr_wr_p(letter, word):
    if letter in right_letters_wrong_position:
        right_letters_wrong_position[letter] += 1
    else:
        right_letters_wrong_position[letter] = 1

def update_wr_rt_p(letter, word):
    tuples = [letter, 0]
    for i in range(len(word)):
        if letter == word[i]:
            tuples[1] = i
            tuples = tuple(tuples)
            break
    if letter in right_letters_wrong_position:

        right_letters_wrong_position[letter] -=1

        if right_letters_wrong_position[letter] == 0:
            del right_letters_wrong_position[letter]

    if tuples not in right_letters_right_position:
        right_letters_right_position[tuples] = 1
        
def check_wr_l(word):
    for a in word:
        if a in wrong_letters:
            return False
    return True

def check_wr_wr_p(word):
    cor = len(right_letters_wrong_position)
    sol = 0
    for key in right_letters_wrong_position:
        if key in word:
            sol += 1
    if sol == cor:
        return True
    return False

def check_wr_rt_p(word):
    cor = len(right_letters_right_position)
    sol = 0
    for i in range(len(word)):
        tuples = (word[i], i)
        if tuples in right_letters_right_position:
            sol += 1
    if sol == cor:
        return True
    return False





def next_word():
    for a in d:
        if check_wr_l(a) == True and check_wr_wr_p(a) == True and check_wr_rt_p(a) == True:
            return a
    return "no_words"
def wordle():
    
    with open(input_path, 'r') as file:
        for line in file:
            d.append(line)
    
    correct = 0
    word = "plane"
    print(explain)
    while correct == 0:
        
       
        print("I guess the word: " + word)

        k = 0
        print("check word")
        while k < 5:
            guessed_words = ""
            var = input()
            if var == "correct":
                correct = 1
                break
            lists = var.split(" ")
            a = check_input(lists, word, guessed_words)
            if a == 1:
                guessed_words += lists[0]
                types = int(lists[1])
                k += 1
                if types == -1:
                   update_wr_l(lists[0], word)
                if types == 0:
                    update_wr_wr_p(lists[0], word)
                if types == 1:
                    update_wr_rt_p(lists[0], word)
        word = next_word()
        if word == "no_words":
            correct = 1
        
wordle()