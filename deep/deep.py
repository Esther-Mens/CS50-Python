# Get user input
answer = input(
    "what is the answer to the Great Question of Life, the Universe and Everything")

# print yes if the user inputs 42 or (case-insensitively) forty-two or forty two
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
# otherwise output No.
else:
    print("No")
