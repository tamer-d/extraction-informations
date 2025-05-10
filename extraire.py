from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from sys import argv, exit
from os import startfile

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
links = list()

if(argv[1][0] > argv[1][2]):
    exit("ERROR: Invalid Interval")

for i in alphabet[ord(argv[1][0].upper())-65 : ord(argv[1][2].upper())-64]:
    links.append(f'http://localhost:{argv[2]}/vidal/vidal-Sommaires-Substances-{i}.html')

subst_counter = 0
subst_total = 0
file_one = open('infos1.txt', 'w', encoding="UTF-8")
substances = list()

for link in links:
    page = urlopen(link).read()
    bs = BeautifulSoup(page, 'html5lib')
    for substance in bs.select(f'#letter{link[-6].lower()} > li'):
        substances.append(substance.find("a").string)
        subst_counter+=1
    file_one.write(f'{link[-6]}: {subst_counter} substances actives\n')
    subst_total+=subst_counter
    subst_counter = 0

file_one.write(f'\nNombre total de substances actives: {subst_total}')
file_one.close()

subdico = open('subst.dic', 'w', encoding="UTF-16 LE")
subdico.write(u'\ufeff')
for substance in substances:
    subdico.write(f'{substance},.N+subst\n')
subdico.close()