#!/usr/bin/env python3
"""
Générateur de mots de passe sécurisés
"""

import random
import string
import argparse
import sys

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Génère un mot de passe aléatoire avec les critères spécifiés.
    """
    chars = string.ascii_lowercase
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if not chars:
        raise ValueError("Au moins un type de caractère doit être sélectionné")
    
    # Garantir au moins un caractère de chaque type sélectionné
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    # Remplir le reste avec des caractères aléatoires
    remaining = length - len(password)
    if remaining < 0:
        # Si la longueur est trop courte, ajuster
        password = password[:length]
        remaining = 0
    
    password.extend(random.choice(chars) for _ in range(remaining))
    
    # Mélanger pour éviter les patterns prévisibles
    random.shuffle(password)
    
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Générateur de mots de passe sécurisés')
    parser.add_argument('-l', '--length', type=int, default=12, help='Longueur du mot de passe (défaut: 12)')
    parser.add_argument('--no-upper', action='store_true', help='Exclure les majuscules')
    parser.add_argument('--no-digits', action='store_true', help='Exclure les chiffres')
    parser.add_argument('--no-special', action='store_true', help='Exclure les caractères spéciaux')
    parser.add_argument('-n', '--count', type=int, default=1, help='Nombre de mots de passe à générer (défaut: 1)')
    parser.add_argument('--version', action='version', version='Password Generator 1.0')
    
    args = parser.parse_args()
    
    try:
        for i in range(args.count):
            password = generate_password(
                length=args.length,
                use_uppercase=not args.no_upper,
                use_digits=not args.no_digits,
                use_special=not args.no_special
            )
            print(password)
    except ValueError as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()