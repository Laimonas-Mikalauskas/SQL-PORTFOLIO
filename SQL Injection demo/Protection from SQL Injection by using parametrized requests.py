from this import c

from SQLite.main import conn

inp_username = input("Enter the username:")
inp_password = input("Enter the password:")

with conn:
    c.execute("SELECT * FROM user WHERE user.username=? AND user.password=?;", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print("Your profile data is:")
        print(res)
    else:
        print(f"User {inp_username} doesn't exist or incorrect password")