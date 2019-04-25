import os
import pickle


class Labyrinth:
    def __init__(self):
        self.robot = 'X'
        self.door = 'U'
        self.Labyrinth = []
        self.map = 'maps\\facile.txt'


    def labyrinth(self, file):
        self.Labyrinth = []
        with open(file, 'r') as a_map:
            for line in a_map:
                liste = line.strip()
                self.Labyrinth.append(list(liste))
        return self.Labyrinth

    def display_labyrinth(self):
        for line in self.Labyrinth:
            print(''.join(line))

    def save_part(self):
        with open(os.getcwd() + '\\maps\\labyrinth', "wb") as file_labyrinth:
            my_pickler = pickle.Pickler(file_labyrinth)
            my_pickler.dump(self.Labyrinth)

    def choose_number(self):
        number = input('Enter a labyrinth number to start playing: ')

        try:
            number = int(number)
            D = {}
            for i, name_file in enumerate(os.listdir("maps")):
                if name_file.endswith(".txt"):
                    chemin = os.path.join("maps", name_file)
                    D[i + 1] = chemin
            if "labyrinth" in os.listdir("maps"):
                if number > len(D) + 1:
                    print("You entered an invalid number")
                    return self.choose_number()
            else:
                if number > len(D):
                    print("You entered an invalid number")
                    return self.choose_number()
            if number <= 0:
                print("You entered an invalid number")
                return self.choose_number()
        except ValueError:
            print("You have not entered a number")
            return self.choose_number()
        if number in D.keys():
            self.map = D[number]
            self.Labyrinth = self.labyrinth(self.map)
        else:
            with open(os.getcwd() + '\\maps\\labyrinth', 'rb') as file:
                my_depickler = pickle.Unpickler(file)
                self.Labyrinth = my_depickler.load()

    def position_robot(self, wanted, Labyrinth):
        for index_line, line in enumerate(Labyrinth):
            for index_column, column in enumerate(line):
                if column == wanted:
                    l, c = index_line, index_column
        return l, c

    def labyrinth_without_robot(self, robot):
        for index_line, line in enumerate(self.labyrinth(self.map)):
            for index_column, column in enumerate(line):
                if column == robot:
                    self.Labyrinth[index_line][index_column] = ' '
        return self.Labyrinth