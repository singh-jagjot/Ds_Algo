from typing import List


def non_constructible_change(coins: List):
    coins.sort()
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin

    return current_change + 1
