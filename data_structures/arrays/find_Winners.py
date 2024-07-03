# In this problem, we are given an array matches consisting of matches [winner, loser] where winner defeats loser.

# We need to collect these 2 kinds of players into two lists separately:

# players that have not lost any matches.
# players that have lost exactly one match.
# then return the two lists in increasing order.

from collections import Counter

def findWinners(matches: list[list[int]]) -> list[list[int]]:
    losses_count = Counter()
    for winner, loser in matches:
        losses_count[loser] += 1
        losses_count[winner] += 0
    
    winners = []
    almost_winners = []
    for player, losses in losses_count.items():
        if losses == 0:
            winners.append(player)
        elif losses == 1:
            almost_winners.append(player)
    
    return [sorted(winners), sorted(almost_winners)]


