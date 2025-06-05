print("Hello User. I'm AI Chatbot. What's your name?")
name=input()
print(f"Nice to meet you,{name}!")
print("How are you feeling today?(Good or Bad)")
mood=input().lower()
if mood=="good":
    print("Glad to hear that!")
elif mood=="bad":
    print("Sorry to hear that, hope things get better soon.")
else:
    print("I see... Sometimes it's hard to put feelings into words.")
print(f"Well it was nice to meet you, {name}. Goodbye.")