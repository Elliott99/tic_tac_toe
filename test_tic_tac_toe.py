from tictactoe import *
import unittest

class TestingTicTacToeMethods(unittest.TestCase):
	
	#tests the change_first_turn() call
	#this should fail: In one TicTacToe instance I have changed the first move state, in another instance 
	#I have not changed the first move state 
	def test_change_first_move(self):
		t=TicTacToe()
		t.change_first_turn()
		game_state=t.get_game_state()
		t_2=TicTacToe()
		game_state_2=t_2.get_game_state()
		self.assertEqual(game_state,game_state_2)

	#checks case of placing a singular cross, then ensures what exists on that inserted cross spot is that cross
	def test_place_marker_1(self):
		print('\n')
		print("Test_place_marker_1 board:")
		t1=TicTacToe()
		t1.place_marker("x",0,0)
		board=t1.get_playing_board()
		value=board[0][0]
		self.assertEqual("x",value)

	#checks case of placing a singular naught, then ensures that what exists on the inserted board spot is that naught
	def test_place_marker_2(self):
		print('\n')
		print("Test_place_marker_2 board: ")
		t2=TicTacToe()
		t2.change_first_turn()
		t2.place_marker("o",1,1)
		board_2=t2.get_playing_board()
		value=board_2[1][1]
		self.assertEqual("o",value)

	#check for a game state in which a horizontal victory is achieved by crosses
	def test_horizontal_cross_victory(self):
		print('\n')
		print("Test_horizontal_cross_victory board:")
		t3=TicTacToe()
		t3.place_marker("x",0,0)
		t3.place_marker("o",2,2)
		t3.place_marker("x",0,1)
		t3.place_marker("o",2,1)
		t3.place_marker("x",0,2)
		end_state=t3.get_end_state()
		self.assertEqual(end_state,t3.END_STATES.CROSS_WON)

	#check for the case of a game in which naughts win by means of a horizontal victory
	def test_horizontal_naught_victory(self):
		print('\n')
		print("Test_horizontal_naught_victory board:")
		t3=TicTacToe()
		t3.place_marker("x",2,2)
		t3.place_marker("o",0,0)
		t3.place_marker("x",1,1)
		t3.place_marker("o",0,1)
		t3.place_marker("x",2,0)
		t3.place_marker("o",0,2)
		end_state=t3.get_end_state()
		self.assertEqual(end_state,t3.END_STATES.NAUGHT_WON)


	#check for the case of a game in which crosses win by a means of a vertical victory
	def test_verical_cross_victory(self):
		print('\n')
		print("Test_vertical_cross_victory board:")
		t3=TicTacToe()
		t3.place_marker("x",0,0)
		t3.place_marker("o",2,2)
		t3.place_marker("x",1,0)
		t3.place_marker("o",2,1)
		t3.place_marker("x",2,0)
		end_state=t3.get_end_state()
		self.assertEqual(end_state,t3.END_STATES.CROSS_WON)

	#checks for the case of a game in which naughts win by a means of a vertical victory
	def test_vertical_naught_victory(self):
		print('\n')
		print("Test_vertical_naught_victory board:")
		t3=TicTacToe()
		t3.place_marker("x",2,2)
		t3.place_marker("o",0,0)
		t3.place_marker("x",2,1)
		t3.place_marker("o",1,0)
		t3.place_marker("x",1,2)
		t3.place_marker("o",2,0)
		end_state=t3.get_end_state()
		self.assertEqual(end_state,t3.END_STATES.NAUGHT_WON)

	#checks for the case of a game in which crosses win by means of a diagonal victory ending with a final move at (0,0)
	def test_diagonal_cross_victory_1(self):
		t4=TicTacToe()
		print('\n')
		print("test_diagonal_cross_victory_1 board:")
		t4.place_marker("x",2,2)
		t4.place_marker("o",1,0)
		t4.place_marker("x",1,1)
		t4.place_marker("o",1,2)
		t4.place_marker("x",0,0)
		end_state=t4.get_end_state()
		self.assertEqual(end_state,t4.END_STATES.CROSS_WON)

	#tests for case of a game in which naughts win by means of a diagonal victory ending with a final move at (0,0)
	def test_diagonal_naught_victory_1(self):
		t5=TicTacToe()
		print('\n')
		print("test_diagonal_naught_victory_1 board:")
		t5.place_marker("x",1,0)
		t5.place_marker("o",2,2)
		t5.place_marker("x",1,2)
		t5.place_marker("o",1,1)
		t5.place_marker("x",2,1)
		t5.place_marker("o",0,0)
		end_state=t5.get_end_state()
		self.assertEqual(end_state,t5.END_STATES.NAUGHT_WON)

	#tests for case of a game in which crosses win by means of a diagonal vcitory with a final move at (2,2)
	def test_diagonal_cross_victory_2(self):
		t6=TicTacToe()
		print('\n')
		print("test_diagonal_cross_victory_2 board:")
		t6.place_marker("x",0,0)
		t6.place_marker("o",1,2)
		t6.place_marker("x",1,1)
		t6.place_marker("o",1,0)
		t6.place_marker("x",2,2)
		end_state=t6.get_end_state()
		self.assertEqual(end_state,t6.END_STATES.CROSS_WON)

	#test for case of a game in which naughts win by means of a diagonal victory with a final move at (2,2)
	def test_diagonal_naught_victory_2(self):
		t7=TicTacToe()
		print('\n')
		print("test_diagonal_naught_victory_2 board:")
		t7.place_marker("x",1,2)
		t7.place_marker("o",0,0)
		t7.place_marker("x",1,0)
		t7.place_marker("o",1,1)
		t7.place_marker("x",2,0)
		t7.place_marker("o",2,2)
		end_state=t7.get_end_state()
		self.assertEqual(end_state,t7.END_STATES.NAUGHT_WON)

	#tests for case of a game in which crosses win by means of a diagonal victory with a final move at (0,2)
	def test_diagonal_cross_victory_3(self):
		t8=TicTacToe()
		print('\n')
		print("test_diagonal_cross_victory_3 board:")
		t8.place_marker("x",2,0)
		t8.place_marker("o",0,0)
		t8.place_marker("x",1,1)
		t8.place_marker("o",1,2)
		t8.place_marker("x",0,2)
		end_state=t8.get_end_state()
		self.assertEqual(end_state,t8.END_STATES.CROSS_WON)

	#tests for case of a game in which naughts win by means of a diagonal victory with a final move at (0,2)
	def test_diagonal_naught_victory_3(self):
		t9=TicTacToe()
		print('\n')
		print("test_diagonal_naught_victory_3 board:")
		t9.place_marker("x",0,0)
		t9.place_marker("o",2,0)
		t9.place_marker("x",1,2)
		t9.place_marker("o",1,1)
		t9.place_marker("x",0,1)
		t9.place_marker("o",0,2)
		end_state=t9.get_end_state()
		self.assertEqual(end_state,t9.END_STATES.NAUGHT_WON)

	#tests for case of a game in which crosses win by a means of a diagonal victory with a final move at (2,0)
	def test_diagonal_cross_victory_4(self):
		t10=TicTacToe()
		print('\n')
		print("test_diagonal_cross_victory_4 board:")
		t10.place_marker("x",0,2)
		t10.place_marker("o",1,2)
		t10.place_marker("x",1,1)
		t10.place_marker("o",0,0)
		t10.place_marker("x",2,0)
		end_state=t10.get_end_state()
		self.assertEqual(end_state,t10.END_STATES.CROSS_WON)

	#tests for case of a diagonal naught victory in which the final winning move is a naught placed at (2,0)
	def test_diagonal_naught_victory_4(self):
		t11=TicTacToe()
		print('\n')
		print("test_diagonal_naught_victory_4 board:")
		t11.place_marker("x",1,2)
		t11.place_marker("o",0,2)
		t11.place_marker("x",0,0)
		t11.place_marker("o",1,1)
		t11.place_marker("x",2,1)
		t11.place_marker("o",2,0)
		end_state=t11.get_end_state()
		self.assertEqual(end_state,t11.END_STATES.NAUGHT_WON)

	#tests for diagonal cross victory in which final winning move is cross placed at (1,1)
	def test_diagonal_cross_victory_5(self):
		t12=TicTacToe()
		print('\n')
		print("test_diagonal_cross_victory_5 board:")
		t12.place_marker("x",0,0)
		t12.place_marker("o",1,2)
		t12.place_marker("x",2,2)
		t12.place_marker("o",0,1)
		t12.place_marker("x",1,1)
		end_state=t12.get_end_state()
		self.assertEqual(end_state,t12.END_STATES.CROSS_WON)

	#tests for diagonal naught victory in the case of the final winning move being a naught placed at (1,1)
	def test_diagonal_naught_victory_5(self):
		t13=TicTacToe()
		print('\n')
		print("test_diagonal_naught_victory_5 board:")
		t13.place_marker("x",1,2)
		t13.place_marker("o",0,2)
		t13.place_marker("x",0,0)
		t13.place_marker("o",2,0)
		t13.place_marker("x",0,1)
		t13.place_marker("o",1,1)
		end_state=t13.get_end_state()
		board=t13.get_playing_board()
		zero_two_val=board[0][2]
		two_zero_val=board[2][0]
		self.assertEqual(end_state,t13.END_STATES.NAUGHT_WON)

	#tests case for a game that ends in a tie
	def test_tie(self):
		t14=TicTacToe()
		print('\n')
		print("Board for testing a game that ends in tie")
		t14.place_marker("x",0,0)
		t14.place_marker("o",0,1)
		t14.place_marker("x",0,2)
		t14.place_marker("o",1,0)
		t14.place_marker("x",1,2)
		t14.place_marker("o",1,1)
		t14.place_marker("x",2,0)
		t14.place_marker("o",2,2)
		t14.place_marker("x",2,1)
		end_state=t14.get_end_state()
		self.assertEqual(end_state,t14.END_STATES.DRAW)









if __name__ == '__main__':

    unittest.main()