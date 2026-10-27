import pandas as pd
import numpy as np

products = {
    "Laptop": "Electronics",
    "Mouse": "Electronics",
    "Keyboard": "Electronics",
    "Headphones": "Electronics",
    "Smartphone": "Electronics",
    "Monitor": "Electronics",
    "Shoes": "Fashion",
    "T-Shirt": "Fashion",
    "Backpack": "Fashion",
    "Watch": "Fashion"
}

cities = [
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Pune"
]

# Status probabilities:
# Delivered = 80%
# Returned = 10%
# Cancelled = 10%

statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Returned",
    "Cancelled"
]

First_names = [
    "Aarav", "Gurpreet", "Ayesha", "Rahul", "David",
    "Aditi", "Harpreet", "Mohammed", "Ananya", "Joseph",
    "Arjun", "Simran", "Fatima", "Aditya", "Daniel",
    "Akash", "Jaspreet", "Zoya", "Aman", "Samuel",
    "Amit", "Amrit", "Rachel", "Anjali", "Karan",
    "Aryan", "Navjot", "Ibrahim", "Priya", "Michael",
    "Ashish", "Gurman", "Sana", "Rohan", "Joshua",
    "Ayush", "Manpreet", "Arman", "Sneha", "Rebecca",
    "Chetan", "Aariz", "Maria", "Harleen", "Sameer",
    "Deepak", "Dilpreet", "Adnan", "Pooja", "Andrew",
    "Diya", "Jasleen", "Ayaan", "Riya", "Thomas",
    "Gaurav", "Harman", "Faizan", "Shreya", "Gabriel",
    "Ishaan", "Navneet", "Noor", "Sahil", "Peter",
    "Isha", "Simranjit", "Yusuf", "Nisha", "Anthony",
    "Jatin", "Gurkirat", "Mariam", "Rohit", "Sarah",
    "Kavya", "Rajveer", "Hamza", "Meera", "Matthew",
    "Nikhil", "Jaswinder", "Omar", "Tanya", "Christopher",
    "Vikas", "Parminder", "Aisha", "Neha", "Benjamin",
    "Varun", "Sukhdeep", "Imran", "Shweta", "Ryan",
    "Yash", "Gurleen", "Salman", "Komal", "Jennifer"
]

last_names = [
    "Sharma", "Verma", "Gupta", "Patel", "Reddy",
    "Rao", "Singh", "Kaur", "Khan", "Ahmed",
    "Ali", "Hussain", "Shaikh", "Ansari", "Syed",
    "Malik", "Qureshi", "Siddiqui", "Chopra", "Kapoor",
    "Mehta", "Shah", "Joshi", "Iyer", "Nair",
    "Menon", "Pillai", "Nayak", "Das", "Dutta",
    "Ghosh", "Banerjee", "Mukherjee", "Chatterjee", "Bose",
    "Saha", "Roy", "Sen", "Paul", "D'Souza",
    "Fernandes", "Rodrigues", "Pereira", "Gomes", "Thomas",
    "Joseph", "George", "Mathew", "Varghese", "Samuel",
    "Williams", "Andrews", "Wilson", "Peter", "Benjamin",
    "Gill", "Sandhu", "Sidhu", "Brar", "Dhillon",
    "Bhatia", "Sodhi", "Arora", "Khanna", "Malhotra",
    "Sethi", "Ahuja", "Bajaj", "Bansal", "Aggarwal",
    "Agarwal", "Mittal", "Goel", "Jain", "Mahajan",
    "Saxena", "Srivastava", "Tiwari", "Mishra", "Pandey",
    "Tripathi", "Dubey", "Yadav", "Chauhan", "Rajput",
    "Shetty", "Gowda", "Naidu", "Krishna", "Prasad",
    "Rajan", "Ramesh", "Kumar", "Rao", "Rathore",
    "Deshmukh", "Kulkarni", "Patil", "Jadhav", "Pawar"
]

course = [
    "CSE",
    "CSM",
    "CSA"
]

