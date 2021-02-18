from enum import Enum
import unittest

class TicTacToe:
	#diagonal locations represent pairs of row/col locations on the board whose insertion could possibly result in a diagonal victory
	#this is declared private/static: I do not want some user being able to access this and modify it, and the locations of diagonal victory
	#spots remains the same throughout all instantiantions of the object. Therefore it's declared static as well
	__diagonal_locations=[[0,0],[0,2],[1,1],[2,0],[2,2]]
	#IllegalStateCall custom Exception:
		#this exception is called when a user attempts to call change_first_turn() after some move or moves have already been made
		#prints out message alerting user this is an illegal call to make and prints message of how many game moves have been made thus far
	class IllegalStateCall(Exception):
		def __init__(self,num_moves):
			self.num_moves=num_moves
			self.err="You can only make a call to change_first_turn() when no moves have yet been made. Total moves made so far is " + str(self.num_moves)
			super().__init__(self.err)
	#IllegalCallToPlaceMarker custom Exception:
		#is called when someone attempts to a place an x/o on the board in a spot where a symbol already exists
	class IllegalCallToPlaceMarker(Exception):
		def __init__(self,row,col,board):
			self.err="You are attempting to insert into a board space that has already been filled. Board index " + str(row)+","+str(col)+" contains value " + board[row][col]
			super().__init__(self.err)
	#IllegalMoveWhenGameHasEnded custom Exception:
		#is raised when a user attempots to make place a symbol on the board when the game has already ended
	class IllegalMoveWhenGameHasEnded(Exception):
		def __init__(self):
			self.err="You are attempting to make another move when the game has ended. Better luck next time but no more moves are permitted!"
			super().__init__(self.err)
	#enum class for states game can end
	#the end state instance variable is set to the enum value NO_RESOLUTION until the game has ended
	class END_STATES(Enum):
		NO_RESOLUTION=1
		DRAW = 2
		CROSS_WON = 3
		NAUGHT_WON = 4
	#MOVE_STATES is an enum class of the state of the game either being in a turn for the Crosses or naughts.
	class MOVE_STATES(Enum):
		CROSS_TURN = 0
		NAUGHT_TURN = 1
	#constructor:
			#instantiantes instancce variables naught moves, cross_moves, total_game_moves which keep of respective number of moves for naughts, crosses, and the overall game
			#game state is by default set to having crosses go first. If you'd like to change it, you can do so with change_first_turn
			#end state is set to NO_RESOLUTION since the game just started and has not yet had an outcome
			#playing_board: A 3x3 2D array which is instantiated to be all zero's 
	def __init__(self):
		self.__naught_moves=0
		self.__cross_moves=0
		self.__total_game_moves=0
		#By default, the game state is set to crosses going first. This can be altered in the first move state
		self.__game_state=self.MOVE_STATES.CROSS_TURN
		#the end state of the game is set to NO RESOLUTION until we have a winner or a draw
		self.__end_state=self.END_STATES.NO_RESOLUTION
		self.__playing_board=[[0 for i in range(3)] for j in range(3)]

	#getter methods for various instance variables. Comes in handy later on for unit testing
	def get_game_state(self):
		return self.__game_state

	def get_playing_board(self):
		return self.__playing_board

	def get_end_state(self):
		return self.__end_state


	#changes the state of the first turn to be set instead to NAUGHT_TURN, giving the first move to naughts and not crosses	
	def change_first_turn(self):
		if (self.__total_game_moves!=0):
			raise self.IllegalStateCall(self.__total_game_moves)
		else:
			self.__game_state=self.MOVE_STATES.NAUGHT_TURN

	#print each of the rows of the playing board member attribute. Printing is prettier this way;gives the array the appearance of an actual 3x3 board
	def print_playing_board(self,move_num):
		print("Playing board after move" + " " + str(move_num) + " " + "now looks like:")
		for i in range(0,len(self.__playing_board)):
			print(self.__playing_board[i])
		print('\n')
	
	#horizontal win: Takes in as parameters the symbol (either cross/naught),playing board, and the row/column symbol exists at
	#we have achieved a horizontal win state if the rest of the row the symbol exists at is filled by the same symbol
	#I check this by having a counter variable that increments every time a matching symbol is found
	#I loop through each of the columns in the row the symbol exists at- therefore, if our counter variable equals 3 by the end, and 
	#we know the TicTacToe board has 3 columns/3 rows, it means every column in the row has the same symbol, indicating a horizontal win state
	def horizontal_win(self,symbol,board,row,column):
			counter=0
			for value in range(0,len(board[0])):
				if board[row][value]==symbol:
					counter+=1
				else:
					return False
			if symbol=='x' and counter==3:
					self.__end_state=self.END_STATES.CROSS_WON
					print("Game over. Crosses win by measure of a horizontal victory")
					return True
			elif symbol=='o' and counter==3:
				self.__end_state=self.END_STATES.NAUGHT_WON
				print("Game over. Naughts win by measure of a horizontal victory")
				return True

	#vertical win: Takes in as parameters the symbol (either cross/naught),playing board, and the row/column symbol exists at
	#we have achieved a vertical win state if all of the rows the column in which the symbol exists at are the same symbol
	#I check this by having a counter variable that increments every time a matching symbol is found
	#I loop through each of the rows with the column value the symbol exists at- therefore, if our counter variable equals 3 by the end, and 
	#we know the TicTacToe board has 3 columns/3 rows, it means every column in the row has the same symbol, indicating a vertical win state

	def vertical_win(self,symbol,board,row,column):
		counter=0
		for val in range(0,len(board)):
			if board[val][column]==symbol:
				counter+=1
			else:
				return False
			if symbol=='x' and counter==3:
				self.__end_state=self.END_STATES.CROSS_WON
				print("Game over. Crosses win by measure of a vertical victory")
				return True
			elif symbol=='o' and counter==3:
				self.__end_state=self.END_STATES.NAUGHT_WON
				print("Game over. Naughts win by measure of a vertical victory")
				return True

	#diagonal win state checker: This win state is more complex than the horizontal/vertical win states
	#Diagonal win states can be achieved from an insertion at the locations in the __diagonal_locations static class attribute
	#In other words, it is only worth our time to check for a diagonal win state if the last insertion was at one of these locations
	#I have commented further within the method to explain these possible cases
	def diagonal_win(self,symbol,board,row,column):
		counter=0
		pair=[row,column]
		for location in range(0,len(self.__diagonal_locations)):
			if (pair==self.__diagonal_locations[location]):
				#if board location is (2,2), we could have an downwards right diagonal and must check locations (1,1) and (0,0)
				if (pair==[2,2] and symbol=="x"):
					if (board[row-1][column-1]==symbol and board[row-2][column-2]==symbol):
						print("Diagonal cross victory has been reached. Game over")
						self.__end_state=self.END_STATES.CROSS_WON
						return True
					else:
						return False
				elif (pair==[2,2] and symbol=="o"):
					if (board[row-1][column-1]==symbol and board[row-2][column-2]==symbol):
						print("Diagonal nought victory has been reached. Game over")
						self.__end_state=self.END_STATES.NAUGHT_WON 
						return True
					else:
						return False
				elif (pair==[0,0] and symbol=="x"):
					#if board location is (0,0), we could have a downwards facing left diagonal, and must check locations (1,1) and (2,2)
					if (board[row+1][column+1]==symbol and board[row+2][column+2]==symbol):
						print("Diagonal cross victory has been reached. Game over")
						self.__end_state=self.END_STATES.CROSS_WON 
						return True
					else:
						return False
				elif (pair==[0,0] and symbol=="o"):
					if (board[row+1][column+1]==symbol and board[row+2][column+2]==symbol):
						print("Diagonal nought victory has been reached. Game over")
						self.__end_state=self.END_STATES.NAUGHT_WON 
						return True
					else:
						return False
				elif (pair==[2,0] and symbol=="o"):
					#if diagonal location is (2,0), we could have a downwards facing left diagonal, and must check locations (1,1) and (0,2)
					if (board[row-1][column+1]==symbol and board[row-2][column+2]==symbol):
						print("Diagonal nought victory has been reached. Game over")
						self.__end_state=self.END_STATES.NAUGHT_WON 
						return True
					else:
						return False
				elif (pair==[2,0] and symbol=="x"):
					if (board[row-1][column+1]==symbol and board[row-2][column+2]==symbol):
						print("Diagonal cross victory has been reached. Game over")
						self.__end_state=self.END_STATES.CROSS_WON 
						return True
					else:
						return False
				elif (pair==[0,2] and symbol=="x"):
					#if diagonal location is (0,2), we could have an upwards facing right diagonal, and must check locations (1,1) and (2,0)
					if (board[row+1][column-1]==symbol and board[row+2][column-2]==symbol):
						print("Diagonal cross victory has been reached. Game over")
						self.__end_state=self.END_STATES.CROSS_WON 
						return True
					else:
						return False
				elif (pair==[0,2] and symbol=="o"):
					if (board[row+1][column-1]==symbol and board[row+2][column-2]==symbol):
						print("Diagonal naught victory has been reached. Game over")
						self.__end_state=self.END_STATES.NAUGHT_WON 
						return True
					else:
						return False

				#location (1,1) must exist in any diagonal, and could be a part of a left/right diagonal
				#There we must have two nested elifs inside of the outermost if checking to see if the left/right diagonal case exists for an insertion at (1,1)
				elif (pair==[1,1] and symbol=="x"):
					if (board[row+1][column+1]==symbol and board[row-1][column-1]==symbol):
						print("Diagonal cross victory has been reached. Game over.")
						self.__end_state=self.END_STATES.CROSS_WON
						return True
					elif (board[row-1][column+1]==symbol and board[row+1][column-1]==symbol):
						print("Diagonal cross victory has been reached. Game over.")
						self.__end_state=self.END_STATES.CROSS_WON
						return True

					else:
						return False
				#accounts for a diagonal win where final insertion is (1,1) and other two points are (0,2) and (2,0)

				elif (pair==[1,1] and symbol=="o"):
					if (board[row+1][column+1]==symbol and board[row-1][column-1]==symbol):
						print("Diagonal naught victory has been reached. Game over.")
						self.__end_state=self.END_STATES.NAUGHT_WON
						return True
					elif ((board[row-1][column+1]==symbol) and (board[row+1][column-1]==symbol)):
						self.__end_state=self.END_STATES.NAUGHT_WON
						print("Diagonal naught victory has now been reached. Game over")
						return True

					else:
						return False

	#checks if game has ended in a tie
	#We have a space constraint of (nn), or in this case (3x3), so there's only 9 possible slots/moves to make on the board
	#If our end state is still set to NO_RESOLUTION, and 9 moves have been made, our game has ended in a tie
	#end_state is set to END_STATES.DRAW
	def check_tie(self):
		if (self.__total_game_moves==9 and self.__end_state==self.END_STATES.NO_RESOLUTION):
			print("The game has ended with no winner and in a tie")
			self.__end_state=self.END_STATES.DRAW
			return True
		else:
			return False

	#check resolution:
		#simply checks if the game has reached a resolution: draw, cross win, or naught win
	def check_resolution(self,symbol,board,row,column):
		if self.vertical_win(symbol,board,row,column)==True or self.horizontal_win(symbol,board,row,column)==True or self.diagonal_win(symbol,board,row,column) or self.check_tie():
			return True
		else:
			return False

	#place_marker: takes in symbol, row, and column
	#The first thing I do in this method is to check for various illegal inputs (illegal insertions, inserting when game has ended, row/col is out of scope, symbol doesn't match whose turn it is)
	def place_marker(self,symbol,row,column):
		if (row > 2) or (column > 2):
			raise ValueError("The scope of the board is between 0 and 2 for both row and column values")
		elif (row < 0) or (column < 0):
			raise ValueError("The scope of the board is between 0 and 2 for both row and column values")
		elif (self.__game_state is self.MOVE_STATES.CROSS_TURN and symbol!="x"):
			raise ValueError("Currently it is the cross turn. Please pass the symbol argument to be 'x'")
		elif (self.__game_state is self.MOVE_STATES.NAUGHT_TURN and symbol!="o"):
			raise ValueError("Currently it is the nought turn. Please pass the symbol argument to be 'o'")
		elif (self.__playing_board[row][column]!=0):
			 val=self.__playing_board[row][column]
			 raise ValueError("You are attempting to insert at a location that already has a symbol")
		elif (self.__end_state!=self.__end_state.NO_RESOLUTION):
			raise IllegalMoveWhenGameHasEnded()
		else:
			#if we have no exceptions that have been raised, place symbol in board[row][column] location, increment counter instance variable
			#for that respective symbol # of moves, and change the state to the opposite symbol turn
			if (symbol=="x"):
				self.__cross_moves+=1
				self.__game_state=self.MOVE_STATES.NAUGHT_TURN
			elif (symbol=="o"):
				self.__naught_moves+=1
				self.__game_state=self.MOVE_STATES.CROSS_TURN
			self.__playing_board[row][column]=symbol
			self.__total_game_moves+=1

		#print the playing board after a move is made (helpful to see intermediate steps of the game)
		self.print_playing_board(self.__total_game_moves)
		#The min # of moves that can be made to reach victory is 4, since the minumum #of moves for any symbol to reach victory is 3
		#Therefore after 3 moves have been made, I can begin to check if the insertion that has just been made causes check_resolution to trigger as true
		#this indicates the game has ended
		if (self.__total_game_moves>3):
			if (self.check_resolution(symbol,self.__playing_board,row,column))==True:
				print("Thanks for playing!")
	
