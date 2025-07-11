# Exercise: Loop through a list of users and print a message for each one.
# If the user's name starts with "A", print that they are allowed to run the test.
# Otherwise, print that the user is skipped.
users = ["Alice", "Bob", "Charlie"]

for user in users:
    if user.startswith("A"):
        print(f"{user} is allowed to run the test.")
    else:
        print(f"{user} is skipped.")


# Exercise: Given a list of URLs, print all of them with numbering.
# Then, print only the URLs that contain the word "login", also with numbering.
urls = ["https://www.w3schools.com/python/login", "https://playwright.dev/", "https://github.com/login", "https://chatgpt.com/", "https://www.youtube.com/"]
num = 1

print("All urls:")
for url in urls:
    print(f"{num}.{url}")
    num += 1

num = 1
print("Urls contain \"login\" word:")
for url in urls:
    if "login" in url:
        print(f"{num}.{url}")
        num += 1


# Exercise: Given a dictionary of users and their roles, 
# loop through the dictionary and print only the users who have the role "admin".
users = {
    "Alice": "admin",
    "Bob": "user",
    "Charlie": "guest"
}

for k,v in users.items():
    if v == "admin":
        print(k,v)


# Exercise: Given a list of test durations, use enumerate to iterate through them with test numbers.
# For each test, print whether it passed (≤ 2.0s) or took too long (> 2.0s), including the duration.
durations = [1.2, 0.8, 3.5, 0.6, 5.0]

for i,d in enumerate(durations, start=1):
    if d > 2.0:
        print(f"Test {i} took too long: {d}s")
    else:
        print(f"Test {i} passed in: {d}s")

# Exercise: Given a list of usernames, loop through the list and run a test only for users whose names start with "a" or "b" (case-insensitive).
# Print a message indicating whether each user is tested or skipped.
user_names = ["lio", "borel", "Azel", "darko43", "piero", "tonia", "Bird3"]

for user in user_names:
    
    if user.lower().startswith("a") or user.lower().startswith("b"):
        print(f"Running test for {user}")
    else:
        print(f"Skipping {user}")


import time
users = {
    "alice": "admin",
    "bob": "user",
    "carla": "guest",
    "dimitris": "user",
    "anna": "admin"
}

admin_users = []
guest_users = []
just_users = []
run_count = 0

for user,role in users.items():
    role = role.casefold()

    if role == "admin":
        admin_users.append(user)
    elif role == "guest":
        guest_users.append(user)
    else:
        just_users.append(user)

    if user.lower().startswith(("a","b")):
        print(f"Running test for user: {user}")
        time.sleep(1.5)
        run_count += 1
    else:
        print(f"Skipping user: {user}")
        time.sleep(1.5)
        
print(f"\nAll admin users: {admin_users}")

role_counts = {
    "admin": len(admin_users),
    "guest": len(guest_users),
    "user": len(just_users)
}
print("Role counts:", role_counts)
print(f"Total tests run: {run_count}")

available_tests = {
    "login": True,
    "register": True,
    "checkout": False,
    "logout": True
}
print(f"Choose 1 test: {list(available_tests.keys())} or 'exit'")
user_input = input(": ")

while user_input in available_tests:
    for x,y in available_tests.items():
        if x == True:
            print("yes")
        else:
            print("no")
    break
    print(f"Choose 1 test: {list(available_tests.keys())} or 'exit'")

else:
    print("Test not found")





