# Simple Sodoku Solver 9X9

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
root.title('Sudoku Solver by Denzol')
root.configure(background='#696969')

# Create Functions Here
# =====
def check_empty(array, row_col_tracker):
	for row in range(0,9):
		for col in range(0,9):
			if array[row][col] == 0:
				row_col_tracker[0] = row
				row_col_tracker[1] = col
				return True
	return False

def usedInRow(array, row, num):
	for i in range(0,9):
		if array[row][i] == num:
			return True
	return False

def usedInCol(array, col, num):
	for i in range(0,9):
		if array[i][col] == num:
			return True
	return False

def usedInBox(array, row, col, num):
	for i in range(0,3):
		for j in range(0,3):
			if array[i+row][j+col] == num:
				return True
	return False

def is_safe(array, row, col, num):
	return not usedInRow(array, row, num) and not usedInCol(array, col, num) and not usedInBox(array, row-row%3, col-col%3, num)

def solveSodoku(array):
	#array = getArray()

	'''
	try:
		for i in range(0,9):
			for j in range(0,9):
				if len(array[i][j]) == 1:
					array[i][j] = int(array[i][j])
				elif len(array[i][j]) == 0:
					array[i][j] = 0
				else:
					condition = False
					messagebox.showerror(title='Error!', message='Enter values from 1 - 9 only!')
					break
	except:
		condition = False
		messagebox.showerror(title='Error!', message='Enter integer values only!')
	'''

	# If condition == True, return all the solved numbers,
	# If condition == False, popup error message

	# Logic for backtrack algorithm is here
	# Initial point where checking if the space is occupied or not
	row_col_tracker = [0,0]

	if not check_empty(array, row_col_tracker):
		return True

	row = row_col_tracker[0]
	col = row_col_tracker[1]

	for num in range(1,10):
		# if looks promising
		if is_safe(array, row, col, num):
			# temporary assignment
			array[row][col] = num

			# return if sucessful
			if solveSodoku(array):
				return True

			# If fail
			array[row][col] = 0

	return False

