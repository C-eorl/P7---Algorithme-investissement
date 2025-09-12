# 📈 Algorithme d'investissement

Ce projet permet de trouver la **meilleure combinaison d’actions** à acheter pour maximiser le profit, en respectant un budget maximal.  
Il propose 3 approches :  
- **Optimized** : utilisation de l’algorithme du sac à dos (Knapsack Dynamic Programming).  
- **Bruteforce** : test de toutes les combinaisons possibles (lent mais exhaustif).
- **Greedy** : utilisation de l’algorithme glouton
---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone git@github.com:C-eorl/P7---Algorithme-investissement.git
cd algorithme-investissement
```
### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```
#### Dépendances

- pandas → gestion des fichiers CSV
- colorama → coloration du terminal
## 📝 Utilisation

Lancer le script depuis un terminal :
```bash
python main.py <path_file> <budget> [--algo {bruteforce,optimized,greedy}]
```
**Arguments**

- path_file : chemin du fichier CSV contenant les actions
- budget : budget maximum en euros
- --algo : algorithme à utiliser
  - optimized (par défaut)
  - bruteforce
  - greedy

**Exemple**
```bash
python main.py data/actions.csv 500 --algo greedy
```
```bash
python main.py data/actions.csv 500 # par default optimized
```