response = input("Greeting: ")

new_response = response.lower().strip() # to accept case sensitivity
#if the greeting has hello,print $0
if 'hello' in new_response:
    print("$0")

#if the response starts with 'h' print $20
elif 'h' == new_response[0]:
    print("$20")
#otherwise
else:
    print("$100")
