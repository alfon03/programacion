'''
Created on Nov 29, 2022

@author: alfonso
'''

print("DIVE es un dispositivo que muestra"
"los estímulos en una pantalla de alta resolución y capta"
"la mirada mediante un rastreador ocular. Además, usará una"
"nueva versión de software de cribado e incorporará el móvil"
"Huawei P50 y la tablet Huawei Matebook E para mejorar su"
"calidad y la precisión.")
c=input("Character to look for: ")
counter= ("DIVE es un dispositivo que muestra"
"los estímulos en una pantalla de alta resolución y capta"
"la mirada mediante un rastreador ocular. Además, usará una"
"nueva versión de software de cribado e incorporará el móvil"
"Huawei P50 y la tablet Huawei Matebook E para mejorar su"
"calidad y la precisión.")
def charactersInString ():
    contador=0
    for i in (counter):
        if i.upper()==c or i.lower()==c:
            contador+=1
    return contador
print(f"In this text the entered character {c} is repeated {charactersInString()} times throughout the text.")