
names_list = open(r"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Input\Names\invited_names.txt", "r")
actual_names_list = names_list.readlines()
stripped_names_list = [names.strip("\n") for names in actual_names_list]
print(stripped_names_list)

custom_letter = r"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Input\Letters\starting_letter.txt"


for person in stripped_names_list:
    with open(custom_letter, "r") as letter:
        letter_content = letter.read()
    letter_content = letter_content.replace("[name]", person)
    with open(rf"C:\Users\ndwat\OneDrive\python\PycharmProjects\Mail Merge Project Start\Output\ReadyToSend\Letter for {person}.docx", "w") as namefile:
        namefile.write(letter_content)