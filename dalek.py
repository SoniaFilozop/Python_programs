import sys

n = 0
for i in sys.stdin:
    i = i.rstrip('\n')
    if [word for word in i.split() if word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далек' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеки' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далека' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеков' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеку' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далекам' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеком' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеками' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеке' or word.lower().strip('"').rstrip(
            ')').lstrip('(').rstrip('.').strip(',') == 'далеках']:
        n += 1
print(n)
