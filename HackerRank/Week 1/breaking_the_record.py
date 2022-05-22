"""
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season 
record for most points and least points in a game. 
Points scored in the first game establish her record 
for the season, and she begins counting from there.

Ex.
scores = [12,24,10,24]
Returns 2 integers 
"""


def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    min_record = 0
    max_record = 0
    
    for i in range(1, len(scores)):
        if min > scores[i]:
            min = scores[i]
            min_record += 1
        elif max < scores[i]:
            max = scores[i]
            max_record += 1

    return max_record, min_record


def main():
    print(breakingRecords([12, 24, 10, 24]))  # EXPECTED 1,1


if __name__ == '__main__':
    main()
