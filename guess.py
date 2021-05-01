# Guessing Game
import random

# Guess Game


def guess_game(limit, number):
     random_number = random.randint(1, number)
    try:
        while limit > 0:
            guess = int(input('What is your guess'))
            limit -= 1
            if random_number == guess:
                print('You got it right!')
                break
            elif guess > number:
                print('Guess is out of range')
                print(f'You have {limit} guess(es) left')
            else:
                print('That was wrong')
                print(f'You have {limit} guess(es) left')
        print('Game over')
        print(f'The random number was {random_number}')

def easy():


def medium():


def hard():


def try_again():


def welcome():
