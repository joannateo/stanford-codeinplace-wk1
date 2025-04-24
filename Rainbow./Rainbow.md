Make Karel paint a rainbow! Karel will start in the left corner of a world with 1 row and 6 columns, like so:



Karel should paint the squares with, in order: the colors "red" , "orange", "yellow", "green", and "blue", and then Karel should move to end in the rightmost spot. The result should look like this:





Did you know that Karel can paint a corner? Call paint_corner and pass in the color you want, in quotes:

def main():
    paint_corner('red')
    move()
    paint_corner('orange')



What colors does Karel know? So many! In fact any "html" color will work. Here is a link with a few:

https://htmlcolorcodes.com/color-names/
