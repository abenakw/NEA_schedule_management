import sqlite3

def print_all_users():
    conn = sqlite3.connect("rms.db")
    cur = conn.cursor()

    # Select all fields from the employee table
    cur.execute("SELECT cid, f_name, l_name, email, role FROM employee")
    rows = cur.fetchall()  # Fetch all rows
    
    if rows:
        print(f"{'CID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Role':<10}")
        print("="*70)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<25} {row[4]:<10}")
    else:
        print("No users found in the database.")

    conn.close()

# Call the function
print_all_users()