from itertools import permutations
from collections import defaultdict

# Define the eight colors
color_names = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Black", "White"]

def generate_all_codes(length, colors):
    return list(permutations(colors, length))

def provide_feedback(secret, guess):
    correct_positions = sum(s == g for s, g in zip(secret, guess))
    secret_color_counts = defaultdict(int)
    guess_color_counts = defaultdict(int)
    for s in secret:
        secret_color_counts[s] += 1
    for g in guess:
        guess_color_counts[g] += 1
    correct_colors = sum(min(secret_color_counts[color], guess_color_counts[color]) for color in secret_color_counts)
    correct_colors -= correct_positions  # Exclude the correct positions
    return (correct_positions, correct_colors)

class Mastermind:
    def __init__(self, code_length=4, num_colors=8, max_guesses=9, initial_guess=None):
        self.colors = color_names[:num_colors]
        self.code_length = code_length
        self.max_guesses = max_guesses
        self.all_codes = generate_all_codes(code_length, self.colors)
        self.possible_codes = self.all_codes.copy()
        self.guesses = []
        self.feedback = []
        self.initial_guess = initial_guess if initial_guess else self.colors[:self.code_length]

    def next_guess(self):
        if not self.guesses:
            return self.initial_guess
        min_max_size = float('inf')
        best_guess = None
        for guess in self.all_codes:
            feedback_counts = defaultdict(int)
            for code in self.possible_codes:
                feedback = provide_feedback(code, guess)
                feedback_counts[feedback] += 1
            if feedback_counts:  # Only consider guesses that have feedback counts
                max_size = max(feedback_counts.values())
                if max_size < min_max_size:
                    min_max_size = max_size
                    best_guess = guess
        return best_guess

    def make_guess(self):
        guess = self.next_guess()
        self.guesses.append(guess)
        return guess

    def receive_feedback(self, correct_positions, correct_colors):
        last_guess = self.guesses[-1]
        feedback = (correct_positions, correct_colors)
        self.feedback.append(feedback)
        self.possible_codes = [code for code in self.possible_codes if provide_feedback(code, last_guess) == feedback]

    def play(self, secret_code=None):
        for _ in range(self.max_guesses):
            guess = self.make_guess()
            print(f"Guess: {guess}")
            if secret_code:
                correct_positions, correct_colors = provide_feedback(secret_code, guess)
            else:
                correct_positions = int(input("Enter the number of correct positions: "))
                correct_colors = int(input("Enter the number of correct colors (excluding correct positions): "))
            print(f"Feedback: {correct_positions} correct positions, {correct_colors} correct colors")
            self.receive_feedback(correct_positions, correct_colors)
            if correct_positions == self.code_length:
                print("Code cracked!")
                return
        print("Failed to crack the code within the allowed number of guesses.")

# Example usage with a predefined secret code:
secret_code = ("Black", "White", "Green", "Red")  # This is the secret code to guess
initial_guess = ["Black", "Red", "Green", "White"]  # User provided initial guess
game = Mastermind(initial_guess=initial_guess)
game.play(secret_code=secret_code)

# For interactive play without a predefined secret code, comment the above lines and uncomment below:
# initial_guess = ["Red", "Yellow", "Blue", "Green"]  # User provided initial guess
# game = Mastermind(initial_guess=initial_guess)
# game.play()
