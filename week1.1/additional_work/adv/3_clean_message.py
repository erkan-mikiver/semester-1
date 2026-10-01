"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version


cleaned_message = raw_message.title()

x = cleaned_message.replace(' ', '')
x = list(x)

cleaned_list = []
upper = 0
for i in x:
    if i.isupper():
        if upper == 0:
            upper += 1
            cleaned_list.append(i)
        else:
            cleaned_list.append(' ')
            cleaned_list.append(i.lower())
    else:
        cleaned_list.append(i)

cleaned_message = ''.join(cleaned_list)


print(f'Original Message: {raw_message}')
print()
print(f'Cleaned Message: {cleaned_message}')

