# IMPOERTING REQUIRED LIBARIES
import random
import pandas as pd
from faker import Faker

# Initialize Faker  
fake = Faker()

# Sample U.S. universities name
universities = [
    ("Harvard University", "Massachusetts"),
    ("Stanford University", "California"),
    ("Massachusetts Institute of Technology", "Massachusetts"),
    ("University of California, Berkeley", "California"),
    ("Princeton University", "New Jersey"),
    ("Yale University", "Connecticut"),
    ("Columbia University", "New York"),
    ("University of Chicago", "Illinois"),
    ("Duke University", "North Carolina"),
    ("University of Michigan", "Michigan"),
    ("University of Texas at Austin", "Texas"),
    ("University of Florida", "Florida"),
    ("Ohio State University", "Ohio"),
    ("Pennsylvania State University", "Pennsylvania"),
    ("University of Washington", "Washington"),
    ("University of Wisconsin-Madison", "Wisconsin"),
    ("Cornell University", "New York"),
    ("Brown University", "Rhode Island"),
    ("Northwestern University", "Illinois"),
    ("Johns Hopkins University", "Maryland")
]

# For Highest education levels
education_levels = ["Bachelor's", "Master's", "PhD"]

# For Job status
job_status_options = ["Employed", "Unemployed"]

# Generate dataset
students = []
for _ in range(100):
    uni, state = random.choice(universities)
    name = fake.name()
    grad_year = random.randint(2024, 2025)
    age = random.randint(22, 35)
    job_status = random.choice(job_status_options)
    education = random.choice(education_levels)

    students.append([name, grad_year, age, uni, state, job_status, education])

# Create DataFrame
df = pd.DataFrame(students, columns=[
    "Name", "Year of Graduation", "Age", "University", "State", "Job Status", "Highest Education"
])

# Save to CSV
df.to_csv("Passed_students(UN)_dataset.csv", index=False)

print("✅ Sample dataset created successfully as 'Passed_students(UN)_dataset.csv'")

# Ensuieng data shape
print(df.head())
print(df.info())
print(df.describe())
