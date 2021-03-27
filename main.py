#Authors: Nikki Meyer and Wafi Hussain
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

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


    def press_submit(self):
        print(self.button_list)
    
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

    


# ----------kivy--------------------------------------------------------------------------------------------------------------------------
 # ----------kivy--------------------------------------------------------------------------------------------------------------------------
class RobotApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    RobotApp().run()
# ----------kivy--------------------------------------------------------------------------------------------------------------------------


