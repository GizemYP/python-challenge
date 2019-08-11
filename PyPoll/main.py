import os
import csv
print("Election Results")
print("------------------------")


candidate = []

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    name = set()

    for col in csvreader:
        candidate.append(col[2])
        name.add(col[2])
    # print(name)

    print(f"Total votes: {len(candidate)}")
    print("------------------------")
    vote_counter = {}.fromkeys(name, 0)

    for name in candidate:
        vote_counter[name] += 1
    # print(vote_counter)

    percent_votes = {
        k: str(round(v / total, 2)) + "%" for total in (sum(vote_counter.values())/100,) for k, v in vote_counter.items()}

    # print(percent_votes)

    keys = percent_votes.keys()
    values = zip(percent_votes.values(), vote_counter.values())
    final_summary = dict(zip(keys, values))

    # print(final_summary)
    for cand, values in final_summary.items():
        print(cand, ":", values[0], "(", values[1], ")")
    print("------------------------")
    max_key = max(vote_counter, key=lambda k: vote_counter[k])
    print(f"Winner: {max_key}")
    print("------------------------")
