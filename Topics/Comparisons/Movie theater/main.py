number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())
if capacity * number_of_halls >= number_of_viewers:
    print("True")
else:
    print("False")