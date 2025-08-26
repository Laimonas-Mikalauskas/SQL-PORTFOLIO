inp_username = input("Įveskite username: ")
inp_password = input("Įveskite slaptažodį: ")

query = f"SELECT * FROM user WHERE user.username='{inp_username}' AND user.password='{inp_password}';"

with conn:
    c.execute(query)
    res = c.fetchall()
    if res:
        print("Your profile data is:")
        print(res)
    else:
        print(f"User {inp_username} does not exist or wrong password")
