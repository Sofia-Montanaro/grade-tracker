import matplotlib.pyplot as plt

voti = {}

print("Inserisci le materie e i voti. Scrivi 'fine' per terminare.")
while True:
    materia = input("Materia: ")
    if materia.lower() == "fine":
        break
    voto = float(input(f"Voto per {materia}: "))
    voti[materia] = voto

if len(voti) == 0:
    print("Nessun voto inserito.")
    exit()

media = sum(voti.values()) / len(voti)
materia_migliore = max(voti, key=voti.get)
materia_peggiore = min(voti, key=voti.get)

print("\n=== RISULTATI ===")
print(f"Media voti: {media:.2f}")
print(f"Miglior materia: {materia_migliore} ({voti[materia_migliore]})")
print(f"Peggior materia: {materia_peggiore} ({voti[materia_peggiore]})")

plt.bar(voti.keys(), voti.values(), color="skyblue")
plt.title("Voti")
plt.xlabel("Materie")
plt.ylabel("Voto")
plt.ylim(0, 10)
plt.show()