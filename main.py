#Authors: Nikki Meyer and Wafi Hussain
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

import operator
from tinker import *
import SSH
import random as rand
from os import system



class MyGridLayout(Widget):
    exit_button = ObjectProperty(None)
    reset_button = ObjectProperty(None)
    submit_button = ObjectProperty(None)
    square1 = ObjectProperty(None)
    square2 = ObjectProperty(None)
    square3 = ObjectProperty(None)
    square4 = ObjectProperty(None)
    square5 = ObjectProperty(None)
    square6 = ObjectProperty(None)
    square7 = ObjectProperty(None)
    square8 = ObjectProperty(None)
    square9 = ObjectProperty(None)
    square10 = ObjectProperty(None)
    square11 = ObjectProperty(None)
    square12 = ObjectProperty(None)
    square13 = ObjectProperty(None)
    square14 = ObjectProperty(None)
    square15 = ObjectProperty(None)
    square16 = ObjectProperty(None)
    square17 = ObjectProperty(None)
    square18 = ObjectProperty(None)
    square19 = ObjectProperty(None)
    square20 = ObjectProperty(None)
    square21 = ObjectProperty(None)
    square22 = ObjectProperty(None)
    square23 = ObjectProperty(None)
    square24 = ObjectProperty(None)
    square25 = ObjectProperty(None)
    square26 = ObjectProperty(None)
    square27 = ObjectProperty(None)
    square28 = ObjectProperty(None)
    square29 = ObjectProperty(None)
    square30 = ObjectProperty(None)
    square31 = ObjectProperty(None)
    square32 = ObjectProperty(None)
    square33 = ObjectProperty(None)
    square34 = ObjectProperty(None)
    square35 = ObjectProperty(None)

    square_count = 0
    button_list = []
    character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', ]
    q_table = [0, 31, 22, 27, 23, 28, 30, 5, 8, 5, 24, 30, 12, 14, 11, 23, 37, 26, 35, 27, 29, 33, 15, 25, 13, 28, 37, 8, 13, 13, 27, 27, 37, 40, 34, 28]
    #q_table = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    A = [11, 7, 3, 9, 15, 17, 18, 19, 20, 25, 30, 35, 16, 21, 26, 31]
    q_table.insert(0,0)
    hold = 0
    characters = 'A'
    percent_match = 0
    common_characters = []


    def press_submit(self):
        for character in self.character_list:
            self.best_match = character
            if self.best_match == 'A':
                self.character_input = [11, 7, 3, 9, 15, 17, 18, 19, 20, 25, 30, 35, 16, 21, 26, 31]
            if self.best_match =='B':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 2, 3, 4, 17, 18, 19, 32, 33, 34, 30, 25, 15, 10]
            if self.best_match =='C':
                self.character_input = [2, 5, 4, 3, 6, 11, 16, 21, 26, 32, 33, 34, 35]
            if self.best_match =='D':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 2, 3, 4, 10, 15, 20, 25, 30, 34, 33, 32]
            if self.best_match =='E':
                self.character_input = [1, 2, 3, 4, 5, 6, 11, 16, 21, 26, 31, 32, 33, 34, 35, 17, 18, 20, 19]
            if self.best_match =='F':
                self.character_input = [1, 2, 3, 4, 5, 6, 11, 16, 21, 26, 31, 17, 18, 19, 20]
            if self.best_match =='G':
                self.character_input = [2, 3, 4, 5, 6, 11, 16, 21, 26, 32, 33, 34, 30, 25, 20, 19, 18]
            if self.best_match =='H':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 5, 10, 15, 20, 25, 30, 35, 17, 18, 19]
            if self.best_match =='I':
                self.character_input = [1, 2, 3, 4, 5, 8, 13, 18, 23, 28, 33, 31, 32, 34, 35]
            if self.best_match =='J':
                self.character_input = [5, 10, 15, 20, 25, 30, 34, 33, 32, 26]
            if self.best_match =='K':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 17, 13, 9, 5, 23, 29, 35]
            if self.best_match =='L':
                self.character_input = [1, 11, 6, 16, 21, 26, 31, 32, 33, 34, 35]
            if self.best_match =='M':
                self.character_input = [13, 7, 1, 9, 5, 10, 15, 20, 25, 30, 35, 6, 11, 16, 21, 26, 31]
            if self.best_match =='N':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 5, 10, 15, 20, 25, 30, 35, 12, 18, 24]
            if self.best_match =='O':
                self.character_input = [2, 3, 4, 32, 33, 34, 26, 21, 16, 11, 6, 10, 15, 20, 25, 30]
            if self.best_match =='P':
                self.character_input = [6, 11, 16, 21, 26, 31, 1, 2, 3, 4, 10, 15, 19, 18, 17]
            if self.best_match =='Q':
                self.character_input = [2, 3, 4, 6, 11, 16, 21, 26, 32, 33, 34, 30, 25, 20, 15, 10, 35, 29, 23]
            if self.best_match =='R':
                self.character_input = [1, 2, 3, 4, 6, 11, 16, 21, 26, 31, 17, 18, 19, 15, 10, 23, 29, 35]
            if self.best_match =='S':
                self.character_input = [2, 3, 4, 5, 31, 32, 33, 34, 30, 25, 6, 11, 17, 18, 19]
            if self.best_match =='T':
                self.character_input = [2, 1, 3, 4, 5, 8, 13, 18, 23, 28, 33]
            if self.best_match =='U':
                self.character_input = [1, 11, 6, 16, 21, 26, 32, 33, 34, 30, 25, 20, 15, 10, 5]
            if self.best_match =='V':
                self.character_input = [33, 27, 29, 21, 25, 15, 10, 5, 20, 16, 6, 1, 11]
            if self.best_match =='W':
                self.character_input = [23, 27, 29, 31, 35, 5, 10, 15, 20, 25, 30, 1, 6, 11, 16, 21, 26]
            if self.best_match =='X':
                self.character_input = [1, 6, 26, 31, 30, 35, 5, 10, 12, 14, 22, 24, 18]
            if self.best_match =='Y':
                self.character_input = [1, 6, 5, 10, 14, 12, 18, 23, 28, 33]
            if self.best_match =='Z':
                self.character_input = [1, 2, 3, 4, 5, 10, 26, 31, 32, 33, 34, 35, 22, 18, 14]
            if self.best_match =='a':
                self.character_input = [11, 12, 13, 14, 15, 20, 25, 30, 35, 34, 33, 32, 26, 22, 23, 24]
            if self.best_match =='b':
                self.character_input = [1, 6, 11, 21, 26, 16, 31, 22, 23, 24, 34, 33, 32, 30]
            if self.best_match =='c':
                self.character_input = [21, 26, 32, 33, 34, 35, 17, 18, 19, 20]
            if self.best_match =='d':
                self.character_input = [26, 32, 33, 34, 35, 22, 23, 24, 25, 30, 20, 15, 10, 5]
            if self.best_match =='e':
                self.character_input = [16, 21, 26, 32, 33, 34, 35, 22, 23, 24, 25, 20, 14, 13, 12]
            if self.best_match =='f':
                self.character_input = [3, 4, 7, 12, 17, 22, 27, 32, 16, 18, 19]
            if self.best_match =='g':
                self.character_input = [8, 9, 12, 17, 23, 14, 19, 24, 29, 34, 33, 32]
            if self.best_match =='h':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 22, 23, 29, 34]
            if self.best_match =='i':
                self.character_input = [18, 23, 28, 33, 8]
            if self.best_match =='j':
                self.character_input = [26, 32, 28, 23, 18, 8]
            if self.best_match =='k':
                self.character_input = [1, 6, 11, 16, 21, 26, 31, 22, 28, 34, 18, 14]
            if self.best_match =='l':
                self.character_input = [3, 8, 13, 18, 23, 28, 33]
            if self.best_match =='m':
                self.character_input = [21, 26, 31, 16, 17, 18, 19, 25, 30, 35, 23, 28, 33]
            if self.best_match =='n':
                self.character_input = [17, 22, 27, 32, 18, 24, 34, 29]
            if self.best_match =='o':
                self.character_input = [21, 26, 32, 33, 29, 24, 18, 17]
            if self.best_match =='p':
                self.character_input = [7, 12, 17, 22, 27, 32, 13, 14, 19, 24, 23]
            if self.best_match =='q':
                self.character_input = [9, 14, 19, 24, 29, 34, 13, 12, 17, 22, 23]
            if self.best_match =='r':
                self.character_input = [22, 27, 32, 18, 19]
            if self.best_match =='s':
                self.character_input = [12, 13, 16, 22, 23, 29, 33, 32]
            if self.best_match =='t':
                self.character_input = [13, 18, 23, 28, 33, 17, 19]
            if self.best_match =='u':
                self.character_input = [16, 21, 26, 32, 33, 29, 34, 24, 19]
            if self.best_match =='v':
                self.character_input = [27, 33, 29, 25, 20, 21, 16]
            if self.best_match =='w':
                self.character_input = [34, 28, 32, 26, 21, 16, 30, 25, 20]
            if self.best_match =='x':
                self.character_input = [28, 22, 24, 34, 32]
            if self.best_match =='y':
                self.character_input = [23, 28, 33, 19, 14, 17, 12]
            if self.best_match =='z':
                self.character_input = [12, 13, 14, 32, 33, 34, 27, 23, 19]
            if self.best_match =='0':
                self.character_input = [12, 13, 14, 32, 33, 34, 27, 23, 19]
            if self.best_match =='1':
                self.character_input = [3, 13, 8, 18, 23, 28, 32, 33, 34, 7]
            if self.best_match =='2':
                self.character_input = [1, 2, 3, 4, 5, 16, 17, 19, 18, 20, 15, 10, 21, 26, 31, 32, 33, 34, 35]
            if self.best_match =='3':
                self.character_input = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 34, 33, 32, 31, 16, 17, 18, 19]
            if self.best_match =='4':
                self.character_input = [1, 6, 11, 16, 17, 18, 19, 20, 10, 5, 15, 25, 30, 35]
            if self.best_match =='5':
                self.character_input = [1, 2, 4, 5, 3, 6, 11, 16, 17, 18, 19, 20, 25, 30, 35, 34, 33, 32, 31]
            if self.best_match =='6':
                self.character_input = [1, 2, 3, 5, 4, 6, 11, 16, 21, 26, 31, 32, 33, 34, 35, 30, 25, 20, 19, 17, 18]
            if self.best_match =='7':
                self.character_input = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35]
            if self.best_match =='8':
                self.character_input = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 34, 33, 32, 31, 26, 21, 16, 11, 6, 17, 18, 19]
            if self.best_match =='9':
                self.character_input = [1, 2, 4, 5, 3, 10, 20, 15, 25, 30, 35, 16, 17, 18, 19, 11, 6]
            if self.best_match =='!':
                self.character_input = [3, 8, 13, 18, 23, 33]
			else:
				return

            
            self.pre_match = 0
            if self.percent_match > self.pre_match:
                self.button_list_set = set(self.button_list)
                self.intersection = self.button_list_set(self.character_input)
                self.common_characters = list(self.intersection)
                self.percent_match = len(self.common_characters)/len(self.charcter_input)
                self.pre_match = self.percent_match
        

        self.x = 1
        # add learning from user input to q_table
        while(self.x  < len(self.button_list)):
            print(self.button_list[self.x])
            self.x = self.x + 1
        self.button_list.sort()
        print(self.percent_match)


    #reset the button list and button colors for another entry
    def press_reset(self):        
        self.button_list.clear()
        self.square_count = 0
        self.square1.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square2.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square3.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square4.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square5.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square6.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square7.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square8.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square9.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square10.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square11.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square12.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square13.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square14.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square15.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square16.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square17.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square18.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square19.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square20.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square21.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square22.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square23.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square24.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square25.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square26.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square27.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square28.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square29.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square30.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square31.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square32.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square33.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square34.background_color = (0.9, 0.9, 0.9, 1.0)
        self.square35.background_color = (0.9, 0.9, 0.9, 1.0)



    def press_exit(self):
        quit()

    #each button press(35) will add square number to list and count number of squares pressed
    def press1(self):
        if (1 not in self.button_list):
            self.button_list.append(1)
            self.square_count += 1
            self.square1.background_color =(0, 0, 0, 1)
    def press2(self):
        if (2 not in self.button_list):
            self.button_list.append(2)
            self.square_count += 1
            self.square2.background_color =(0, 0, 0, 1)
    def press3(self):
        if (3 not in self.button_list):
            self.button_list.append(3)
            self.square_count += 1
            self.square3.background_color =(0, 0, 0, 1)
    def press4(self):
        if (4 not in self.button_list):
            self.button_list.append(4)
            self.square_count += 1
            self.square4.background_color =(0, 0, 0, 1)
    def press5(self):
        if (5 not in self.button_list):
            self.button_list.append(5)
            self.square_count += 1
            self.square5.background_color =(0, 0, 0, 1)
    def press6(self):
        if (6 not in self.button_list):
            self.button_list.append(6)
            self.square_count += 1
            self.square6.background_color =(0, 0, 0, 1)
    def press7(self):
        if (7 not in self.button_list):
            self.button_list.append(7)
            self.square_count += 1
            self.square7.background_color =(0, 0, 0, 1)
    def press8(self):
        if (8 not in self.button_list):
            self.button_list.append(8)
            self.square_count += 1
            self.square8.background_color =(0, 0, 0, 1)
    def press9(self):
        if (9 not in self.button_list):
            self.button_list.append(9)
            self.square_count += 1
            self.square9.background_color =(0, 0, 0, 1)
    def press10(self):
        if (10 not in self.button_list):
            self.button_list.append(10)
            self.square_count += 1
            self.square10.background_color =(0, 0, 0, 1)
    def press11(self):
        if (11 not in self.button_list):
            self.button_list.append(11)
            self.square_count += 1
            self.square11.background_color =(0, 0, 0, 1)
    def press12(self):
        if (12 not in self.button_list):
            self.button_list.append(12)
            self.square_count += 1
            self.square12.background_color =(0, 0, 0, 1)
    def press13(self):
        if (13 not in self.button_list):
            self.button_list.append(13)
            self.square_count += 1
            self.square13.background_color =(0, 0, 0, 1)
    def press14(self):
        if (14 not in self.button_list):
            self.button_list.append(14)
            self.square_count += 1
            self.square14.background_color =(0, 0, 0, 1)
    def press15(self):
        if (15 not in self.button_list):
            self.button_list.append(15)
            self.square_count += 1
            self.square15.background_color =(0, 0, 0, 1)
    def press16(self):
        if (16 not in self.button_list):
            self.button_list.append(16)
            self.square_count += 1
            self.square16.background_color =(0, 0, 0, 1)
    def press17(self):
        if (17 not in self.button_list):
            self.button_list.append(17)
            self.square_count += 1
            self.square17.background_color =(0, 0, 0, 1)
    def press18(self):
        if (18 not in self.button_list):
            self.button_list.append(18)
            self.square_count += 1
            self.square18.background_color =(0, 0, 0, 1)
    def press19(self):
        if (19 not in self.button_list):
            self.button_list.append(19)
            self.square_count += 1
            self.square19.background_color =(0, 0, 0, 1)
    def press20(self):
        if (20 not in self.button_list):
            self.button_list.append(20)
            self.square_count += 1
            self.square20.background_color =(0, 0, 0, 1)
    def press21(self):
        if (21 not in self.button_list):
            self.button_list.append(21)
            self.square_count += 1
            self.square21.background_color =(0, 0, 0, 1)
    def press22(self):
        if (22 not in self.button_list):
            self.button_list.append(22)
            self.square_count += 1
            self.square22.background_color =(0, 0, 0, 1)
    def press23(self):
        if (23 not in self.button_list):
            self.button_list.append(23)
            self.square_count += 1
            self.square23.background_color =(0, 0, 0, 1)
    def press24(self):
        if (24 not in self.button_list):
            self.button_list.append(24)
            self.square_count += 1
            self.square24.background_color =(0, 0, 0, 1)
    def press25(self):
        if (25 not in self.button_list):
            self.button_list.append(25)
            self.square_count += 1
            self.square25.background_color =(0, 0, 0, 1)
    def press26(self):
        if (26 not in self.button_list):
            self.button_list.append(26)
            self.square_count += 1
            self.square26.background_color =(0, 0, 0, 1)
    def press27(self):
        if (27 not in self.button_list):
            self.button_list.append(27)
            self.square_count += 1
            self.square27.background_color =(0, 0, 0, 1)
    def press28(self):
        if (28 not in self.button_list):
            self.button_list.append(28)
            self.square_count += 1
            self.square28.background_color =(0, 0, 0, 1)
    def press29(self):
        if (29 not in self.button_list):
            self.button_list.append(29)
            self.square_count += 1
            self.square29.background_color =(0, 0, 0, 1)
    def press30(self):
        if (30 not in self.button_list):
            self.button_list.append(30)
            self.square_count += 1
            self.square30.background_color =(0, 0, 0, 1)
    def press31(self):
        if (31 not in self.button_list):
            self.button_list.append(31)
            self.square_count += 1
            self.square31.background_color =(0, 0, 0, 1)
    def press32(self):
        if (32 not in self.button_list):
            self.button_list.append(32)
            self.square_count += 1
            self.square32.background_color =(0, 0, 0, 1)
    def press33(self):
        if (33 not in self.button_list):
            self.button_list.append(33)
            self.square_count += 1
            self.square33.background_color =(0, 0, 0, 1)
    def press34(self):
        if (34 not in self.button_list):
            self.button_list.append(34)
            self.square_count += 1
            self.square34.background_color =(0, 0, 0, 1)
    def press35(self):
        if (35 not in self.button_list):
            self.button_list.append(35)
            self.square_count += 1
            self.square35.background_color =(0, 0, 0, 1)

	def run_ssh(self):
		self.address = 0
		self.unsername = root
		self.password = rpi123456
		self.send_symbol = self.best_match
		ssh pvt@104.192.143.1 "~/tools/run_pvt.pl $BUILD_NUMBER"
		




    
# ----------kivy--------------------------------------------------------------------------------------------------------------------------
 # ----------kivy--------------------------------------------------------------------------------------------------------------------------
class RobotApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    RobotApp().run()
# ----------kivy--------------------------------------------------------------------------------------------------------------------------