def getArray():

	global frame1_entry1
	global frame1_entry2
	global frame1_entry3
	global frame1_entry4
	global frame1_entry5
	global frame1_entry6
	global frame1_entry7
	global frame1_entry8
	global frame1_entry9

	global frame2_entry1
	global frame2_entry2
	global frame2_entry3
	global frame2_entry4
	global frame2_entry5
	global frame2_entry6
	global frame2_entry7
	global frame2_entry8
	global frame2_entry9

	global frame3_entry1
	global frame3_entry2
	global frame3_entry3
	global frame3_entry4
	global frame3_entry5
	global frame3_entry6
	global frame3_entry7
	global frame3_entry8
	global frame3_entry9

	global frame4_entry1
	global frame4_entry2
	global frame4_entry3
	global frame4_entry4
	global frame4_entry5
	global frame4_entry6
	global frame4_entry7
	global frame4_entry8
	global frame4_entry9

	global frame5_entry1
	global frame5_entry2
	global frame5_entry3
	global frame5_entry4
	global frame5_entry5
	global frame5_entry6
	global frame5_entry7
	global frame5_entry8
	global frame5_entry9

	global frame6_entry1
	global frame6_entry2
	global frame6_entry3
	global frame6_entry4
	global frame6_entry5
	global frame6_entry6
	global frame6_entry7
	global frame6_entry8
	global frame6_entry9

	global frame7_entry1
	global frame7_entry2
	global frame7_entry3
	global frame7_entry4
	global frame7_entry5
	global frame7_entry6
	global frame7_entry7
	global frame7_entry8
	global frame7_entry9

	global frame8_entry1
	global frame8_entry2
	global frame8_entry3
	global frame8_entry4
	global frame8_entry5
	global frame8_entry6
	global frame8_entry7
	global frame8_entry8
	global frame8_entry9

	global frame9_entry1
	global frame9_entry2
	global frame9_entry3
	global frame9_entry4
	global frame9_entry5
	global frame9_entry6
	global frame9_entry7
	global frame9_entry8
	global frame9_entry9

	global mainArray
	mainArray = []
	mainArray.clear()
	for i in range(0,9):
		mainArray.append([None]*9)

	# ROW 1 (BOX 1 - 3)
	mainArray[0][0] = frame1_entry1.get()
	mainArray[0][1] = frame1_entry2.get()
	mainArray[0][2] = frame1_entry3.get()
	mainArray[0][3] = frame2_entry1.get()
	mainArray[0][4] = frame2_entry2.get()
	mainArray[0][5] = frame2_entry3.get()
	mainArray[0][6] = frame3_entry1.get()
	mainArray[0][7] = frame3_entry2.get()
	mainArray[0][8] = frame3_entry3.get()

	# ROW 2 (BOX 1 - 3)
	mainArray[1][0] = frame1_entry4.get()
	mainArray[1][1] = frame1_entry5.get()
	mainArray[1][2] = frame1_entry6.get()
	mainArray[1][3] = frame2_entry4.get()
	mainArray[1][4] = frame2_entry5.get()
	mainArray[1][5] = frame2_entry6.get()
	mainArray[1][6] = frame3_entry4.get()
	mainArray[1][7] = frame3_entry5.get()
	mainArray[1][8] = frame3_entry6.get()

	# ROW 3 (BOX 1 - 3)
	mainArray[2][0] = frame1_entry7.get()
	mainArray[2][1] = frame1_entry8.get()
	mainArray[2][2] = frame1_entry9.get()
	mainArray[2][3] = frame2_entry7.get()
	mainArray[2][4] = frame2_entry8.get()
	mainArray[2][5] = frame2_entry9.get()
	mainArray[2][6] = frame3_entry7.get()
	mainArray[2][7] = frame3_entry8.get()
	mainArray[2][8] = frame3_entry9.get()

	# ROW 4 (BOX 4 - 6)
	mainArray[3][0] = frame4_entry1.get()
	mainArray[3][1] = frame4_entry2.get()
	mainArray[3][2] = frame4_entry3.get()
	mainArray[3][3] = frame5_entry1.get()
	mainArray[3][4] = frame5_entry2.get()
	mainArray[3][5] = frame5_entry3.get()
	mainArray[3][6] = frame6_entry1.get()
	mainArray[3][7] = frame6_entry2.get()
	mainArray[3][8] = frame6_entry3.get()

	# ROW 5 (BOX 4 - 6)
	mainArray[4][0] = frame4_entry4.get()
	mainArray[4][1] = frame4_entry5.get()
	mainArray[4][2] = frame4_entry6.get()
	mainArray[4][3] = frame5_entry4.get()
	mainArray[4][4] = frame5_entry5.get()
	mainArray[4][5] = frame5_entry6.get()
	mainArray[4][6] = frame6_entry4.get()
	mainArray[4][7] = frame6_entry5.get()
	mainArray[4][8] = frame6_entry6.get()

	# ROW 6 (BOX 4 - 6)
	mainArray[5][0] = frame4_entry7.get()
	mainArray[5][1] = frame4_entry8.get()
	mainArray[5][2] = frame4_entry9.get()
	mainArray[5][3] = frame5_entry7.get()
	mainArray[5][4] = frame5_entry8.get()
	mainArray[5][5] = frame5_entry9.get()
	mainArray[5][6] = frame6_entry7.get()
	mainArray[5][7] = frame6_entry8.get()
	mainArray[5][8] = frame6_entry9.get()

	# ROW 7 (BOX 7 - 9)
	mainArray[6][0] = frame7_entry1.get()
	mainArray[6][1] = frame7_entry2.get()
	mainArray[6][2] = frame7_entry3.get()
	mainArray[6][3] = frame8_entry1.get()
	mainArray[6][4] = frame8_entry2.get()
	mainArray[6][5] = frame8_entry3.get()
	mainArray[6][6] = frame9_entry1.get()
	mainArray[6][7] = frame9_entry2.get()
	mainArray[6][8] = frame9_entry3.get()

	# ROW 8 (BOX 7 - 9)
	mainArray[7][0] = frame7_entry4.get()
	mainArray[7][1] = frame7_entry5.get()
	mainArray[7][2] = frame7_entry6.get()
	mainArray[7][3] = frame8_entry4.get()
	mainArray[7][4] = frame8_entry5.get()
	mainArray[7][5] = frame8_entry6.get()
	mainArray[7][6] = frame9_entry4.get()
	mainArray[7][7] = frame9_entry5.get()
	mainArray[7][8] = frame9_entry6.get()

	# ROW 9 (BOX 7 - 9)
	mainArray[8][0] = frame7_entry7.get()
	mainArray[8][1] = frame7_entry8.get()
	mainArray[8][2] = frame7_entry9.get()
	mainArray[8][3] = frame8_entry7.get()
	mainArray[8][4] = frame8_entry8.get()
	mainArray[8][5] = frame8_entry9.get()
	mainArray[8][6] = frame9_entry7.get()
	mainArray[8][7] = frame9_entry8.get()
	mainArray[8][8] = frame9_entry9.get()

	condition = True

	try:
		for i in range(0,9):
			for j in range(0,9):
				if len(mainArray[i][j]) == 1:
					mainArray[i][j] = int(mainArray[i][j])
				elif len(mainArray[i][j]) == 0:
					mainArray[i][j] = 0
				else:
					condition = False
					mainArray.clear()
					messagebox.showerror(title='Error!', message='Enter values from 1 - 9 only!')
					break
	except:
		condition = False
		mainArray.clear()
		messagebox.showerror(title='Error!', message='Enter integer values only!')

	if condition == True:
		solveSodoku(mainArray)
	if condition == False:
		pass

	print(solveSodoku(mainArray))
	if solveSodoku(mainArray):

		frame1_entry1.delete(0, END)
		frame1_entry2.delete(0, END)
		frame1_entry3.delete(0, END)
		frame1_entry4.delete(0, END)
		frame1_entry5.delete(0, END)
		frame1_entry6.delete(0, END)
		frame1_entry7.delete(0, END)
		frame1_entry8.delete(0, END)
		frame1_entry9.delete(0, END)

		frame2_entry1.delete(0, END)
		frame2_entry2.delete(0, END)
		frame2_entry3.delete(0, END)
		frame2_entry4.delete(0, END)
		frame2_entry5.delete(0, END)
		frame2_entry6.delete(0, END)
		frame2_entry7.delete(0, END)
		frame2_entry8.delete(0, END)
		frame2_entry9.delete(0, END)

		frame3_entry1.delete(0, END)
		frame3_entry2.delete(0, END)
		frame3_entry3.delete(0, END)
		frame3_entry4.delete(0, END)
		frame3_entry5.delete(0, END)
		frame3_entry6.delete(0, END)
		frame3_entry7.delete(0, END)
		frame3_entry8.delete(0, END)
		frame3_entry9.delete(0, END)

		frame4_entry1.delete(0, END)
		frame4_entry2.delete(0, END)
		frame4_entry3.delete(0, END)
		frame4_entry4.delete(0, END)
		frame4_entry5.delete(0, END)
		frame4_entry6.delete(0, END)
		frame4_entry7.delete(0, END)
		frame4_entry8.delete(0, END)
		frame4_entry9.delete(0, END)

		frame5_entry1.delete(0, END)
		frame5_entry2.delete(0, END)
		frame5_entry3.delete(0, END)
		frame5_entry4.delete(0, END)
		frame5_entry5.delete(0, END)
		frame5_entry6.delete(0, END)
		frame5_entry7.delete(0, END)
		frame5_entry8.delete(0, END)
		frame5_entry9.delete(0, END)

		frame6_entry1.delete(0, END)
		frame6_entry2.delete(0, END)
		frame6_entry3.delete(0, END)
		frame6_entry4.delete(0, END)
		frame6_entry5.delete(0, END)
		frame6_entry6.delete(0, END)
		frame6_entry7.delete(0, END)
		frame6_entry8.delete(0, END)
		frame6_entry9.delete(0, END)

		frame7_entry1.delete(0, END)
		frame7_entry2.delete(0, END)
		frame7_entry3.delete(0, END)
		frame7_entry4.delete(0, END)
		frame7_entry5.delete(0, END)
		frame7_entry6.delete(0, END)
		frame7_entry7.delete(0, END)
		frame7_entry8.delete(0, END)
		frame7_entry9.delete(0, END)

		frame8_entry1.delete(0, END)
		frame8_entry2.delete(0, END)
		frame8_entry3.delete(0, END)
		frame8_entry4.delete(0, END)
		frame8_entry5.delete(0, END)
		frame8_entry6.delete(0, END)
		frame8_entry7.delete(0, END)
		frame8_entry8.delete(0, END)
		frame8_entry9.delete(0, END)

		frame9_entry1.delete(0, END)
		frame9_entry2.delete(0, END)
		frame9_entry3.delete(0, END)
		frame9_entry4.delete(0, END)
		frame9_entry5.delete(0, END)
		frame9_entry6.delete(0, END)
		frame9_entry7.delete(0, END)
		frame9_entry8.delete(0, END)
		frame9_entry9.delete(0, END)

		# ROW 1 (BOX 1 - 3)
		frame1_entry1.insert(0, mainArray[0][0])
		frame1_entry2.insert(0, mainArray[0][1])
		frame1_entry3.insert(0, mainArray[0][2])
		frame2_entry1.insert(0, mainArray[0][3])
		frame2_entry2.insert(0, mainArray[0][4])
		frame2_entry3.insert(0, mainArray[0][5])
		frame3_entry1.insert(0, mainArray[0][6])
		frame3_entry2.insert(0, mainArray[0][7])
		frame3_entry3.insert(0, mainArray[0][8])

		# ROW 2 (BOX 1 - 3)
		frame1_entry4.insert(0, mainArray[1][0])
		frame1_entry5.insert(0, mainArray[1][1])
		frame1_entry6.insert(0, mainArray[1][2])
		frame2_entry4.insert(0, mainArray[1][3])
		frame2_entry5.insert(0, mainArray[1][4])
		frame2_entry6.insert(0, mainArray[1][5])
		frame3_entry4.insert(0, mainArray[1][6])
		frame3_entry5.insert(0, mainArray[1][7])
		frame3_entry6.insert(0, mainArray[1][8])

		# ROW 3 (BOX 1 - 3)
		frame1_entry7.insert(0, mainArray[2][0])
		frame1_entry8.insert(0, mainArray[2][1])
		frame1_entry9.insert(0, mainArray[2][2])
		frame2_entry7.insert(0, mainArray[2][3])
		frame2_entry8.insert(0, mainArray[2][4])
		frame2_entry9.insert(0, mainArray[2][5])
		frame3_entry7.insert(0, mainArray[2][6])
		frame3_entry8.insert(0, mainArray[2][7])
		frame3_entry9.insert(0, mainArray[2][8])

		# ROW 4 (BOX 4 - 6)
		frame4_entry1.insert(0, mainArray[3][0])
		frame4_entry2.insert(0, mainArray[3][1])
		frame4_entry3.insert(0, mainArray[3][2])
		frame5_entry1.insert(0, mainArray[3][3])
		frame5_entry2.insert(0, mainArray[3][4])
		frame5_entry3.insert(0, mainArray[3][5])
		frame6_entry1.insert(0, mainArray[3][6])
		frame6_entry2.insert(0, mainArray[3][7])
		frame6_entry3.insert(0, mainArray[3][8])

		# ROW 5 (BOX 4 - 6)
		frame4_entry4.insert(0, mainArray[4][0])
		frame4_entry5.insert(0, mainArray[4][1])
		frame4_entry6.insert(0, mainArray[4][2])
		frame5_entry4.insert(0, mainArray[4][3])
		frame5_entry5.insert(0, mainArray[4][4])
		frame5_entry6.insert(0, mainArray[4][5])
		frame6_entry4.insert(0, mainArray[4][6])
		frame6_entry5.insert(0, mainArray[4][7])
		frame6_entry6.insert(0, mainArray[4][8])

		# ROW 6 (BOX 4 - 6)
		frame4_entry7.insert(0, mainArray[5][0])
		frame4_entry8.insert(0, mainArray[5][1])
		frame4_entry9.insert(0, mainArray[5][2])
		frame5_entry7.insert(0, mainArray[5][3])
		frame5_entry8.insert(0, mainArray[5][4])
		frame5_entry9.insert(0, mainArray[5][5])
		frame6_entry7.insert(0, mainArray[5][6])
		frame6_entry8.insert(0, mainArray[5][7])
		frame6_entry9.insert(0, mainArray[5][8])

		# ROW 7 (BOX 7 - 9)
		frame7_entry1.insert(0, mainArray[6][0])
		frame7_entry2.insert(0, mainArray[6][1])
		frame7_entry3.insert(0, mainArray[6][2])
		frame8_entry1.insert(0, mainArray[6][3])
		frame8_entry2.insert(0, mainArray[6][4])
		frame8_entry3.insert(0, mainArray[6][5])
		frame9_entry1.insert(0, mainArray[6][6])
		frame9_entry2.insert(0, mainArray[6][7])
		frame9_entry3.insert(0, mainArray[6][8])

		# ROW 8 (BOX 7 - 9)
		frame7_entry4.insert(0, mainArray[7][0])
		frame7_entry5.insert(0, mainArray[7][1])
		frame7_entry6.insert(0, mainArray[7][2])
		frame8_entry4.insert(0, mainArray[7][3])
		frame8_entry5.insert(0, mainArray[7][4])
		frame8_entry6.insert(0, mainArray[7][5])
		frame9_entry4.insert(0, mainArray[7][6])
		frame9_entry5.insert(0, mainArray[7][7])
		frame9_entry6.insert(0, mainArray[7][8])

		# ROW 9 (BOX 7 - 9)
		frame7_entry7.insert(0, mainArray[8][0])
		frame7_entry8.insert(0, mainArray[8][1])
		frame7_entry9.insert(0, mainArray[8][2])
		frame8_entry7.insert(0, mainArray[8][3])
		frame8_entry8.insert(0, mainArray[8][4])
		frame8_entry9.insert(0, mainArray[8][5])
		frame9_entry7.insert(0, mainArray[8][6])
		frame9_entry8.insert(0, mainArray[8][7])
		frame9_entry9.insert(0, mainArray[8][8])

		frame1_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame1_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame2_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame2_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame3_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame3_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame4_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame4_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame5_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame5_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame6_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame6_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame7_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame7_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame8_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame8_entry9.config(state='readonly', readonlybackground='#C0C0C0')

		frame9_entry1.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry2.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry3.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry4.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry5.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry6.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry7.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry8.config(state='readonly', readonlybackground='#C0C0C0')
		frame9_entry9.config(state='readonly', readonlybackground='#C0C0C0')
		
	else:
		print('No Solution Exists')

