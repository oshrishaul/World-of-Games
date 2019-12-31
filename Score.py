import os
from Utils import file_name

"""""""""
- The function will try to read the current score in the scores file
- if it fails it will create a new one and will use it to save the current score.  
 - The function will print the user current score. 
 - Amount of poimants for winning a game is = 1 point per difficulty level (difficulty 3 = 3 points). 
- Each time the user is winning a game, the points he won will be added to his current amount of point saved in a file.   
- file_name() call the right file to read and write the score (Utils.py)
"""""""""


def add_score(difficulty):
    try:
        file_name() # get the file from Utils.py --> file_name()
        if os.path.isfile(file_name()) is False:
            my_file = open(file_name(), 'w+', encoding='utf-8')
            difficulty = str(difficulty)
            my_file.write(difficulty)
            print("Congratulations, you've earned", difficulty, "Points")
            my_file.close()
        else:
            my_file=open(file_name(), 'r+', encoding='utf-8')
            points = my_file.read()
            points = int(points)
            points = difficulty + points
            points = str(points)
            my_file.seek(0)
            my_file.write(points)
            print("Congratulations, you've earned ", difficulty, " Points. now you have", points, " points.")
            my_file.close()

    except ValueError or IOError as e:
        print("ERROR:", e)

