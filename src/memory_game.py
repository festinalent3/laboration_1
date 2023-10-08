from console_manager import ConsoleManager
from memory_sequence import MemorySequence


class MemoryGame:
    def __init__(self, console_manager: ConsoleManager, sequence: MemorySequence):
        self._console_manager = console_manager
        self._sequence = sequence
        self._correct_guesses = 0

    def run(self):
        try:
            self._intro()
            self._set_and_display_sequence()
            self._guess_sequence()
        except KeyboardInterrupt:
            self._console_manager.output("\nGiving up already are we? Exiting...")
            exit(0)

    def _intro(self):
        self._console_manager.clear_console()
        intro_message = """
    ****** Welcome to Memory! ******
     _____   _____   _____   _____ 
    |  ?  | |  ?  | |  ?  | |  ?  |
    |     | |     | |     | |     |
    |_____| |_____| |_____| |_____|
    
    This game tests your ability to memorize a sequence of characters,
    the length of which you can choose.
    
    Remember that a longer sequence is harder to remember, but you will get more time to memorize it!
    
    """
        self._console_manager.output(intro_message)

    def _set_and_display_sequence(self):
        sequence_length = self._console_manager.get_value_from_user_input(
            int, "Please enter the desired length of the sequence: "
        )
        self._sequence.set_length(sequence_length)
        self._sequence.generate_sequence()
        self._console_manager.display_for_duration(
            self._sequence, self._sequence.length
        )

    def _guess_sequence(self):
        self._console_manager.output("Now it is time to test your memory!")
        self._sequence.shuffle_sequence()
        self._console_manager.output(
            "Shuffled sequence: " + " ".join(self._sequence.shuffled_sequence)
        )

        while self._correct_guesses < self._sequence.length:
            self._guess_a_character()

        self._console_manager.output("Congratulations, you won!")

    def _guess_a_character(self):
        user_guess = self._console_manager.get_value_from_user_input(
            str,
            f'Enter the {"first" if self._correct_guesses == 0 else "next"} '
            + "character of the sequence: ",
        )

        if user_guess == self._sequence.sequence[self._correct_guesses]:
            self._console_manager.output("Correct!")
            self._correct_guesses += 1
        else:
            self._console_manager.output("Incorrect, please try again.")


if __name__ == "__main__":
    game = MemoryGame(ConsoleManager(), MemorySequence())
    game.run()
