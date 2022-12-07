#!/bin/python

def getText():
    text = ""
    with open('input.txt') as f:
        text = f.read()
    return text


def getCode(text):
    for index in range(0, len(text)):
        consumed = []
        marker = index+14
        word = text[index:marker]
        for letter in word:
            if(letter in consumed):
                break
            else:
                consumed.append(letter)
        if(len(consumed) == 14):
            return marker
        


def main():
    text = getText()
    msg = getCode(text)
    print(msg)


main()