def clearAll():

	global frame1_entry1
	global frame1_entry2
	global frame1_entry3
	global frame1_entry4
	global frame1_entry5
	global frame1_entry6
	global frame1_entry7
	global frame1_entry8
	global frame1_entry9

	global frame2_entry1
	global frame2_entry2
	global frame2_entry3
	global frame2_entry4
	global frame2_entry5
	global frame2_entry6
	global frame2_entry7
	global frame2_entry8
	global frame2_entry9

	global frame3_entry1
	global frame3_entry2
	global frame3_entry3
	global frame3_entry4
	global frame3_entry5
	global frame3_entry6
	global frame3_entry7
	global frame3_entry8
	global frame3_entry9

	global frame4_entry1
	global frame4_entry2
	global frame4_entry3
	global frame4_entry4
	global frame4_entry5
	global frame4_entry6
	global frame4_entry7
	global frame4_entry8
	global frame4_entry9

	global frame5_entry1
	global frame5_entry2
	global frame5_entry3
	global frame5_entry4
	global frame5_entry5
	global frame5_entry6
	global frame5_entry7
	global frame5_entry8
	global frame5_entry9

	global frame6_entry1
	global frame6_entry2
	global frame6_entry3
	global frame6_entry4
	global frame6_entry5
	global frame6_entry6
	global frame6_entry7
	global frame6_entry8
	global frame6_entry9

	global frame7_entry1
	global frame7_entry2
	global frame7_entry3
	global frame7_entry4
	global frame7_entry5
	global frame7_entry6
	global frame7_entry7
	global frame7_entry8
	global frame7_entry9

	global frame8_entry1
	global frame8_entry2
	global frame8_entry3
	global frame8_entry4
	global frame8_entry5
	global frame8_entry6
	global frame8_entry7
	global frame8_entry8
	global frame8_entry9

	global frame9_entry1
	global frame9_entry2
	global frame9_entry3
	global frame9_entry4
	global frame9_entry5
	global frame9_entry6
	global frame9_entry7
	global frame9_entry8
	global frame9_entry9

	global mainArray

	frame1_entry1.config(state=NORMAL, background='#C0C0C0')
	frame1_entry2.config(state=NORMAL, background='#C0C0C0')
	frame1_entry3.config(state=NORMAL, background='#C0C0C0')
	frame1_entry4.config(state=NORMAL, background='#C0C0C0')
	frame1_entry5.config(state=NORMAL, background='#C0C0C0')
	frame1_entry6.config(state=NORMAL, background='#C0C0C0')
	frame1_entry7.config(state=NORMAL, background='#C0C0C0')
	frame1_entry8.config(state=NORMAL, background='#C0C0C0')
	frame1_entry9.config(state=NORMAL, background='#C0C0C0')

	frame2_entry1.config(state=NORMAL, background='#C0C0C0')
	frame2_entry2.config(state=NORMAL, background='#C0C0C0')
	frame2_entry3.config(state=NORMAL, background='#C0C0C0')
	frame2_entry4.config(state=NORMAL, background='#C0C0C0')
	frame2_entry5.config(state=NORMAL, background='#C0C0C0')
	frame2_entry6.config(state=NORMAL, background='#C0C0C0')
	frame2_entry7.config(state=NORMAL, background='#C0C0C0')
	frame2_entry8.config(state=NORMAL, background='#C0C0C0')
	frame2_entry9.config(state=NORMAL, background='#C0C0C0')

	frame3_entry1.config(state=NORMAL, background='#C0C0C0')
	frame3_entry2.config(state=NORMAL, background='#C0C0C0')
	frame3_entry3.config(state=NORMAL, background='#C0C0C0')
	frame3_entry4.config(state=NORMAL, background='#C0C0C0')
	frame3_entry5.config(state=NORMAL, background='#C0C0C0')
	frame3_entry6.config(state=NORMAL, background='#C0C0C0')
	frame3_entry7.config(state=NORMAL, background='#C0C0C0')
	frame3_entry8.config(state=NORMAL, background='#C0C0C0')
	frame3_entry9.config(state=NORMAL, background='#C0C0C0')

	frame4_entry1.config(state=NORMAL, background='#C0C0C0')
	frame4_entry2.config(state=NORMAL, background='#C0C0C0')
	frame4_entry3.config(state=NORMAL, background='#C0C0C0')
	frame4_entry4.config(state=NORMAL, background='#C0C0C0')
	frame4_entry5.config(state=NORMAL, background='#C0C0C0')
	frame4_entry6.config(state=NORMAL, background='#C0C0C0')
	frame4_entry7.config(state=NORMAL, background='#C0C0C0')
	frame4_entry8.config(state=NORMAL, background='#C0C0C0')
	frame4_entry9.config(state=NORMAL, background='#C0C0C0')

	frame5_entry1.config(state=NORMAL, background='#C0C0C0')
	frame5_entry2.config(state=NORMAL, background='#C0C0C0')
	frame5_entry3.config(state=NORMAL, background='#C0C0C0')
	frame5_entry4.config(state=NORMAL, background='#C0C0C0')
	frame5_entry5.config(state=NORMAL, background='#C0C0C0')
	frame5_entry6.config(state=NORMAL, background='#C0C0C0')
	frame5_entry7.config(state=NORMAL, background='#C0C0C0')
	frame5_entry8.config(state=NORMAL, background='#C0C0C0')
	frame5_entry9.config(state=NORMAL, background='#C0C0C0')

	frame6_entry1.config(state=NORMAL, background='#C0C0C0')
	frame6_entry2.config(state=NORMAL, background='#C0C0C0')
	frame6_entry3.config(state=NORMAL, background='#C0C0C0')
	frame6_entry4.config(state=NORMAL, background='#C0C0C0')
	frame6_entry5.config(state=NORMAL, background='#C0C0C0')
	frame6_entry6.config(state=NORMAL, background='#C0C0C0')
	frame6_entry7.config(state=NORMAL, background='#C0C0C0')
	frame6_entry8.config(state=NORMAL, background='#C0C0C0')
	frame6_entry9.config(state=NORMAL, background='#C0C0C0')

	frame7_entry1.config(state=NORMAL, background='#C0C0C0')
	frame7_entry2.config(state=NORMAL, background='#C0C0C0')
	frame7_entry3.config(state=NORMAL, background='#C0C0C0')
	frame7_entry4.config(state=NORMAL, background='#C0C0C0')
	frame7_entry5.config(state=NORMAL, background='#C0C0C0')
	frame7_entry6.config(state=NORMAL, background='#C0C0C0')
	frame7_entry7.config(state=NORMAL, background='#C0C0C0')
	frame7_entry8.config(state=NORMAL, background='#C0C0C0')
	frame7_entry9.config(state=NORMAL, background='#C0C0C0')

	frame8_entry1.config(state=NORMAL, background='#C0C0C0')
	frame8_entry2.config(state=NORMAL, background='#C0C0C0')
	frame8_entry3.config(state=NORMAL, background='#C0C0C0')
	frame8_entry4.config(state=NORMAL, background='#C0C0C0')
	frame8_entry5.config(state=NORMAL, background='#C0C0C0')
	frame8_entry6.config(state=NORMAL, background='#C0C0C0')
	frame8_entry7.config(state=NORMAL, background='#C0C0C0')
	frame8_entry8.config(state=NORMAL, background='#C0C0C0')
	frame8_entry9.config(state=NORMAL, background='#C0C0C0')

	frame9_entry1.config(state=NORMAL, background='#C0C0C0')
	frame9_entry2.config(state=NORMAL, background='#C0C0C0')
	frame9_entry3.config(state=NORMAL, background='#C0C0C0')
	frame9_entry4.config(state=NORMAL, background='#C0C0C0')
	frame9_entry5.config(state=NORMAL, background='#C0C0C0')
	frame9_entry6.config(state=NORMAL, background='#C0C0C0')
	frame9_entry7.config(state=NORMAL, background='#C0C0C0')
	frame9_entry8.config(state=NORMAL, background='#C0C0C0')
	frame9_entry9.config(state=NORMAL, background='#C0C0C0')

	frame1_entry1.delete(0, END)
	frame1_entry2.delete(0, END)
	frame1_entry3.delete(0, END)
	frame1_entry4.delete(0, END)
	frame1_entry5.delete(0, END)
	frame1_entry6.delete(0, END)
	frame1_entry7.delete(0, END)
	frame1_entry8.delete(0, END)
	frame1_entry9.delete(0, END)

	frame2_entry1.delete(0, END)
	frame2_entry2.delete(0, END)
	frame2_entry3.delete(0, END)
	frame2_entry4.delete(0, END)
	frame2_entry5.delete(0, END)
	frame2_entry6.delete(0, END)
	frame2_entry7.delete(0, END)
	frame2_entry8.delete(0, END)
	frame2_entry9.delete(0, END)

	frame3_entry1.delete(0, END)
	frame3_entry2.delete(0, END)
	frame3_entry3.delete(0, END)
	frame3_entry4.delete(0, END)
	frame3_entry5.delete(0, END)
	frame3_entry6.delete(0, END)
	frame3_entry7.delete(0, END)
	frame3_entry8.delete(0, END)
	frame3_entry9.delete(0, END)

	frame4_entry1.delete(0, END)
	frame4_entry2.delete(0, END)
	frame4_entry3.delete(0, END)
	frame4_entry4.delete(0, END)
	frame4_entry5.delete(0, END)
	frame4_entry6.delete(0, END)
	frame4_entry7.delete(0, END)
	frame4_entry8.delete(0, END)
	frame4_entry9.delete(0, END)

	frame5_entry1.delete(0, END)
	frame5_entry2.delete(0, END)
	frame5_entry3.delete(0, END)
	frame5_entry4.delete(0, END)
	frame5_entry5.delete(0, END)
	frame5_entry6.delete(0, END)
	frame5_entry7.delete(0, END)
	frame5_entry8.delete(0, END)
	frame5_entry9.delete(0, END)

	frame6_entry1.delete(0, END)
	frame6_entry2.delete(0, END)
	frame6_entry3.delete(0, END)
	frame6_entry4.delete(0, END)
	frame6_entry5.delete(0, END)
	frame6_entry6.delete(0, END)
	frame6_entry7.delete(0, END)
	frame6_entry8.delete(0, END)
	frame6_entry9.delete(0, END)

	frame7_entry1.delete(0, END)
	frame7_entry2.delete(0, END)
	frame7_entry3.delete(0, END)
	frame7_entry4.delete(0, END)
	frame7_entry5.delete(0, END)
	frame7_entry6.delete(0, END)
	frame7_entry7.delete(0, END)
	frame7_entry8.delete(0, END)
	frame7_entry9.delete(0, END)

	frame8_entry1.delete(0, END)
	frame8_entry2.delete(0, END)
	frame8_entry3.delete(0, END)
	frame8_entry4.delete(0, END)
	frame8_entry5.delete(0, END)
	frame8_entry6.delete(0, END)
	frame8_entry7.delete(0, END)
	frame8_entry8.delete(0, END)
	frame8_entry9.delete(0, END)

	frame9_entry1.delete(0, END)
	frame9_entry2.delete(0, END)
	frame9_entry3.delete(0, END)
	frame9_entry4.delete(0, END)
	frame9_entry5.delete(0, END)
	frame9_entry6.delete(0, END)
	frame9_entry7.delete(0, END)
	frame9_entry8.delete(0, END)
	frame9_entry9.delete(0, END)

