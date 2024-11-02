manager = 'abcdefghijklmnopqrstuvwxyz'
hmm = [list(manager[i:] + manager[:i]) for i in range(len(manager))]

def crew_member(textus):
     hope = ''
     for i in range(len(textus)):
          symb = textus[i]
          if(symb.isalpha()) == True:
               if (ord(symb) + 9 > 100):
                    symb = manager[(manager.index(symb)+13) % 26]
               elif ord(symb) >= 78:
                    symb = chr(ord(symb) + 19).upper()
               else:
                    symb = chr(ord(symb) + 45).upper()
          hope += symb
     return(hope)

def alert(hmm, textus):
     encrypted_message = ''
     for i in range(len(textus)):
          if (i + 1) == len(textus):
               impo,ster = textus[i-1].lower(),textus[i-2].lower()
               impo = hmm[0].index(impo)
               for v in range(26):
                    if hmm[v][0] == ster:
                         ster = v
                         break
               imposter = hmm[impo][ster] #!!!
               if (ord(textus[i]) + 9 < 100):
                    imposter = imposter.upper()
               encrypted_message += imposter

          elif not textus[i].isalpha():
               emerg,ency = hmm[0].index(textus[i+1].lower()),0
               for s in range(26):
                    if hmm[s][0] == textus[i-1].lower():
                         ency = s
                         break
               encrypted_message += hmm[emerg][ency]

          else:
               amo = hmm[0].index(textus[i].lower())
               if textus[i-1].isalpha():
                    for j in range(26):
                         if hmm[j][0] == textus[i-1].lower():
                              gus = j
                              break
               else:
                    for j in range(26):
                         if textus[i-2].lower() != 0 and hmm[j][0] == textus[i-2].lower():
                              gus = j
                              break
               amogus = hmm[amo][gus]  # !!!
               if (ord(textus[i]) + 9 < 100):
                    amogus = amogus.upper()
               encrypted_message += amogus
     return encrypted_message

text = input("Enter your message: ")
print("Blue last wish:",alert(hmm,crew_member(text)))

# Blue last wish: EOVYnnubdglxvzzassmabtamjjvhllallalmmubdglxvrrlpvkwwhetazzgihqvv
