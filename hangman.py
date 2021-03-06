def hangman():
    import random
    
    word_list = ['word', 'letter', 'number', 'person', 'pen', 'class',
                 'people', 'sound', 'water', 'side', 'place', 'man', 'men',
                 'woman', 'women', 'boy', 'girl', 'year', 'day', 'week', 'month',
                 'name', 'sentence', 'line', 'air', 'land', 'home', 'hand', 'house',
                 'picture', 'animal', 'mother', 'father', 'brother', 'sister', 'world',
                 'head', 'page', 'country', 'question', 'answer', 'school', 'plant', 'food',
                 'sun', 'state', 'eye', 'city', 'tree', 'farm', 'story', 'sea', 'night', 'day',
                 'life', 'north', 'south', 'east', 'west', 'child', 'children', 'example', 'paper',
                 'music', 'river', 'car', 'foot', 'feet', 'book', 'science', 'room', 'friend', 'idea',
                 'fish', 'mountain', 'horse', 'watch', 'color', 'face', 'wood', 'list', 'bird', 'body',
                 'dog', 'family', 'song', 'door', 'product', 'wind', 'ship', 'area', 'rock', 'order', 'fire',
                 'problem', 'piece', 'top', 'bottom', 'king', 'space']

    stages = ['',
              '--------        ',
              '|       |       ',
              '|       |       ',
              '|       0       ',
              '|      /|)      ',
              '|      //       ',
              '|               '
              ]

    print ('Welcom to Hangman')

    while True:
        word = random.choice(word_list)
        wrong = 0
        rletters = list(word)
        board = ['__']*len(word)
    
        while True:
            if '__' not in board:
                    print(f'\nYou win! It was: {word}')
                    break
            print('\n')
            char = input('Guess a letter: ')
            if char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
                print(' '.join(board))
            elif char == 'hint':
                i = board.index('__')
                char = rletters[i]
                board[i] = char
                rletters[i] = '$'
                print(' '.join(board))
            else:
                wrong += 1
                print(' '.join(board))
                print('\n'.join(stages[:wrong+1]))
                if wrong == len(stages) -1:
                    print(f'You lose! It was: {word}')
                    break

        if input('again? (y/n):') == 'n':
            break
        
hangman()


























