# =====

frame1 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame2 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame3 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame4 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame5 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame6 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame7 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame8 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame9 = LabelFrame(root, padx=5, pady=5, background='#696969')
frame10 = Frame(root, padx=20, pady=20, background='#696969')

frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2)
frame4.grid(row=1, column=0)
frame5.grid(row=1, column=1)
frame6.grid(row=1, column=2)
frame7.grid(row=2, column=0)
frame8.grid(row=2, column=1)
frame9.grid(row=2, column=2)
frame10.grid(row=3, column=0, columnspan=3)

# BOX 1
frame1_entry1 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry2 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry3 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry4 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry5 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry6 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry7 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry8 = Entry(frame1, width=3, background='#C0C0C0')
frame1_entry9 = Entry(frame1, width=3, background='#C0C0C0')

frame1_entry1.grid(row=0, column=0, ipadx=1)
frame1_entry2.grid(row=0, column=1, ipadx=1)
frame1_entry3.grid(row=0, column=2, ipadx=1)
frame1_entry4.grid(row=1, column=0, ipadx=1)
frame1_entry5.grid(row=1, column=1, ipadx=1)
frame1_entry6.grid(row=1, column=2, ipadx=1)
frame1_entry7.grid(row=2, column=0, ipadx=1)
frame1_entry8.grid(row=2, column=1, ipadx=1)
frame1_entry9.grid(row=2, column=2, ipadx=1)

