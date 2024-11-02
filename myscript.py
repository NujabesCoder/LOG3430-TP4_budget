import os
import sys

# Obtenir les hachages des commits "mauvais" et "bon"
badhash = os.getenv("BAD_HASH", "c1a4be04b972b6c17db242fc37752ad517c29402")  # exemple de hash mauvais
goodhash = os.getenv("GOOD_HASH", "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")  # exemple de hash bon

# Fonction principale pour exécuter git bisect
def run_bisect():
    os.system(f"git bisect start {badhash} {goodhash}")
    # Utilisation de pytest pour exécuter les tests à chaque étape de bisect
    result = os.system("git bisect run pytest")
    os.system("git bisect reset")
    sys.exit(result)

if __name__ == "__main__":
    run_bisect()
