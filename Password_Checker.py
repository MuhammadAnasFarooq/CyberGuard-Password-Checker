import string 
password = input("Enter your Password : ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
     feedback.append("Use atleast 8 characters")

if any(char.isupper() for char in password):
     score += 1
else :
     feedback.append("Add uppercase letter")

if any(char.islower() for char in password):
     score += 1
else :
     feedback.append("Add lowercase letter")

if any(char.isdigit() for char in password):
     score += 1
else :
     feedback.append("Add numbers")

if any(char in string.punctuation for char in password):
     score += 1
else :
     feedback.append("Add symbols like @,#,&,!")
    
print("\nPassword Score:", score, "/ 5")

if score <= 2:
    print("Strength: Weak")
elif score == 3 or score == 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("Great password!")