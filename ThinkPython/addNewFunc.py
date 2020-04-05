#
# addNewFunc.py
# @author bulbasaur
# @description 
# @created 2020-03-15T16:46:35.109Z+08:00
# @last-modified 2020-03-15T16:55:06.980Z+08:00
#

# Defination of the function named print_lyrics
def print_lyrics():  # the () in none, because this func does not accept any arguments
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# Call func
print_lyrics()


# Repeat the func in a new func
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# Call the new func
repeat_lyrics()