'''
Created on Nov 29, 2022

@author: alfonso
'''
s = ("DIVE es un dispositivo que muestra"
"los estímulos en una pantalla de alta resolución y capta"
"la mirada mediante un rastreador ocular. Además, usará una"
"nueva versión de software de cribado e incorporará el móvil"
"Huawei P50 y la tablet Huawei Matebook E para mejorar su"
"calidad y la precisión."
"En 2019 empezó la colaboración entre ambas partes," 
"logrando el primer hito ese mismo año por un estudio multicéntrico"
"en el que se examinaron a niños de diferentes edades, etnias y" 
"patologías visuales en hospitales de diversos países.")
def numberInString():
    numbers = sum(c.isdigit() for c in s)
    return numbers
print(f"In this text there are {numberInString()} numbers.")
