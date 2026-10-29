# Largest Concatenate

A Python solution that arranges individual digits into the largest possible number. For `[2, 3, 9, 2, 2]`, the result is **93222**.

[largest_concatenate.py](largest_concatenate.py) repeatedly selects the largest remaining digit, appends it to a string, and removes it from the input list.

This version is for digits from 0 to 9. Sorting by numeric value does not always produce the largest concatenation for numbers with multiple digits.
