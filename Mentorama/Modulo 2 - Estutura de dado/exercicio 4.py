setx = set(['apple', 'mango'])
sety = set(['mango', 'orange'])
setz = set(['mango'])

u = setx | sety | setz
c = setx & sety
s = setx.issubset(sety and setz)
d = setx.difference(sety)

print(f'A união dos conjuntos vai ficar assim : {u}')
print()
print(f"O elemento comum é {c}. ")
print()
print(f"O setx é {s} para subconjunto de sety e setz. ")
print()
d = setx.difference(sety)
print(f'O elemento que não exite no sety é: {d}.')
