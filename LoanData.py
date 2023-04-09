import csv

data = [
    ['income', 'credit_score', 'loan_amount', 'employment_status', 'employed', 'nth_amount'],
    [45000, 550, 8000, 'employed', 0, 18000.0],
    [55000, 620, 15000, 'employed', 0, 22000.0],
    [65000, 680, 25000, 'self-employed', 1, 26000.0],
    [75000, 720, 35000, 'employed', 0, 30000.0],
    [85000, 780, 45000, 'self-employed', 1, 34000.0]
]

with open('loan_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
