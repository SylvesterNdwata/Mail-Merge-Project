#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names_list = open(r"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Input\Names\invited_names.txt", "r")
actual_names_list = names_list.readlines()
stripped_names_list = [names.strip("\n") for names in actual_names_list]
print(stripped_names_list)

custom_letter = r"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Input\Letters\starting_letter.txt"


for person in stripped_names_list:
    with open(custom_letter, "r") as letter:
        letter_content = letter.read()
    letter_content = letter_content.replace("[name]", person)
    #open(rf"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Output\ReadyToSend\Letter for {person}.txt")
    with open(rf"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Output\ReadyToSend\Letter for {person}.txt", "w") as namefile:
        namefile.write(letter_content)