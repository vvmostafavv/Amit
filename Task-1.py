# Task 1

email = "Amit_ml@gmail.edu"

# Check about the gmail 
if email.count('@') != 1 or email.count('.') < 1 or email.index('@') > email.rindex('.'):
    result = "Invalid email"
else:
    # Extract username
    username = email.split('@')[0]
    
    # Extract Domain
    domain = email.split('@')[1]
    domain_name = domain.rsplit('.', 1)[0]  
    
    # Check for Domain Ending
    if email.endswith('.com'):
        domain_type = "Commercial Domain"

    elif email.endswith('.edu'):
        domain_type = "Educational Domain"

    else:
        domain_type = "Other Domain"
    
    result = (f"The Username is: {username}\nThe Domain name is: {domain_name}\nThe Domain type is: {domain_type}")

print(result)


print("#"*50)
#######################################################################################################

# Task 2

# Encoded message
encoded_message = "###!!@mocleW EPGTQ!!!6789"

# Extract the core part of the message
core_part = encoded_message.split('@')[1].split('!!!')[0].strip()
print(core_part)

# Reverse the firs word
first_word = core_part.split()[0]
reversed_first_word = first_word[::-1]
print(f"The first word is: {reversed_first_word}")

# Replace shifted vowels in the second word
second_word = core_part.split()[1]
changed_second_word = second_word
# No vowels to change in "EPGTQ"

# Final decoded message
final_message = f"{reversed_first_word} {changed_second_word}"
print("Final decoded message is:", final_message)

print("#"*50)
#######################################################################################################

# Task 3

# Encoded message
encoded_message = "&&&**$gnirtS PLIO!!@1234"

# Extract the core part of the message
core_part = encoded_message.split('$')[1].split('!!')[0].strip()
print(f"Core part is: {core_part}")

# Reverse the string
first_word = core_part.split()[0]
reversed_first_word = first_word[::-1]  
print(f"Reversed first word: {reversed_first_word}")

# Replace shifted vowels in the second word
second_word = core_part.split()[1]
# Replace I => E and O => U
changed_second_word = second_word.replace('I', 'E').replace('O', 'U')
print(f"Changed second word: {changed_second_word}")

# Final decoded message
final_message = f"{reversed_first_word} {changed_second_word}"
print(f"Final decoded message is: {final_message}")

print("#"*50)
#######################################################################################################

# Task 4

# Encoded message
encoded_message = "##$$$@!yalpstcejorp EPUVT****9887"

# Extract the core part of the message
core_part = encoded_message.split('!')[1].split('****')[0].strip()
print(f"Core part is: {core_part}")

# Reverse the first word
first_word = core_part.split()[0]
reversed_first_word = first_word[::-1]  
print(f"Reversed first word: {reversed_first_word}")

# Replace shifted vowels in the second word
second_word = core_part.split()[1]
# Replace E => A and U => O
changed_second_word = second_word.replace('E', 'A').replace('U', 'O')
print(f"Changed second word: {changed_second_word}")

# Final decoded message
final_message = f"{reversed_first_word} {changed_second_word}"
print(f"Final decoded message is: {final_message}")
