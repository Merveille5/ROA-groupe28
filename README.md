# ♟️ Jeu du Morpion avec Intelligence Artificielle (MCTS)

## 🧠 Description

Ce projet implémente une intelligence artificielle pour jouer au **jeu du Morpion (Tic-Tac-Toe)** en utilisant l’algorithme de **Monte Carlo Tree Search (MCTS)**.

L'utilisateur joue contre une IA capable de prendre des décisions optimisées grâce à des simulations répétées et une stratégie probabiliste.

---

## 🎯 Objectif

Permettre à une IA de choisir le meilleur coup en maximisant ses chances de victoire à partir de simulations aléatoires.

---

## ⚙️ Algorithme utilisé

### 🔹 Monte Carlo Tree Search (MCTS)

L’algorithme suit 4 étapes principales :

1. **Sélection**  
   Sélection du nœud le plus prometteur via la formule UCT.

2. **Expansion**  
   Ajout d’un nouveau nœud (coup possible non exploré).

3. **Simulation (Rollout)**  
   Simulation d’une partie complète (avec heuristique).

4. **Rétropropagation**  
   Mise à jour des statistiques (victoires / visites).

---

## 📐 Formule UCT

\[
UCT = \frac{wins}{visits} + c \cdot \sqrt{\frac{\ln(N)}{visits}}
\]

où :
- `wins` : nombre de victoires  
- `visits` : nombre de visites  
- `N` : nombre total de simulations  
- `c` : constante d’exploration (≈ 1.41)

---

## 🧩 Fonctionnalités

- Jeu interactif en console  
- IA basée sur MCTS  
- Heuristique améliorée pour les simulations :
  - gagner immédiatement  
  - bloquer l’adversaire  
  - privilégier le centre  
  - privilégier les coins  
- Affichage du plateau  
- Détection automatique du gagnant  

---

## ▶️ Exécution

### 🔧 Prérequis
- Python 3.x

### 🚀 Lancer le programme

```bash
python main.py
