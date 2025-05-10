import regex as re
from os import startfile
from sys import argv



extra_file = open('subst_corpus.dic', 'w', encoding="UTF-16 LE")
extra_file.write(u'\ufeff')

subst_step1 = open('subst.dic', 'r', encoding="UTF-16 LE").read().replace(u'\ufeff', '').split("\n")
subst_step1.remove('')
dict_result = {med[0:-9] for med in subst_step1}


corpus_set = {}
substance_pattern = '^[ 0-9\tØ-]*([A-Za-zéèê]{3,})( LP)?[ :]*?(\d+(\.\d+|,\d+)?|(un|deux|trois|quatre|cinq|six|sept|huit|neuf|dix)[ ])[ :]*?(mg|U[ ]|UI|g|µg|ml|[,: ]?[ ]?\d*?(/j|sachet(s)?))'
f = open(argv[1], 'r', encoding="UTF-8").read().replace(u'\u00A0',' ')
subst = re.findall(substance_pattern, f, re.I | re.M)
for sub in subst:
    extra_file.write(f'{sub[0].lower()},.N+subst\n')
extra_file.close()
corpus_set = {i[0].lower() for i in subst}

final_result_enrichir = list(dict_result.union(corpus_set))
enrichissement = list(corpus_set.difference(dict_result))
final_result_enrichir.sort()
enrichissement.sort()
print(enrichissement)

finaldict_subst_enrichir = open('subst.dic', 'w', encoding="UTF-16 LE")
finaldict_subst_enrichir.write(u'\ufeff')
for elt in final_result_enrichir:
    finaldict_subst_enrichir.write(f'{elt},.N+subst\n')
finaldict_subst_enrichir.close()

l = list(corpus_set)
l.sort()

letter_marker = 'a'
letter_counter = 0
total_counter = 0
f2 = open('infos2.txt', 'w', encoding="UTF-8")
for k in l:
    while (letter_marker != k[0]):
        f2.write("=========================================================================\n")
        f2.write(f'{letter_marker.upper()}: {letter_counter}\n')
        f2.write("=========================================================================\n")
        letter_marker = chr(ord(letter_marker)+1)
        total_counter += letter_counter
        letter_counter = 0 
    f2.write(k+"\n")
    letter_counter += 1

f2.write("=========================================================================\n")
f2.write(f'{letter_marker.upper()}: {letter_counter}\n')
f2.write("=========================================================================\n")
f2.write(f'Nombre total de substances actives: {total_counter}')
f2.close()

letter_marker = 'a'
letter_counter = 0
total_counter = 0
f3 = open('infos3.txt', 'w', encoding="UTF-8")
for doc in enrichissement:
    while (letter_marker != doc[0]):
        f3.write("=========================================================================\n")
        f3.write(f'{letter_marker.upper()}: {letter_counter}\n')
        f3.write("=========================================================================\n")
        letter_marker = chr(ord(letter_marker)+1)
        total_counter += letter_counter
        letter_counter = 0 
    f3.write(doc+"\n")
    letter_counter += 1
f3.write("=========================================================================\n")
f3.write(f'{letter_marker.upper()}: {letter_counter}\n')
f3.write("=========================================================================\n")
f3.write(f'Nombre total de substances actives: {total_counter}')
f3.close()
