r = .04
annual_salary = input('Annual Salary: ')
portion_saved = input('% saved: ')
total_cost = input('Total Cost: ')
semi_annual_raise = input('raise: ')
current_savings = 0
months = 0
while current_savings < (total_cost/4):
	current_savings += r/12*current_savings #monthly interest
	current_savings += annual_salary/12*portion_saved
	months +=1
	if months%6 == 0:
		annual_salary += annual_salary*semi_annual_raise
print months