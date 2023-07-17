'''This script analyzes voting numbers of election_data.csv and prints and returns a txt file of the results'''
# import packages
import csv
import os

# read thorugh csv
csv_path = os.path.join("Resources","election_data.csv")
with open(csv_path,"r",) as file:
    csv_reader = csv.reader(file,delimiter=',')
    headers = next(csv_reader)                  # get/skip headers
    cand_dict = {}
    total = 0                                   # initalize total cnt
    for row in csv_reader:
        total += 1
        if row[2] not in cand_dict:             # make dictionary key value if not in dictionary
            cand_dict[row[2]] = 1
        else:
            cand_dict[row[2]] += 1

# write to txt and print results
if not os.path.exists('analysis'):
    os.mkdir('analysis')
txt_path = os.path.join("analysis","results.txt")
with open (txt_path, "w") as file:
    file.write("Election Results\n")
    print("Election Results\n")
    file.write("-"*25)
    print("-"*25)
    file.write(f"\nTotal Votes: {total}\n")
    print(f"\nTotal Votes: {total}\n")
    file.write("-"*25)
    print("-"*25)
    win_num = 0
    for cand in cand_dict:                      # loop through to calculate and record candidate info
        if cand_dict[cand] > win_num:           # check if candidate is winner
            win_num = cand_dict[cand]
            win_cand = cand
        file.write(f"\n{cand}: {(cand_dict[cand]/total)*100:.3f}% ({cand_dict[cand]})")
        print(f"\n{cand}: {(cand_dict[cand]/total)*100:.3f}% ({cand_dict[cand]})")
    file.write("\n"+("-"*25))
    print("\n"+("-"*25))
    file.write(f"\nWinner: {win_cand}\n")
    print(f"\nWinner: {win_cand}\n")
    file.write("-"*25)
    print("-"*25)