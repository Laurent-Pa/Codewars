import math  # ← Cette ligne manquait !

def is_square(n):
    """Vérifie si la racine carrée de n est un entier."""
    if n < 0:
        return False
    racine = math.isqrt(n)
    return racine * racine == n
