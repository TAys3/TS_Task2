# A ton of errors will appear in the terminal if no boxes are ticked and you move the slider,
# but this is expected, and the app will still run, unaffected.

import gooeypie as gp
import string
import random

#setting
app = gp.GooeyPieApp('Password Generator')
app.set_size(400,500)
app.set_resizable(False)    #window will not be able to be resized

font = 'fira code'  #font used for certain widgets. Can only use fonts you have installed, or it will use the default
pass_len = 0
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
DIGITS = string.digits
OTHER = string.punctuation

#functions
def make_pass(event):   #generates a password based upon user's input
    global LOWER_CASE
    global UPPER_CASE
    global DIGITS
    global OTHER
    if pass_len_slider.value == 1:    #This changes the label's text to the value of the slider
        plural = ''
    else:
        plural = 's'
    slider_label.text = f'''Password length: 
{pass_len_slider.value} character{plural}'''

    pass_char = ""
    if letters.checked == True:     #These are to check if a box is ticked, and then add the characters if so
        pass_char += LOWER_CASE
    else:
        pass
    if cap_letters.checked == True:
        pass_char += UPPER_CASE
    else:
        pass
    if numbers.checked == True:
        pass_char += DIGITS
    else:
        pass
    if special_char.checked == True:
        pass_char += OTHER
    else:
        pass
    
    Gen_Pass = ''
    for i in range(pass_len_slider.value):  #This creates the password
        Gen_Pass += random.choice(pass_char)
    Password.text = Gen_Pass
    

def copy_pass(event):   #Copies the password to the clipboard
    app.copy_to_clipboard(Password.text)

#widgets
slider_label = gp.StyleLabel(app, f'''Password length: 
{pass_len} characters''')
slider_label.set_font(f'{font}', 12)
pass_len_slider = gp.Slider(app, 1, 40)
letters = gp.Checkbox(app, 'a-z')
cap_letters = gp.Checkbox(app, 'A-Z')
numbers = gp.Checkbox(app, '0-9')
special_char = gp.Checkbox(app, 'Special characters')
Password = gp.Input(app)    #decided to make it an input box so that the user can make changes easily
Password.justify = 'center'
copy_to_clip = gp.ImageButton(app, 'Resources/211649_clipboard_icon2.png', copy_pass, 'Copy to clipboard')
new_pass = gp.Button(app, 'Re-generate password', make_pass)


#event listeners
pass_len_slider.add_event_listener('change', make_pass)
letters.add_event_listener('change', make_pass)
cap_letters.add_event_listener('change', make_pass)
numbers.add_event_listener('change', make_pass)
special_char.add_event_listener('change', make_pass)



#layout
app.set_grid(8, 6)
app.add(slider_label, 1, 1, align = 'left')
app.add(pass_len_slider, 2, 1, align = 'center', column_span = 6, fill = True, stretch = True)
app.add(letters, 3, 1, align = 'left')
app.add(cap_letters, 3, 2, align = 'left')
app.add(numbers, 4, 1, align = 'left')
app.add(special_char, 4, 2, align = 'left')
app.add(Password, 5, 1, align = 'center', column_span = 6, stretch = True, fill = True)
app.add(copy_to_clip, 6, 1, align = 'center',  column_span = 6, stretch = True, fill = True)
app.add(new_pass, 7, 1, align = 'center',  column_span = 6, row_span = 2, stretch = True, fill = True,)



app.run()