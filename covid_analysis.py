import rki

dates, cases = rki.get_cases_last7days("Gesamt")
print (cases)


dates, cases = rki.get_cases_last7days("Berlin")
print (cases)