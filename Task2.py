"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
task 2: which telephone number spent the longest time on the phone
during the period? don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def find_number_and_longest_time(calls):
    telephone_number = ""
    logest_total_time = 0
    spent_time = {}

    for call in calls:
        incoming, answering, _, during = call
        if incoming in spent_time:
            spent_time[incoming] += int(during)
        else:
            spent_time[incoming] = int(during)

        if answering in spent_time:
            spent_time[answering] += int(during)
        else:
            spent_time[answering] = int(during)

    telephone_number = max(spent_time, key = lambda k: spent_time[k])
    logest_total_time = spent_time[telephone_number]

    return telephone_number, logest_total_time

def main():
    telephone_number, logest_total_time = find_number_and_longest_time(calls)
    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016."
        .format(telephone_number, logest_total_time)
    )
    
if __name__ == "__main__":
    main()

