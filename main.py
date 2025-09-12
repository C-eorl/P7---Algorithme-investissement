import argparse
import time
from colorama import Fore, Style, init
from data_gestion import get_data_csv, clean_data

from algorithmes.optimized import knapsack_algo
from algorithmes.bruteforce import bruteforce_algo
from algorithmes.greedy import greedy_algo

def display_result(result: dict):
    init(autoreset=True)
    print(f"\n{Fore.CYAN}=== Résultat - utilisation algorithme {result['algo_used']} ==={Style.RESET_ALL}\n")
    print(f"{Fore.CYAN}Temps d'éxécution du script:{Style.RESET_ALL} {result['time']:.4f} secondes")
    print(f"{Fore.CYAN}Fichier utilisée:{Style.RESET_ALL} {result['path_file']}")
    print(f"{Fore.CYAN}Totals d'actions :{Style.RESET_ALL} {result['number_actions']} - {Fore.CYAN}Totals d'action valide :{Style.RESET_ALL} {result['number_valid_actions']}")
    print(f"{Fore.CYAN}Budget max :{Style.RESET_ALL} {result['budget']} euros")
    print(f"{Fore.CYAN}Meilleure combinaison d'actions :{Style.RESET_ALL} \n{result['best_combo']}")
    print(f"{Fore.CYAN}Profit total :{Style.RESET_ALL} {result['best_profit']} euros")
    print(f"{Fore.CYAN}Cout total :{Style.RESET_ALL} {result['best_cost']} euros")
    print("\n" + 50*f"{Fore.CYAN}=")

def main():
    """
    Fonction principal:
        - Initialise les arguments du script
        - Lance un timer
        - Récupère les données
        - Nettoie les données
        - Traite les donnée via algorithmes
        - Initialise dict de donnée des résultats
        - Affiche les données des résultats

    """
    algorithmes = {
        "optimized": knapsack_algo,
        "bruteforce": bruteforce_algo,
        "greedy": greedy_algo
    }
    parser = argparse.ArgumentParser(description="Algorithme d'investissement")
    parser.add_argument("path_file", help="Chemin du fichier des actions")
    parser.add_argument("budget", type=int, help="budget maximum en euros" )
    parser.add_argument(
        "--algo",
        choices=list(algorithmes.keys()),
        default="optimized",
        help="Algorithme à utiliser (bruteforce, optimized, greedy). Défaut : optimized")
    args = parser.parse_args()

    data_actions = get_data_csv(args.path_file)
    if data_actions is None:
        print("Le script ne peut aller plus long\nFermeture")
        return

    actions_clean = clean_data(data_actions)
    start = time.perf_counter()
    algo_func = algorithmes[args.algo]
    result = algo_func(actions_clean, args.budget)
    end = time.perf_counter()

    dict_result = {
        "path_file": args.path_file,
        "algo_used": args.algo,
        "number_actions": len(data_actions),
        "number_valid_actions": len(actions_clean),
        "budget": args.budget,
        "best_combo": result[0],
        "best_profit": result[1],
        "best_cost": result[2],
        "time": end - start
    }
    display_result(dict_result)

if __name__ == "__main__":
    main()