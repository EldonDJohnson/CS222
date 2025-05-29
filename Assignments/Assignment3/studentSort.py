def main():
    try: 
        studentList = {}
        fileInput = open("C:/Users/Eldon/Downloads/students.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
        
        for s in students:
            parts = s.split(',')
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4].rstrip('\n')]
        
            options = ""
            
            while options != 3:
                print("1) Search by Last Name" + "\n"
                      "2) Search by Major" + "\n"
                      "3) Quit")
                options = int(input("Choose an Option: "))
                
                if options == 1:
                   name = input("Enter the last name you want to search for: ")
                   
                   if parts[1] == name: 
                       print(s)
                       
                   else: 
                       print("Student Not Found")
                   
                elif options == 2:
                   major = input("Enter the major you want to search for: ")
                   
                   if parts[3] == major: 
                       print(s)
                       
                   else: 
                       print("Student Not Found")
                   
                elif options == 3:
                    break
                
                else:
                   print("Invalid Response")
            
    except FileNotFoundError:
        print("File Not Found")
main()