# BOX 2
frame2_entry1 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry2 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry3 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry4 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry5 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry6 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry7 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry8 = Entry(frame2, width=3, background='#C0C0C0')
frame2_entry9 = Entry(frame2, width=3, background='#C0C0C0')

frame2_entry1.grid(row=0, column=0, ipadx=1)
frame2_entry2.grid(row=0, column=1, ipadx=1)
frame2_entry3.grid(row=0, column=2, ipadx=1)
frame2_entry4.grid(row=1, column=0, ipadx=1)
frame2_entry5.grid(row=1, column=1, ipadx=1)
frame2_entry6.grid(row=1, column=2, ipadx=1)
frame2_entry7.grid(row=2, column=0, ipadx=1)
frame2_entry8.grid(row=2, column=1, ipadx=1)
frame2_entry9.grid(row=2, column=2, ipadx=1)

# BOX 3
frame3_entry1 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry2 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry3 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry4 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry5 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry6 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry7 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry8 = Entry(frame3, width=3, background='#C0C0C0')
frame3_entry9 = Entry(frame3, width=3, background='#C0C0C0')

frame3_entry1.grid(row=0, column=0, ipadx=1)
frame3_entry2.grid(row=0, column=1, ipadx=1)
frame3_entry3.grid(row=0, column=2, ipadx=1)
frame3_entry4.grid(row=1, column=0, ipadx=1)
frame3_entry5.grid(row=1, column=1, ipadx=1)
frame3_entry6.grid(row=1, column=2, ipadx=1)
frame3_entry7.grid(row=2, column=0, ipadx=1)
frame3_entry8.grid(row=2, column=1, ipadx=1)
frame3_entry9.grid(row=2, column=2, ipadx=1)

