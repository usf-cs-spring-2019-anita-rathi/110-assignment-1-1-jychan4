#Assignment 1.1

#Question1

second=int(input("Enter number of seconds"))
hour=second//3600
minute=second%3600//60
seconds=second%3600%60
print("hours:",hour,"\nminutes:",minute,"\nseconds:",seconds)


#Question2
# P= Present Value
# F, Future Value = $10,000
# R = 2.99
# n = number of years

fv=10000
r=.0299
n=10
pv=fv/(1+r)**n
print("Present Value",pv)
