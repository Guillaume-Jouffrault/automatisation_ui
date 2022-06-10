# fen = 	-image
# 	        -bouton(numero)(un seul -> autant de noeuds que de bouton)

class Fenetre:
    def __init__(self, id, button_number, number_of_buttons):
        self.id = id  # id of window's screenshot

        # number of tabs needed from first button of the window to this button
        self.button_number = button_number

        # useful to identify the button
        self.number_of_buttons = number_of_buttons

    def get_key(self, evenmt: str):  # evenemt = 'CLIC' | 'TAB'
        return evenmt+str(self.id)