# BOX 4
frame4_entry1 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry2 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry3 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry4 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry5 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry6 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry7 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry8 = Entry(frame4, width=3, background='#C0C0C0')
frame4_entry9 = Entry(frame4, width=3, background='#C0C0C0')

frame4_entry1.grid(row=0, column=0, ipadx=1)
frame4_entry2.grid(row=0, column=1, ipadx=1)
frame4_entry3.grid(row=0, column=2, ipadx=1)
frame4_entry4.grid(row=1, column=0, ipadx=1)
frame4_entry5.grid(row=1, column=1, ipadx=1)
frame4_entry6.grid(row=1, column=2, ipadx=1)
frame4_entry7.grid(row=2, column=0, ipadx=1)
frame4_entry8.grid(row=2, column=1, ipadx=1)
frame4_entry9.grid(row=2, column=2, ipadx=1)

# BOX 5
frame5_entry1 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry2 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry3 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry4 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry5 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry6 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry7 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry8 = Entry(frame5, width=3, background='#C0C0C0')
frame5_entry9 = Entry(frame5, width=3, background='#C0C0C0')

frame5_entry1.grid(row=0, column=0, ipadx=1)
frame5_entry2.grid(row=0, column=1, ipadx=1)
frame5_entry3.grid(row=0, column=2, ipadx=1)
frame5_entry4.grid(row=1, column=0, ipadx=1)
frame5_entry5.grid(row=1, column=1, ipadx=1)
frame5_entry6.grid(row=1, column=2, ipadx=1)
frame5_entry7.grid(row=2, column=0, ipadx=1)
frame5_entry8.grid(row=2, column=1, ipadx=1)
frame5_entry9.grid(row=2, column=2, ipadx=1)

