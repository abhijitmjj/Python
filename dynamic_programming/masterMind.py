from itertools import product
from collections import defaultdict

# Define the six colors
color = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Purple", "Orange"]

def generate_all_codes(length, colors):
    return list(product(colors, repeat=length))

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

def knuth_mastermind(secret_code, code_length=4, colors=8, max_guesses=9):
    color_names = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Purple", "Orange"]
    all_codes = generate_all_codes(code_length, color_names)
    possible_codes = all_codes.copy()
    initial_guess = ("Black", "Red", "Green", "White")

    def next_guess(possible_codes):
        min_max_size = float('inf')
        best_guess = None
        for guess in possible_codes:
            feedback_counts = defaultdict(int)
            for code in possible_codes:
                feedback = provide_feedback(code, guess)
                feedback_counts[feedback] += 1
            max_size = max(feedback_counts.values())
            if max_size < min_max_size:
                min_max_size = max_size
                best_guess = guess
        return best_guess

    guesses = [initial_guess]
    while len(guesses) < max_guesses:
        current_guess = guesses[-1]
        feedback = provide_feedback(secret_code, current_guess)
        if feedback == (code_length, 0):
            break
        possible_codes = [code for code in possible_codes if provide_feedback(code, current_guess) == feedback]
        next_guess_value = next_guess(possible_codes)
        guesses.append(next_guess_value)
    
    # If we reached the maximum number of guesses and didn't find the code
    if len(guesses) >= max_guesses and feedback != (code_length, 0):
        print("Failed to find the secret code within the allowed number of guesses.")
    
    return guesses

# Example usage
secret_code = ("Black", "White", "Green", "Red")  # This is the secret code to guess
guesses = knuth_mastermind(secret_code)
print("Guesses:", guesses)
print("Number of guesses:", len(guesses))
