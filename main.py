import matplotlib.pyplot as plt

def chiedi_materia():
    while True:
        materia = input("Materia: ").strip()
        if materia == "":
            print("Errore: la materia non può essere vuota. Riprova.")
        elif materia.lower() == "fine":
            return "fine"
        else:
            return materia

def chiedi_voto():
    while True:
        voto_str = input("Voto (0-10): ").strip()
        try:
            voto = float(voto_str)
            if 0 <= voto <= 10:
                return voto
            else:
                print("Errore: il voto deve essere tra 0 e 10. Riprova.")
        except ValueError:
            print("Errore: devi inserire un numero valido. Riprova.")

voti = {}

print("Inserisci le materie e i voti. Scrivi 'fine' per terminare.")

while True:
    materia = chiedi_materia()
    if materia.lower() == "fine":
        break
    voto = chiedi_voto()
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
