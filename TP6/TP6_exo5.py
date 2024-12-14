import unicodedata
import string

def nettoyer_texte(texte):
    # Supprimer la ponctuation et les espaces
    texte_sans_ponctuation = texte.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    return texte_sans_ponctuation

def normaliser_caracteres(texte):
    # Normaliser les caractères accentués
    texte_normalise = unicodedata.normalize('NFD', texte)
    texte_sans_accent = ''.join(c for c in texte_normalise if unicodedata.category(c) != 'Mn')
    return texte_sans_accent

def est_palindrome(texte):
    # Vérifier si le texte est un palindrome
    texte_nettoye = nettoyer_texte(texte)
    texte_normalise = normaliser_caracteres(texte_nettoye).lower()
    return texte_normalise == texte_normalise[::-1]

def main():
    phrase = input("Entrez un mot ou une phrase : ")
    if est_palindrome(phrase):
        print("C'est un palindrome.")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()