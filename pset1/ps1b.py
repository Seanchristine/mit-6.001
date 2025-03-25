#pset1B
annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter your portion saved"))
total_cost=float(input("Enter your total cost"))
semi_annual_raise=float(input("Enter your semi annual raise"))
portion_down_payment=0.25*total_cost
current_savings=0
r=0.04
additional=r/12
number_of_month=0
while current_savings<portion_down_payment: 
    
    monthly_salary=annual_salary*portion_saved/12
    current_savings+=monthly_salary+(current_savings*additional)
    number_of_month+=1
    if number_of_month%6==0:
        annual_salary+=(annual_salary*semi_annual_raise)
        
print("Number of months",number_of_month);