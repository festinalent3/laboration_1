import os
import time


class ConsoleManager:
    def output(self, text: str):
        print(text)

    def clear_console(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")

    def display_for_duration(self, text: str, duration: int):
        print(text)
        time.sleep(duration)
        self.clear_console()

    def get_value_from_user_input(self, data_type: int | str, prompt: str):
        while True:
            user_input = input(prompt)
            try:
                return data_type(user_input)
            except ValueError:
                print("Invalid input, please try again. (Ctrl+C to exit)")
