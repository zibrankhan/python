from faker import Faker
fake=Faker()
for i in range(100):
    print('Employee Name: ', fake.name())
    print('Employee Name: ', fake.first_name())
    print('Employee Name: ', fake.last_name())
    print('Employee ID: ', fake.random_number(5))
    print('Employee DOB: ', fake.date())
    print('Employee Email ID: ', fake.email())
    print('Employee Alternative no. : ', fake.random_int(min=0, max=9999))
    print('Employee Role : ', fake.random_element(elements=('soft Er', 'Team Lead', 'CEO')))
    print()
