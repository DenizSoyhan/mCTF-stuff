manager = 'abcdefghijklmnopqrstuvwxyz'
hmm = [list(manager[i:] + manager[:i]) for i in range(len(manager))]

for i in range(len(hmm)):
     print(hmm[i])

def crew_member(textus):
     hope = ''
     for i in range(len(textus)):
          symb = textus[i]
          if(symb.isalpha()) == True:
               if (ord(symb) + 9 > 100): #ascii +9 büyükse rot13
                    symb = manager[(manager.index(symb)+13) % 26]
               elif ord(symb) >= 78:#ascii 78den büyük veya eşitse 19 EKLE büyük harf yap
                    symb = chr(ord(symb) + 19).upper()
               else:#              #diğerleri patlarsa 45 ekle büyük yap
                    symb = chr(ord(symb) + 45).upper()
          hope += symb
     return(hope)
#print(crew_member("PPP"))

def alert(hmm, textus):
     encrypted_message = ''
     for i in range(len(textus)):
          if (i + 1) == len(textus):#if last character
               impo,ster = textus[i-1].lower(),textus[i-2].lower() # ab{c} => impo=b.lower AND ster=a.lower 
               impo = hmm[0].index(impo)#hmm[0].index(impo) "b" harfinin alfabedeki indexi
               for v in range(26):
                    if hmm[v][0] == ster: #alfabedeki hangi satır v ile eşleşiyorsa onun indexi ster e verilir
                         ster = v
                         break
               imposter = hmm[impo][ster] #!!!
               if (ord(textus[i]) + 9 < 100):
                    imposter = imposter.upper()
               encrypted_message += imposter

          elif not textus[i].isalpha():#if not an alphabetic character
               emerg,ency = hmm[0].index(textus[i+1].lower()),0
               for s in range(26):
                    if hmm[s][0] == textus[i-1].lower():
                         ency = s
                         break
               encrypted_message += hmm[emerg][ency]

          else:#alphabetic and not the last character
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
#                        MESSAGE
#                      CREW MEMBER
#                         ALERT
# Blue last wish: EOVYnnubdglxvzzassmabtamjjvhllallalmmubdglxvrrlpvkwwhetazzgihqvv

