import pandas as pd
import numpy as np
import streamlit as st


# -----------------------------
# STREAMLIT APP
# -----------------------------

st.set_page_config(
    page_title="Data Generator",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Data Generator")


# -----------------------------
# USER INPUT
# -----------------------------

n = st.number_input(
    "Enter the number of records to generate:",
    min_value=1,
    max_value=10000,
    value=100,
    step=10
)


selection = st.selectbox(
    "Select the type of data you want:",
    [
        "E-commerce Sales Data",
        "Student Data",
        "Employee Data",
        "Passenger Details",
        "Inventory Data"
    ]
)


# -----------------------------
# DATA
# -----------------------------

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


statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Cancelled",
    "Returned"
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
suppliers =  [
    "PrimeSource Suppliers",
    "GlobalLink Traders",
    "ReliableGoods Pvt Ltd",
    "Universal Supply Co.",
    "NextGen Distributors",
    "EverTrade Suppliers",
    "QualitySource Traders",
    "DirectLine Distributors",
    "ProSupply Solutions",
    "CoreTrade Pvt Ltd"
]

# -----------------------------
# E-COMMERCE DATA
# -----------------------------

product_list = np.random.choice(
    list(products.keys()),
    n
)

category_list = [
    products[product]
    for product in product_list
]

ecommerce_data = {
    "Order_ID": range(1001, 1001 + n),
    "Product": product_list,
    "Category": category_list,
    "Quantity": np.random.randint(1, 5, n),
    "Price": np.random.randint(500, 70000, n),
    "City": np.random.choice(cities, n),
    "Status": np.random.choice(statuses, n)
}

ecommerce_df = pd.DataFrame(ecommerce_data)

ecommerce_df["Revenue"] = (
    ecommerce_df["Quantity"] *
    ecommerce_df["Price"]
)


# -----------------------------
# STUDENT DATA
# -----------------------------

student_data = {
    "Student_ID": range(10000, 10000 + n),
    "First_Name": np.random.choice(First_names, n),
    "Last_Name": np.random.choice(last_names, n),
    "Semester": np.random.randint(1, 8, n),
    "Course": np.random.choice(course, n),
    "City": np.random.choice(cities, n)
}

student_df = pd.DataFrame(student_data)


# -----------------------------
# EMPLOYEE DATA
# -----------------------------

employee_data = {
    "Employee_ID": range(1000, 1000 + n),
    "First_Name": np.random.choice(First_names, n),
    "Last_Name": np.random.choice(last_names, n),
    "Job_Title": np.random.choice(job_titles, n),
    "City": np.random.choice(cities, n)
}

employee_df = pd.DataFrame(employee_data)

# -----------------------------
# PASSENGER DATA
# -----------------------------

passenger_data = {
    "PNR": range(2000, 2000 + n),
    "First_Name": np.random.choice(First_names, n),
    "Last_Name": np.random.choice(last_names, n),
    "Age": np.random.randint(18, 80, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "City": np.random.choice(cities, n)
}

passenger_df = pd.DataFrame(passenger_data)
#-----------------------------
# INVENTORY DATA
#-----------------------------


inventory_data = {
    "Product_Name": product_list,
    "Category": category_list,
    "Stock_Quantity": np.random.randint(10, 1000, n),
    "New_stock Status": np.random.choice(["Ordered", "InTransit", "Received"], n),
    
    "Supplier": np.random.choice(suppliers, n)
}

inventory_df = pd.DataFrame(inventory_data)


# -----------------------------
# DISPLAY SELECTED DATA
# -----------------------------

if selection == "E-commerce Sales Data":

    st.subheader("E-commerce Sales Data")

    st.dataframe(
        ecommerce_df,
        use_container_width=True
    )

    csv = ecommerce_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="ecommerce_sales.csv",
        mime="text/csv"
    )


elif selection == "Student Data":

    st.subheader("Student Data")

    st.dataframe(
        student_df,
        use_container_width=True
    )

    csv = student_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="student_data.csv",
        mime="text/csv"
    )


elif selection == "Employee Data":

    st.subheader("Employee Data")

    st.dataframe(
        employee_df,
        use_container_width=True
    )

    csv = employee_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="employee_data.csv",
        mime="text/csv"
    )

elif selection == "Passenger Details":

    st.subheader("Passenger Details")

    st.dataframe(
        passenger_df,
        use_container_width=True
    )

    csv = passenger_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="passenger_data.csv",
        mime="text/csv"
    )
elif selection == "Inventory Data":

   
    st.dataframe(
        inventory_df,
        use_container_width=True
    )

    csv = inventory_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="inventory_data.csv",
        mime="text/csv"
    )