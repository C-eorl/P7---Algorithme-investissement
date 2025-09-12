def knapsack_algo(actions: list[tuple[str, float, float, float]], budget: int):
    """
    algorithme Knapsack
    :param actions: list[(name, cost, benefit, profit), ...]
    :param budget: bugdet max a utilisé
    :return: la meilleure combinaison d'action, le profit et le coût de la combinaison
    """

    budget = int(budget * 100) # convertion en centime pour index table
    nb_actions = len(actions)
    # initialisation
    table = [[0] * (budget + 1) for _ in range(nb_actions + 1)]

    # algo
    for i in range(1, nb_actions+1):
        for w in range(budget+1):
            cost = int(actions[i-1][1] * 100)
            profit = actions[i-1][3]
            if cost <= w:
                table[i][w] = max(profit + table[i-1][w - cost], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    # récuperation résultat
    w = budget
    i = nb_actions
    action_resultat = []
    while i > 0 and w > 0:
        cost = int(actions[i-1][1] * 100)
        if table[i][w] != table[i-1][w]:
            action_resultat.append(actions[i-1])
            w = w - cost
            i -= 1
        else:
            i -= 1

    action_resultat.reverse()
    best_profit = sum(action[3] for action in action_resultat)
    best_combo = [action[0] for action in action_resultat]
    best_cost = sum(action[1] for action in action_resultat)

    return best_combo, best_profit, best_cost


if __name__ == "__main__":
    pass