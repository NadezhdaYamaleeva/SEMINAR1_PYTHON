# Напишите программу для проверки истинности утверждения ¬(X V Y V Z) = ¬X⋀ ¬Y⋀ ¬Z для всех значений предикат
# if not (x or y or z) == (not x and not y and z):

for x in range (2):
    for y in range (2):
        for z in range (2):
            if not (x or y or z) == (not x and not y and not z):
                print (f'Утверждение ¬(X V Y V Z) = ¬X⋀ ¬Y⋀ ¬Z истинно при x={x}, y={y}, z={z}')