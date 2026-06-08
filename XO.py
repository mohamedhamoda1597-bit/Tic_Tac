import os
def clear():
    os.system("cls")
class Player :
    def __init__(self):
        self.name = ""
        self.sympol = ""
    def choose_player(self):
       while True :
           name = input("Entre your Name(Entre only letter) : ").capitalize()
           if name.isalpha() :
               self.name = name 
               break
           else :
               print("Invalid name Entre again")
       return self.name
    def choose_Sympol(self):  
        while True :
            sympol = input("Entre your sympol(Entre one letter) : ").title()
            if sympol.isalpha() and len(sympol)==1 :
                self.sympol = sympol
                break
            else :
                print("Invalid Sympol Entre again")
        return sympol
class Menu :
    def display_menu_start(self):
        message = """
hello in game choice num of(1 , 2 ):
1.Start 
2.Quite : 
"""
        choice = input(message)
        return choice
    def display_menu_end(self):
        message = """
end game choice num of(1 , 2 ):
1.restart 
2.Quite : 
"""
        choice = input(message)
        return choice
class Board :
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i < 6 :
                print("-" * 5)
    def update_board(self,choice,sympol):
        if self.is_valid_move(choice):
            self.board[choice-1]= sympol
            return True
        return False
    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
    def restart_board(self):
        self.board = [str(i) for i in range(1,10)]
class Game :
   def __init__(self):
       self.player = [Player(),Player()]
       self.board = Board()
       self.menu = Menu()
       self.current_player_index = 0
   def start_game(self):
      choice = self.menu.display_menu_start()
      if choice == "1" :
          self.set_up_player()
          self.play_game()
      else :
          self.quite_game()
   def set_up_player(self):
       for num,player in enumerate(self.player,start=1):
           print(f"player {num} ,entre your details ")
           player.choose_player()
           player.choose_Sympol()
           clear()
   def play_game(self):
       while True :
           self.turn_game()
           if self.check_win() or self.check_draw() :
               self.check()
               self.quite_game()
               break
       choice = self.menu.display_menu_end()
       if choice == "1":
            self.restart_game()
       else :
            self.quite_game()
   def restart_game(self):
     self.board.restart_board()
     self.current_player_index = 0
     self.play_game()
   def check(self):
       player = self.player[self.current_player_index]
       if self.check_win():
           print(f"{player.name} is win ")
       if self.check_draw() :
           print("draw")
   def turn_game(self):
       clear()
       player = self.player[self.current_player_index]
       self.board.display_board()
       print(f"{player.name} 's turn ,{player.sympol}")
       while True:
         try:
            choice_cell = int(input("Entre num (1 , 9): "))
            if 1<= choice_cell <= 9 and self.board.update_board(choice_cell,player.sympol):
               break
            else: 
                print("Invaild value , try again ")
         except ValueError:
           print("Invalid value, try again ")
       if not self.check_win():
         self.switch_player()
   def switch_player(self):
       self.current_player_index = 1 - self.current_player_index
   def check_win(self) :
       win_combinatios = [
         [0,1,2],[3,4,5],[6,7,8],
         [0,3,6],[1,4,7],[2,5,8],
         [0,4,8],[2,4,6]
       ]
       for comb in win_combinatios:
           if self.board.board[comb[0]]== self.board.board[comb[1]]==self.board.board[comb[2]] and not self.board.board[comb[0]].isdigit():
               return True
       return False
   def check_draw(self):
       return all(not cell.isdigit() for cell in self.board.board )
   def quite_game(self):
       print("Game over ...")
game = Game()
game.start_game()