# BOX 6
frame6_entry1 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry2 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry3 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry4 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry5 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry6 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry7 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry8 = Entry(frame6, width=3, background='#C0C0C0')
frame6_entry9 = Entry(frame6, width=3, background='#C0C0C0')

frame6_entry1.grid(row=0, column=0, ipadx=1)
frame6_entry2.grid(row=0, column=1, ipadx=1)
frame6_entry3.grid(row=0, column=2, ipadx=1)
frame6_entry4.grid(row=1, column=0, ipadx=1)
frame6_entry5.grid(row=1, column=1, ipadx=1)
frame6_entry6.grid(row=1, column=2, ipadx=1)
frame6_entry7.grid(row=2, column=0, ipadx=1)
frame6_entry8.grid(row=2, column=1, ipadx=1)
frame6_entry9.grid(row=2, column=2, ipadx=1)

# BOX 7
frame7_entry1 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry2 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry3 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry4 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry5 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry6 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry7 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry8 = Entry(frame7, width=3, background='#C0C0C0')
frame7_entry9 = Entry(frame7, width=3, background='#C0C0C0')

frame7_entry1.grid(row=0, column=0, ipadx=1)
frame7_entry2.grid(row=0, column=1, ipadx=1)
frame7_entry3.grid(row=0, column=2, ipadx=1)
frame7_entry4.grid(row=1, column=0, ipadx=1)
frame7_entry5.grid(row=1, column=1, ipadx=1)
frame7_entry6.grid(row=1, column=2, ipadx=1)
frame7_entry7.grid(row=2, column=0, ipadx=1)
frame7_entry8.grid(row=2, column=1, ipadx=1)
frame7_entry9.grid(row=2, column=2, ipadx=1)

