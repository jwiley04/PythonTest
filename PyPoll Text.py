import os
import csv

file = os.path.join('election_data.csv')

  
poll = {}
total_votes = 0


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

   

    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 

candidates = []
votes = []


for key, value in poll.items():
    candidates.append(key)
    votes.append(value)


vote_percentage = []
for n in votes:
    vote_percentage.append(round(n/total_votes*100, 3))


combined_data = list(zip(candidates, votes, vote_percentage))


winner_order = []

for name in combined_data:
    if max(votes) == name[1]:
        winner_order.append(name[0])


first_place = winner_order[0]


if len(winner_order) > 1:
    for w in range(1, len(winner_order)):
        first_place = first_place + ", " + winner_order[w]


output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in combined_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + first_place + '\n-------------------------')


with open(output_file, 'r') as readfile:
    print(readfile.read())