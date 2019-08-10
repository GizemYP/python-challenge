import os
import csv
print("Eleection Results")
print("------------------------")


val = []
candidate = []

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for col in csvreader:
        val.append(col)
        candidate.append(col[2])
        votes = len(val)

    print(f"Total Votes: {votes}")
    print("------------------------")

    Khan = 0
    Correy = 0
    Li = 0
    oTooley = 0
    c_win = ["Khan", "Correy", "Li", "O'Tooley"]
    c_tot = []

    for obj in candidate:
        if obj == "Khan":
            Khan += 1
        elif obj == "Correy":
            Correy += 1
        elif obj == "Li":
            Li += 1
        elif obj == "O'Tooley":
            oTooley += 1
    c_tot.append(Khan)
    c_tot.append(Correy)
    c_tot.append(Li)
    c_tot.append(oTooley)

    print(f"Khan: {round(Khan/len(val) *100,3)}% {c_tot[0]}")
    print(f"Correy: {round(Correy/len(val) *100,3)}% {c_tot[1]}")
    print(f"Li: {round(Li/len(val) *100,3)}% {c_tot[2]}")
    print(f"O'Tooley: {round(oTooley/len(val) *100,3)}% {c_tot[3]}")
    print("------------------------")

    winner = c_win[c_tot.index(max(c_tot))]
    print(f"Winner: {winner}")
    print("------------------------")