# BOX 8
frame8_entry1 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry2 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry3 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry4 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry5 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry6 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry7 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry8 = Entry(frame8, width=3, background='#C0C0C0')
frame8_entry9 = Entry(frame8, width=3, background='#C0C0C0')

frame8_entry1.grid(row=0, column=0, ipadx=1)
frame8_entry2.grid(row=0, column=1, ipadx=1)
frame8_entry3.grid(row=0, column=2, ipadx=1)
frame8_entry4.grid(row=1, column=0, ipadx=1)
frame8_entry5.grid(row=1, column=1, ipadx=1)
frame8_entry6.grid(row=1, column=2, ipadx=1)
frame8_entry7.grid(row=2, column=0, ipadx=1)
frame8_entry8.grid(row=2, column=1, ipadx=1)
frame8_entry9.grid(row=2, column=2, ipadx=1)

# BOX 9
frame9_entry1 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry2 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry3 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry4 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry5 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry6 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry7 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry8 = Entry(frame9, width=3, background='#C0C0C0')
frame9_entry9 = Entry(frame9, width=3, background='#C0C0C0')

frame9_entry1.grid(row=0, column=0, ipadx=1)
frame9_entry2.grid(row=0, column=1, ipadx=1)
frame9_entry3.grid(row=0, column=2, ipadx=1)
frame9_entry4.grid(row=1, column=0, ipadx=1)
frame9_entry5.grid(row=1, column=1, ipadx=1)
frame9_entry6.grid(row=1, column=2, ipadx=1)
frame9_entry7.grid(row=2, column=0, ipadx=1)
frame9_entry8.grid(row=2, column=1, ipadx=1)
frame9_entry9.grid(row=2, column=2, ipadx=1)

# Solve button
buttonSolve = Button(frame10, text='Solve Sodoku!', background='#C0C0C0', command=getArray)
buttonSolve.grid(row=0, column=0,ipadx=20)

# Clear button
buttonClear = Button(frame10, text='Clear', background='#C0C0C0', command=clearAll)
buttonClear.grid(row=0, column=1, ipadx=20)

root.mainloop()