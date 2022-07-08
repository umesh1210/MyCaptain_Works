import csv
def write_into_csv():
    with open('student_info.csv','w+',) as csv_file:
        writter = csv.writter(csv_file)

        writter.writterow(info_list)
if __name__== '__main__':
    condition = True

    while(condition):
        student_info=input("Enter student info in the following format :")
        print("Entered student info"+student_info)

        #split
        student_info_list=student_info.split(' ')
        print("entered split up information is:"+str(student_info_list))


        print("Entered split up information is -\nName: {}\nAge: {}\nContact_number")
        write_into_csv(student_info_list)

        condition_check=input("Enter (yes/no) if you want to enter information for another students:")
        if condition_check=="yes":
            condition=True
        elif condition_check=="no":
            condition=False