job_titles = [
    "Intern",
    "Trainee Software Engineer",
    "Junior Software Engineer",
    "Software Engineer",
    "Software Engineer II",
    "Senior Software Engineer",
    "Software Developer",
    "Senior Software Developer",
    "QA Engineer",
    "Senior QA Engineer",
    "Data Analyst",
    "Data Scientist",
    "DevOps Engineer",
    "Cloud Engineer",
    "Business Analyst",
    "Senior Business Analyst",
    "Technical Lead",
    "Team Lead",
    "Project Manager",
    "Product Manager",
    "Engineering Manager",
    "Senior Engineering Manager",
    "Engineering Director",
    "Vice President of Engineering",
    "Chief Technology Officer"
]


print("Select an option to generate random data and CSV file:")
print("1. Generate E-commerce Sales Data")
print("2. Generate Student Data")
print("3. Generate Employee Data")
print("4. Generate Passenger Details")

choice = int(input("Enter your choice (1, 2, 3, or 4): "))
n = int(input("Enter the number of records to generate: "))


# E-COMMERCE DATA

if choice == 1:

    product_list = np.random.choice(
        list(products.keys()),
        n
    )

    category_list = [
        products[product]
        for product in product_list
    ]

    data = {
        "Order_ID": range(1001, 1001 + n),
        "Product": product_list,
        "Category": category_list,
        "Quantity": np.random.randint(1, 5, n),
        "Price": np.random.randint(500, 70000, n),
        "City": np.random.choice(cities, n),

        # 80% Delivered, 10% Returned, 10% Cancelled
        "Status": np.random.choice(
            statuses,
            n
        )
    }

    df = pd.DataFrame(data)

    # Calculate Revenue
    df["Revenue"] = df["Quantity"] * df["Price"]

    filename = "ecommerce_sales.csv"


# STUDENT DATA

elif choice == 2:

    info = {
        "Student_ID": range(10000, 10000 + n),
        "First_Name": np.random.choice(
            First_names,
            n
        ),
        "Last_Name": np.random.choice(
            last_names,
            n
        ),
        "Gender": np.random.choice(
            ["Male", "Female"],
            n
        ),
        "Semester": np.random.randint(
            1,
            8,
            n
        ),
        "Course": np.random.choice(
            course,
            n
        ),
        "City": np.random.choice(
            cities,
            n
        )
    }

    df = pd.DataFrame(info)

    filename = "student_data.csv"


# EMPLOYEE DATA

elif choice == 3:

    TABLE = {
        "Employee_ID": range(1000, 1000 + n),
        "First_Name": np.random.choice(
            First_names,
            n
        ),
        "Last_Name": np.random.choice(
            last_names,
            n
        ),
        "Job_Title": np.random.choice(
            job_titles,
            n
        ),
        "City": np.random.choice(
            cities,
            n
        )
    }

    df = pd.DataFrame(TABLE)

    filename = "employee_data.csv"


# PASSENGER DATA

elif choice == 4:

    passenger_data = {
        "PNR": range(2000, 2000 + n),
        "First_Name": np.random.choice(
            First_names,
            n
        ),
        "Last_Name": np.random.choice(
            last_names,
            n
        ),
        "Age": np.random.randint(
            18,
            80,
            n
        ),
        "Gender": np.random.choice(
            ["Male", "Female", "Other"],
            n
        ),
        "City": np.random.choice(
            cities,
            n
        )
    }

    df = pd.DataFrame(passenger_data)

    filename = "passenger_data.csv"


# INVALID CHOICE

else:

    print("Invalid choice. Please select either 1, 2, 3, or 4.")
    exit()


# CSV DOWNLOAD

download = input(
    "Do you want to download the generated data as a CSV file? (yes/no): "
).strip().lower()


if download == "yes":

    df.to_csv(
        filename,
        index=False
    )

    print("\nGenerated Data:")
    print(df.head())

    print("\nCSV created successfully!")
    print("File:", filename)

else:

    print(
        "Thank you for using the data generator. Goodbye!"
    )