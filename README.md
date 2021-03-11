## Task0:
Worst-case time complexity is O(1).
The time-complexity for this program is O(1) because we are not iterating the
elements from input lists(calls or texts). We are accessing the first and last
values from the lists (calls and texts) by an index.


## Task1:
Worst-case time complexity is O(n).
The time-complexity for this program is O(n) because we are iterating the
elements from input lists(calls and texts). In this iteration, the add()
has a time-complexity of O(1). We can express it like this O(2n+4+1).
2n = Two lists(calls and texts) iteration, 4 = add(), 1 = len()
So the simplification of this run time analysis is O(n).

Worst-case space complexity is O(n).
The space-complexity for this program is O(n) because worst-case is all
numbers are unique.
So the length of unique_tele_nums is n, therefore, worst-case is O(n).



## Task2:
Worst-case time complexity is O(n).
The time-complexity for this program is O(n) because we are iterating the
elements from input lists(calls and texts). In this iteration, the time-complexity
of storing the dictionary(spent_time) is O(1). And max() is O(n). And list accessing
is O(1). We can express it like this O(2n+3).
So the simplification of this run time analysis is O(n).

Worst-case space complexity is O(n).
The space-complexity for this program is O(n) because worst-case is all
numbers are unique.

telephone_number = O(1)
logest_total_time = O(1)
spent_time = O(n)
O(n+2) = O(n)


## Task3:
Worst-case time complexity is O(n log n + n*s).
The time-complexity for this program is O(n log n + n*s) because the largest order is
sorted() and finding a specific character in the string in the iteration(calls).
The first function find_all_bangalore_have_codes has a few simple functions.

```
is_bagalore_area_number: O(1)
  string slice: O(5-0) = O(5)
get_area_code: O(s)
  accessing from string by an index: O(1)
  find: O(n), n = string length
get_mobile_prefix: O(1)
  accessing from string by an index: O(1)
  check tuples: O(3)
  string slice: O(4-0) = O(4)
```

And adding to the set has a complexity of O(1) and finally sorting the list has
complexity of O(n log n). We can express it like this O(n log n + n*s + 2).
And the second function get_pct_of_call_fixed_lines_in_bangalore is similar to
the first function but we are not sorting from the list. This just returns a value
therefore is O(n). So simplification of this run time analysis is O(n log n + n*s).

Worst-case space complexity is O(n).
The space-complexity for this program is O(n) because worst-case is all codes of
numbers are unique.


## Task4:
Worst-case time complexity is O(n log n).
The time-complexity for this program is O(n log n) because the largest order is
sorted(). add() is O(1), iterating over a list(calls and texts) is O(n),
difference() is O(len(c=calls length) + len(t=texts length)), list() is O(n)
And sorted() is O(n log n).

O(n log n) > O(n) > O(1)

So the simplification of this run time analysis is O(n log n).

Worst-case space complexity is O(n).
This space-complexity for this program is O(n) because we are storing the
elements from input lists(calls and texts). Worst-case is all numbers are unique.
outgoing = O(n), non_tele = O(3n), tele = O(4n)
So simplification is O(n).

