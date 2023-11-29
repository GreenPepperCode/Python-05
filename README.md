# Python-05 : Fichiers-Modules-Fonctions

## Contexte :
Se familiariser avec l’utilisation des fichiers et les Modules dans le langage Python.

## Mot clé (= notion à apprendre) :
1. Modules : En Python, un module est un fichier contenant du code Python. Il peut inclure des fonctions, des classes et des variables, et est souvent utilisé pour organiser et réutiliser du code.
2. Bibliothèque : Une collection de modules. Une bibliothèque fournit des fonctionnalités supplémentaires non présentes dans le langage de base, comme des opérations mathématiques avancées, des interactions avec le système d'exploitation, etc.
3. Importer : Le mot-clé import en Python est utilisé pour accéder au code contenu dans un autre module ou bibliothèque.
4. Framework : Un cadre de travail (framework) est un ensemble de bibliothèques ou de modules qui fournissent une structure pour développer des applications spécifiques (comme des applications web ou des jeux).
5. Fichier : Dans le contexte de la programmation, un fichier est un document stockant des données sur le disque dur, que ce soit du code, du texte, des images, etc.
6. CSV : Format de fichier texte pour stocker des données tabulaires. CSV signifie "Comma-Separated Values" (valeurs séparées par des virgules).
7. Pandas : Une bibliothèque Python populaire pour l'analyse de données. Elle offre des structures de données et des outils pour manipuler et analyser facilement des ensembles de données.
8. Random : Un module Python utilisé pour générer des nombres aléatoires ou effectuer des sélections aléatoires.
9. Math : Un module Python fournissant des fonctions mathématiques standard telles que l'exponentiation, la racine carrée, le logarithme, etc.
10. Matplotlib : Une bibliothèque de visualisation de données en Python. Elle est utilisée pour créer des graphiques et des visualisations de données statiques, animées et interactives.
11. Numpy : Une bibliothèque pour le calcul scientifique en Python. Elle fournit un support pour les grands tableaux et matrices multi-dimensionnelles, ainsi que pour une large gamme de fonctions mathématiques de haut niveau.
12. Dataframe : Une structure de données bidimensionnelle, similaire à une table de base de données, utilisée dans Pandas. Elle est composée de lignes et de colonnes et peut stocker différents types de données.
13. Package : Ensemble de modules Python regroupés. Un package peut contenir un ou plusieurs modules et est utilisé pour distribuer et organiser le code Python de manière structurée.

Problématique (forme de question, il peut y en avoir plusieurs)
- Comment manipuler un fichier en utilisant des modules ? 
- Comment importer et installer des librairies ?
- Comment créer un module ?
- Comment les modules facilitent les manipulations des données en python ?

## Hypothèses Vrai-Faux (à la fin)
1. Patrick : Toutes les bibliothèques sont utilisables gratuitement.
   - Plutôt Faux. Beaucoup de bibliothèques Python sont gratuites et open-source, mais certaines bibliothèques, en particulier celles destinées à un usage professionnel, peuvent être payantes.
2. Hadjer : Une bibliothèque est un ensemble de modules.
   - Vrai. Une bibliothèque Python est effectivement un ensemble de modules qui fournissent des fonctionnalités supplémentaires.
3. Salah : On peut se passer de bibliothèques.
   - Plutôt Vrai. Il est possible de programmer en Python sans utiliser de bibliothèques externes, mais les bibliothèques rendent souvent le développement plus rapide et plus facile.
4. Il n’y a pas de différence entre bibliothèque et librairie.
   - Faux. En informatique, une "bibliothèque" (library en anglais) est un ensemble de fonctions et de modules. Le terme "librairie" est parfois utilisé à tort pour désigner une bibliothèque en français, mais ne devrait pas l'être.
5. Raphaël : on peut lire toutes extensions de fichiers.
   - Plutôt Vrai. Python peut lire la plupart des formats de fichiers, mais cela peut nécessiter des bibliothèques spécifiques pour certains formats.
6. Une librairie est plus petite qu’une bibliothèque.
   - Faux. Comme indiqué précédemment, le terme "librairie" ne devrait pas être utilisé pour désigner une bibliothèque en informatique.
7. Thibaut : il est possible d’ouvrir un fichier en lecture et écriture.
   - Vrai. Python permet d'ouvrir des fichiers en mode lecture-écriture.
8. Alexis : Les bibliothèques ralentissent le programme.
   - Plutôt Faux. Les bibliothèques peuvent ajouter des fonctionnalités et de la complexité, mais elles ne ralentissent pas nécessairement le programme. En fait, certaines bibliothèques sont optimisées pour améliorer les performances.
9. Hassan : On peut écrire dans tous types de fichiers.
   - Plutôt Vrai. Python est capable d'écrire dans différents types de fichiers, bien que cela puisse nécessiter des bibliothèques spécifiques pour certains formats.
10. Certains modules s’appuient sur d’autres modules.
   - Vrai. Il est courant en Python que des modules dépendent d'autres modules.
11. Alexandre : c’est facile d’importer une librairie.
   - Plutôt Vrai. Importer une bibliothèque (le terme correct) en Python est généralement simple, à condition qu'elle soit installée.
12. Ahmed : Pour utiliser certaines fonctions il faut importer une librairie.
   - Vrai. Pour utiliser des fonctions qui ne sont pas dans les modules standards de Python, il faut importer les bibliothèques correspondantes.
13. Munkherdene : une bibliothèque est une boite à outils.
   - Vrai. C'est une bonne métaphore pour décrire une bibliothèque, qui offre un ensemble d'outils (fonctions, classes) pour réaliser certaines tâches.
14. Pour ouvrir et fermer un fichier correctement, il faut minimum 4 lignes.
   - Plutôt Faux. Avec l'instruction with en Python, on peut ouvrir et fermer un fichier proprement en moins de 4 lignes.
15. Philippe : Il faut effectuer plusieurs opérations pour écrire dans un fichier.
   - Plutôt Vrai. Écrire dans un fichier implique généralement d'ouvrir le fichier, d'écrire les données, et de fermer le fichier.
16. Bart : il faut fermer un fichier proprement pour éviter la corruption des données.
   - Vrai. Il est important de fermer correctement les fichiers pour assurer l'intégrité des données.
17. Paul : Une bibliothèque est un fichier python.
   - Plutôt Faux. Une bibliothèque peut être composée de plusieurs fichiers Python (modules).
18. On peut importer une librairie partiellement.
   - Vrai. En Python, il est possible

## Plan d’action :
- Explorer les ressources
- Définir les mots clés
- Vérifier les hypothèses
- Tester toutes les notions abordées sur un fichier Jupyter Notebook à rendre sur GitHub
- Finaliser le RER