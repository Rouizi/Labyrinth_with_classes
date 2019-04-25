from labyrinth import Labyrinth

class Robot(Labyrinth):
    def __init__(self):
        super(Robot, self).__init__()
        self.direction = 'E'
        self.n = 1

    def choose_direction(self):
        self.direction = input('Enter an order: N(North), S(South), E(East), W(West),'
                          ' Q(save and quit): ')
        if len(self.direction) > 2 or self.direction == '' or self.direction == ' ' or self.direction == '  ':
            print("You have not entered a valid order")
            return self.choose_direction()
        if len(self.direction) == 1:
            if not self.direction.isalpha():
                print("You did not enter a letter")
                return self.choose_direction()
            else:
                self.direction = self.direction.upper()
                self.n = 1
                return self.direction
        if len(self.direction) == 2:
            if not self.direction[0].isalpha():
                print("You did not enter a letter")
                return self.choose_direction()
            elif self.direction[1].isalpha():
                print("You have entered several letters")
                return self.choose_direction()
            else:
                self.direction = self.direction[0].upper() + self.direction[1]
                self.n = int(self.direction[1])
                return self.direction

    def check_direction(self):
        displacement = True
        while displacement:
            self.choose_direction()
            line, column = self.position_robot(self.robot, self.Labyrinth)
            line_p, column_p = self.position_robot(self.door, self.Labyrinth)
            if self.direction[0] == 'E':
                if self.n > len(self.Labyrinth[line]) - column - 1:
                    print("You can not do this")
                    continue
                liste_du_parcour = []
                for i in range(self.n + 1):
                    liste_du_parcour.append(self.Labyrinth[line][column + i])
                if 'O' in liste_du_parcour:
                    print("You can not do this, there is a wall")
                    continue
                else:
                    self.Labyrinth = self.labyrinth_without_robot(self.robot)
                    self.Labyrinth[line][column + self.n] = 'X'
                    self.display_labyrinth()

            elif self.direction[0] == 'W':
                if self.n > column:
                    print("You can not do this")
                    continue
                liste_du_parcour = []
                for i in range(self.n + 1):
                    liste_du_parcour.append(self.Labyrinth[line][column - i])
                if 'O' in liste_du_parcour:
                    print("You can not do this, there is a wall")
                    continue
                else:
                    self.Labyrinth = self.labyrinth_without_robot(self.robot)
                    self.Labyrinth[line][column - self.n] = 'X'
                    self.display_labyrinth()
            elif self.direction[0] == 'N':
                if self.n > line:
                    print("You can not do this")
                    continue
                liste_du_parcour = []
                for i in range(self.n + 1):
                    liste_du_parcour.append(self.Labyrinth[line - i][column])
                if 'O' in liste_du_parcour:
                    print("You can not do this, there is a wall")
                    continue
                else:
                    self.Labyrinth = self.labyrinth_without_robot(self.robot)
                    self.Labyrinth[line - self.n][column] = 'X'
                    self.display_labyrinth()
            elif self.direction[0] == 'S':
                if self.n > len(self.Labyrinth) - line - 1:
                    print("You can not do this")
                    continue
                liste_du_parcour = []
                for i in range(self.n + 1):
                    liste_du_parcour.append(self.Labyrinth[line + i][column])
                if 'O' in liste_du_parcour:
                    print("You can not do this, there is a wall")
                    continue
                else:
                    self.labyrinth_without_robot(self.robot)
                    self.Labyrinth[line + self.n][column] = 'X'
                    self.display_labyrinth()
            elif len(self.direction) == 2 and self.direction[0] == 'Q':
                print("You have not entered a valid order")
            elif len(self.direction) == 1 and self.direction == "Q":
                print("You have save and leave the game")
                self.save_part()
                displacement = False
            else:
                print("You entered a wrong letter")
                continue
            line, column = self.position_robot(self.robot, self.Labyrinth)
            if line == line_p and column == column_p:
                print("CONGRATULATIONS you win !!!")
                displacement = False