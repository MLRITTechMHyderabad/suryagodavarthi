employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
updated_employees = list(map(
    lambda emp: {**emp, "salary": round(emp["salary"] * (1.10 if emp["rating"] >= 4 else 1.05 if emp["rating"] == 3 else 0.97), 2)},
    employees
))
for emp in updated_employees:
    print(emp)

















