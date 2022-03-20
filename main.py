from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# first create class for our app
class MainApp(App):
    def build(self):
        # operator
        self.operators = ["/","*","+","-"]

        # this is for changing the icon of the tab
        self.icon = "Calculatorlogo.png"

        # this is for first use
        self.last_was_operator = None
        self.last_button = None

        # this is for layout
        main_layout = BoxLayout(orientation = "vertical")
        # this is our output screen
        self.solution = TextInput(background_color = "black",foreground_color = "white",multiline = False, halign ="right", font_size=50, readonly = True)

        # we are adding in main program as widget
        main_layout.add_widget(self.solution)
        # here we have use nested list or array as the orientation is vertical
        button = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"]
        ]
        # to add the button in calculator we use for loop
        for row in button:
            h_layout = BoxLayout()
            for label in row:
                # to look button good we added properties
                button = Button(
                    text = label, font_size = 50, background_color = "grey",
                    pos_hint = {"center_x":0.5, "center_y":0.5}
                )
                # button to work
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            # finally we have added button to main layout
            main_layout.add_widget(h_layout)

        # same goes for equal
        equal_button = Button(
            text="=", font_size=50, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            # it is for clicking two operators
            if current and (self.last_was_operator and button_text in self.operators):
                return button_text
            # it is for  if there is no number then operators button should not work
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

# Created by Siddhant Garudkar
# this is our main file
class main:
    app = MainApp()
    app.run()

# we can also write as this
# if __name__ == "__main__":
#     app = MainApp()
#     app.run()




