"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in bangalore are calls
to other fixed lines in bangalore."
The percentage should have 2 decimal digits
"""

def is_bagalore_area_number(tele_nums):
    if tele_nums[0:5] == "(080)":
        return True
    else:
        return False

def get_area_code(tele_nums):
    assert(tele_nums[0] == "(")
    return tele_nums[0:tele_nums.find(")") + 1]

def get_mobile_prefix(tele_nums):
    assert(tele_nums[0] in ("7","8","9"))
    return tele_nums[0:4]

def find_all_bangalore_have_codes(calls):
    codes = set()
    for call in calls:
        incoming = call[0]
        if is_bagalore_area_number(incoming):
            answering = call[1]
            f_num = answering[0]

            if f_num == "(":
                codes.add(get_area_code(answering))
            elif f_num in ("7","8","9"):
                codes.add(get_mobile_prefix(answering))
            elif answering[0:3] == "140":
                codes.add("140")

    return sorted(list(codes))

def get_pct_of_call_fixed_lines_in_bangalore(calls):
    call_count = 0
    call_fixed_lines_count = 0

    for call in calls:
        if is_bagalore_area_number(call[0]):
            call_count += 1
            if is_bagalore_area_number(call[1]):
                call_fixed_lines_count += 1

    pct = (call_fixed_lines_count / call_count) * 100 
    return "{:.2f}".format(pct)

def main():
    # Part A
    codes = find_all_bangalore_have_codes(calls)
    print("The numbers called by people in Bangalore have codes:")
    for code in codes:
        print(code)
    
    # Part B
    pct = get_pct_of_call_fixed_lines_in_bangalore(calls)
    print(
        "{} percent of calls from fixed lines in bangalore are calls to other fixed lines in bangalore."
        .format(pct)
    )

if __name__ == "__main__":
    main()

