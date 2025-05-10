#-------unitex.py-------#
import os
from os import path
if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin Dela_fr.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
# Importance du fichier Alphabet.txt :
# Le fichier d'alphabet appeler "Alphabet.txt" est un fichier texte décrivant tous les caractères d'une langue
# ainsi que les correspondances entre lettres miniscules et majuscules.
# Sa présence est obligatoire pour qu'Unitex puisse fonctionner.
