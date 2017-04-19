#Givens
total_cost = 1000000 #total cost is $1M
down = .25 * total_cost #down payment
r = .04 #return rate on investment
semi_annual_raise = .07 #raise rate
annual_salary = input('Annual Salary: ')
monthly_salary = annual_salary/12.0
high = 10000 #starting high guess for bi-sectional search. set to 10K to start as integer?
low = 0 #opposite of low
count = 0 #counter for number of guesses
savings = 0 #starting savings amount
months = 36 #number of months to save
guess_buffer = 100 #so it doesn't go into infinite loop b/c of floats?


#for loop to calculate max savings possible
for m in range (1,months):
	savings += monthly_salary + savings*r/12
	if m % 6 == 0:
		monthly_salary += (monthly_salary*semi_annual_raise)

#print statement if we can't make enough
if savings < down-guess_buffer:
	print "Make more or save more"

#bi-sectional guess if we do make enough
else:
	while abs(down - savings) >= guess_buffer:
		savings = 0 #reset savings every time we while loop
		savings_rate = int(high + low)/2.0 #why do we have to set this to int?
		monthly_salary = annual_salary/12.0 #have to reset monthly_salary b/c for loop
		count += 1 #guess counter
		for m in range(1,months):
			savings += savings_rate/10000*monthly_salary + savings*r/12
			if m % 6 == 0:
				monthly_salary += (monthly_salary*semi_annual_raise)
		if abs(down-savings) <= guess_buffer: #final answer; success print!
			print "Savings", savings
			print "Savings rate", savings_rate/10000
			print "Steps in bisection search:", count
			break
		elif down-savings > guess_buffer: #if savings not enough
			low = savings_rate
			print low, "not enough"
		elif down-savings < -guess_buffer: #if savings too high
			high = savings_rate
			print high, "too much"
	