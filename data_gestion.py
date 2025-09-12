import pandas as pd


def get_data_csv (path_csv):
    """
    Récupère les informations du fichier .csv
    Transforme si str, puis en décimal les %
    Calcule les profits
    Retourne une liste de tuple (name, cost, benefit, profit)
    :param path_csv: chemin du fichier csv contenant la liste des actions
    :return: list des actions dans le bon format
    """
    try:
        df = pd.read_csv(path_csv, encoding="utf-8")
        actions = df.iloc[:, 0].tolist()
        costs = df.iloc[:, 1].tolist()
        if df.iloc[:, 2].dtype == type(str):
            benefits = df.iloc[:, 2].str.replace("%", "").astype(float) / 100
        else:
            benefits = df.iloc[:, 2] / 100

        profits = [round(cost * benefit, 2) for cost, benefit in zip(costs, benefits)]
        all_actions = list(zip(actions, costs, benefits, profits))

        return all_actions
    except FileNotFoundError:
        print("Le fichier utilisé est introuvable")
        return None


def clean_data(data: list[tuple[str, float, float, float]]) -> list[tuple[str, float, float, float]]:
    """
    Retire les actions dont les valeurs numériques sont égales à 0 ou négatives
    :param data: liste des actions
    :return: liste des actions moins les inutilisables
    """
    new_data = []

    for action in data:
        if all(v > 0 for v in action[1:]):
            new_data.append(action)

    return new_data