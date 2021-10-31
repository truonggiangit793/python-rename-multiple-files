import os, sys, time, random
import calendar
from getch import pause

# Function to prompt YES or NO answer from user
def prompt_yes_no_query(question):
    sys.stdout.write('%s [y/n]: ' % question)
    value = ['y','n','yes','no','ye']
    prompt = input().lower()
    while prompt not in value:
        sys.stdout.write("Type error! Please response with 'y' for 'YES' or 'n' for 'NO': ")
        prompt = input().lower()
    if prompt == 'n' or prompt == 'no':
        return False
    return True

# Function to check directory
def dirCheck(dir):
    if '"' in dir:
        dir = dir.split('"')[1]
    if "'" in dir:
        dir = dir.split("'")[1]
    while not (os.path.isdir(dir)):
        if not prompt_yes_no_query("Invalid directory! Do you want to try again?"):
            print('Goodbye!')
            time.sleep(1)
            exit()
        dir = input('Choose or drag your folder here: ')
    return dir

# Function to genrate file name
def file_name_generator(index='',prefix=''):
    start, end = 10000, 90000
    time_stamp = calendar.timegm(time.gmtime())
    random_number = random.randint(start, end)
    if index:
        random_number = index
    if prefix:
        file_name = f'{prefix}_{time_stamp}{random_number}'
    else:
        file_name = f'{time_stamp}{random_number}'
    return file_name

# Function main
def main(dir,prefix):
    name_list = []
    for index, file in enumerate(os.listdir(dir)):
        file_name = file_name_generator(index+1,prefix)
        if not file_name in name_list:
            name_list.append(file_name)
        else:
            file_name = file_name_generator(index+1,prefix)
            name_list.append(file_name)
    return name_list
        
# Self execution
if __name__ == '__main__':
    prefix = ''
    folder = dirCheck(input('Choose or drag your folder here: '))
    if prompt_yes_no_query("Do you want to add prefix to your file name? E.g. YourPrefix_163342672941656.FileExtension"):
        prefix = input('Type your prefix: ')
    name_list = main(folder,prefix)
    for index, file in enumerate(os.listdir(folder)):
        extend = (file.split(".")[-1])
        file_name = f'{folder}\{name_list[index]}.{extend}'
        os.rename(f'{folder}\{file}',file_name)
    print('Done!')
        