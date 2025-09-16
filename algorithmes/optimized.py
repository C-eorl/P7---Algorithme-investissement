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
    for action_index in range(1, nb_actions+1):
        for current_budget in range(budget+1):
            action_cost = int(actions[action_index-1][1] * 100)
            action_profit = actions[action_index-1][3]
            # table[i][w] = profit de l'action i par rapport a un budget w
            if action_cost <= current_budget:
                table[action_index][current_budget] = max(
                    action_profit + table[action_index-1][current_budget - action_cost],
                    table[action_index-1][current_budget]
                )
                # profit de l'action i par rapport à un budget w = soit profit de
                # l'action i + le profit optimal de l'action i-1 avec le budget restant
            else:
                table[action_index][current_budget] = table[action_index-1][current_budget]

    # récuperation résultat
    curr_budget = budget
    index_action = nb_actions
    action_resultat = []
    while index_action > 0 and curr_budget > 0:
        cost = int(actions[index_action-1][1] * 100)
        if table[index_action][curr_budget] != table[index_action-1][curr_budget]:
            action_resultat.append(actions[index_action-1])
            curr_budget = curr_budget - cost
            index_action -= 1
        else:
            index_action -= 1

    action_resultat.reverse()
    best_profit = sum(action[3] for action in action_resultat)
    best_combo = [action[0] for action in action_resultat]
    best_cost = sum(action[1] for action in action_resultat)

    return best_combo, best_profit, best_cost


if __name__ == "__main__":
    pass