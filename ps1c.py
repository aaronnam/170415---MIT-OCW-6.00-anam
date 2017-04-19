total_cost = 1000000 #total cost is $1M
down = .25 * total_cost
r = .04
semi_annual_raise = .07
annual_salary = input('Annual Salary: ')
high = 10000
low = 0
count = 0
savings = 0
found = False
months = 1

monthly_salary = annual_salary/12.0
for m in range (0,35):
	savings += monthly_salary + savings*r/12
	if months % 6 == 0:
		monthly_salary += (monthly_salary*semi_annual_raise)
	months +=1
if savings < down-100:
	print "Make more or save more"
else:
	while abs(down - savings) >= 100:
		savings = 0
		months = 1
		monthly_salary = annual_salary/12.0
		savings_rate = int(high + low)/2.0
		for m in range(0,35):
			savings += savings_rate/10000*monthly_salary + savings*r/12
			if months % 6 == 0:
				monthly_salary += (monthly_salary*semi_annual_raise)
			months +=1
		if abs(down-savings) <= 100:
			print savings_rate
			print savings
			found = True
			break
		elif down-savings > 100:
			low = savings_rate
			print low
		elif down-savings < -100:
			high = savings_rate
			print high
		count +=1
	print "Savings", savings
	print "Savings rate", savings_rate/10000
	print "Steps in bisection search:", count