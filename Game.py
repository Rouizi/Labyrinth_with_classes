import os
from robot import Robot


def main():
    robot = Robot()

    continue_part = True
    while continue_part:
        print("Existing labyrinths :")
        for i, name_file in enumerate(os.listdir("maps")):
            if name_file.endswith(".txt"):
                print(f"  {i + 1} - {name_file[:-4]}")
            if name_file == 'labyrinth':
                print(f"  {i + 1} - continue part")

        choix_labyrinth = True
        while choix_labyrinth:
            robot.choose_number()
            robot.display_labyrinth()
            robot.check_direction()
            choix_labyrinth = False
            continue_part = False


main()
