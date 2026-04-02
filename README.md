# ROA-groupe28
recherche arborescente monte carlo 

La Recherche arborescente Monte-Carlo (Monte Carlo Tree Search, MCTS) est une
méthode d’exploration de grands espaces de décision basée sur la simulation aléatoire.

Elle construit progressivement un arbre de recherche en simulant des parties ou des
séquences d’actions et en utilisant les résultats pour estimer la qualité des décisions.

MCTS combine quatre phases principales : sélection, expansion, simulation (ou playout),
et mise à jour des valeurs. Cette approche est particulièrement efficace pour les jeux
à information parfaite (comme le Go ou les échecs), les problèmes de planification et
certains problèmes d’optimisation stochastique.

Par exemple, dans un jeu de morpion, MCTS simule de nombreuses parties aléatoires
depuis l’état courant pour estimer quelle action offre les meilleures chances de victoire,
et construit progressivement un arbre qui guide le choix du coup optim
