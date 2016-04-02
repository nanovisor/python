try:
    inp = raw_input("Enter hours ")
    hours = float(inp)
    inp = raw_input("Enter rate ")
    rate = float(inp)
except:
    print "Error, please enter numeric input"
    quit()

print hours, rate
if hours <= 40 :
    pay = hours * rate
else :
    pay = 40 * rate + (rate * 1.5 * (hours - 40))
print pay
