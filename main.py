import os
import shutil

def extension_extraction(file_name):
    index_of_dot = file_name.rfind(".")
    last_character_index = len(file_name)
    extension = file_name[index_of_dot:last_character_index] 
    return extension
    
def data_extension_identificator(extension):
# for shorthing the extension based on the type of data
    data_sorting = {
        ('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp'):"Images",
        ('.doc', '.docx', '.pdf', '.txt', '.xlsx', '.pptx'):"Document",
        ('.mp4', '.mov', '.avi', '.mkv', '.wmv'):"Video",
        ('.mp3', '.wav', '.flac', '.aac'):"Audio",
        ('.py', '.java', '.c', '.cpp', '.html', '.css', '.js'):"Code",
        ('.zip', '.rar', '.7z', '.tar', '.gz'):"Archive"
    }
    for i in data_sorting:
        if extension in i:
            return data_sorting[i]
    else:
        print("Data Extension not found")
        return "unknown"
def moves_files(source,destination):
    try:
        shutil.move(source,destination)
    except FileExistsError:
        main2(source)
def rename(file_path):
    file_name = os.path.basename(file_path)
    # to-do

    
def sorting(user_input):

    list_of_files_and_folders = os.listdir(user_input)
    # iterating through the list of file and folders present in the user_input directory
    for i in list_of_files_and_folders:

        location_of_dir_files = os.path.join(user_input,i)
        if os.path.isfile(location_of_dir_files):
            extension =extension_extraction(i)
            data_type_of_file =data_extension_identificator(extension)
             # this block of code is to move files into a designated directory if found in dict
            location_of_moving = os.path.join(user_input,data_type_of_file)
            if os.path.exists(location_of_moving):
                shutil.move(location_of_dir_files,location_of_moving)
            else:
                os.mkdir(location_of_moving)
                shutil.move(location_of_dir_files,location_of_moving)
        else:
            continue

def main():
    while True:
        print("_"*90)
        print("choose operations you want to perform :")
        print("       ___type 0 for exiting the programe:")
        print("       ___type 1 for sorting the files:")
        value_of_user = int(input("type your choise:"))
        user_input_location =input("location of for operation:")
        print("_"*90)
        match value_of_user:
            case 0:
                break
            case 1:
                if os.path.exists(user_input_location):
                    sorting(user_input_location)
                    print("operation completrd ........")
                else:
                    print("path doesn't exist:---------")
            case _:
                print ("type the correct value:")

if __name__=="__main__":
    main()
def main2(source):
    print(f"There is already a file with the same name as the folder name you specified {source}")
    print("press r for renaming this file ")
    print("press s for skipping for this file:")
    user_input = input("enter your choise:")
    if user_input=="r":
        rename(source)
    elif user_input=="s":
        print("skipped the operation.")
