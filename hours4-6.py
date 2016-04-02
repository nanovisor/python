def computepay(h,r):
    if h > 40 :
        sal = 40 * r + (r * 1.5 * (h - 40.0))
        return sal
    else :
        return "sha-la-la"

hours = raw_input("Enter Hours:")
hours = float(hours)
rate = raw_input("Enter Rate:")
rate = float(rate)

print computepay(hours,rate)
