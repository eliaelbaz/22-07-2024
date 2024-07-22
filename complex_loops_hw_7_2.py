# 2
topic = input("Enter the topic of the vote: ");
votes = [];
count_for = 0;
count_against = 0;
count_abstain = 0;
first_for = None
last_against = None
for i in range(44):
    try:
        vote = int(input(f"Enter the vote for country {i + 1} (1=for, 2=against, 3=abstain, 4=veto): "));

        if vote not in [1, 2, 3, 4]:
            print("Invalid vote. Please enter a number between 1 and 4.");
            continue
        votes.append(vote);
        if vote == 1:
            count_for += 1;
            if first_for is None:
                first_for = i + 1;
        elif vote == 2:
            count_against += 1;
            last_against = i + 1;
        elif vote == 3:
            count_abstain += 1;
        elif vote == 4:
            print(f"Veto was cast by country {i + 1}.");
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.");
        break
else:
    print("The voting process is complete.");
    print(f"Votes for: {count_for}");
    print(f"Votes against: {count_against}");
    print(f"Abstain votes: {count_abstain}");
    if first_for:
        print(f"The first country that voted for is country number {first_for}.");
    if last_against:
        print(f"The last country that voted against is country number {last_against}.");
print("Collected votes:", votes);
