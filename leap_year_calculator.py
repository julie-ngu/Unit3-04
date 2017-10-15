# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program calculates if a year after the birth of Christ is a leap year or not.

import ui

def check_button_touch_up_inside(sender):
    # calculates if entered year is a leap year or not
    
    # input
    inputted_year = int(view['enter_year_textfield'].text)
    
    #process
    if inputted_year < 0:
        view['answer_label'].text = "Invalid year. Please enter a year that is of positive value and is after BC."
    elif inputted_year % 4 == 0:
        if inputted_year % 100 == 0:
            if inputted_year % 400 == 0:
                view['answer_label'].text = "Yes, this year is a leap year."
            else:
                view['answer_label'].text = "No, this year is not a leap year."
        else:
            view['answer_label'].text = "Yes, this year is a leap year."
    else:
        view['answer_label'].text = "No, this year is not a leap year."

view = ui.load_view() 
view.present('full_view')
