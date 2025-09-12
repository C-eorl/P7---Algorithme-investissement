from itertools import combinations

# =========================== Brute-force =========================== #

def bruteforce_algo(actions, budget):
    """
    Parcours toutes les combinaisons possibles pour trouver la meilleure combinaison
    par rapport à un budget puis la retourne.
    :param actions: list[tuple] => (name, cost, benefit, profit)
    :param budget: budget maximum en euros
    :return: (meilleure combinaison, profit total, coût total)
    """
    best_profit = 0
    best_combo = []
    best_cost = 0

    for r in range(1, len(actions) + 1):
        for combo in combinations(actions, r):
            total_cost = sum(action[1] for action in combo)  # Somme des couts par combinaison
            total_profit = sum(action[3] for action in combo)  # Somme des profits par combinaison

            if total_cost <= budget and total_profit > best_profit:
                best_profit = total_profit
                best_combo = [action[0] for action in combo]
                best_cost = total_cost

    return best_combo, best_profit, best_cost
