def greedy_algo(actions: list[tuple[str, float, float, float]], budget):
    # liste trié en fonction du ratio profit/cout
    list_sort_action = sorted(actions, key=lambda x: x[3] / x[1], reverse=True)

    # initialisation
    best_profit = 0
    best_cost = 0
    best_combo = []

    for action in list_sort_action:
        cost_action = action[1]
        profit_action = action[3]
        if best_cost + cost_action <= budget:
            best_combo.append(action)
            best_cost += cost_action
            best_profit += profit_action

    best_combo = [action[0] for action in best_combo]
    return best_combo, best_profit, best_cost
