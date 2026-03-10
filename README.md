# Password Generator

Un générateur de mots de passe sécurisés en Python.

## Fonctionnalités

- Génère des mots de passe aléatoires avec des critères personnalisables
- Options pour inclure/exclure majuscules, chiffres, caractères spéciaux
- Longueur personnalisable
- Génération de plusieurs mots de passe en une commande
- Garantit au moins un caractère de chaque type sélectionné

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/[votre-username]/password-generator.git
cd password-generator
```

2. Aucune installation requise - Python 3.x est suffisant.

## Utilisation

### Générer un mot de passe par défaut (12 caractères avec tout) :
```bash
python password_generator.py
```

### Options disponibles :
```bash
python password_generator.py --help
```

Exemples :
```bash
# Mot de passe de 16 caractères
python password_generator.py -l 16

# 5 mots de passe sans caractères spéciaux
python password_generator.py --no-special -n 5

# Mot de passe uniquement avec lettres minuscules et chiffres
python password_generator.py --no-upper --no-special

# Mot de passe très long (24 caractères)
python password_generator.py -l 24
```

## Exemple de sortie
```
$ python password_generator.py
$n$g!8L7@wP1

$ python password_generator.py -l 16 -n 2
Kp9@mX!z2Qv8$LrT
Y3#bN8qW!pZ2@vCx
```

## Structure du projet

- `password_generator.py` : Script principal
- `README.md` : Documentation (ce fichier)

## Licence

MIT License - libre d'utilisation et modification.

## Auteur

Généré automatiquement par LUMENA AI.

## Date

10 mars 2026