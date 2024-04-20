from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def text_box_1_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the first text box"""
        num_elements = int(self.text_box_1.text)
        self.text_box_2.enabled = True
        self.text_box_2.placeholder = f"Enter {num_elements} integers"

    def text_box_2_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in the second text box"""
        array = [int(x) for x in self.text_box_2.text.split()]
        sorted_array = self.insertion_sort(array)
        self.text_box_3.text = ' '.join(str(x) for x in sorted_array)

    def insertion_sort(self, array):
        """Perform insertion sort on the given array"""
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        array = [int(x) for x in self.text_box_2.text.split()]
        sorted_array = self.insertion_sort(array)
        self.text_box_3.text = ' '.join(str(x) for x in sorted_array)
