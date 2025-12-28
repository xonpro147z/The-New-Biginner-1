def file_exists_decorator(func): 
    def wrapper(file_name, *args, **kwargs): 
     import os 
     if not os.path.exists(file_name): 
      raise FileNotFoundError(f"File '{file_name}' does not exist.") 
     return func(file_name, *args, **kwargs) 
    return wrapper 
@file_exists_decorator 
def read_file_content(file_name): 
    # read_file_content = file_exists_decorator(read_file_content)
    with open(file_name, 'r', encoding = 'utf-8') as file: 
     return file.read() 
# Usage of the decorated function 
try:
 content = read_file_content('example.txt')
 print(content)  
except FileNotFoundError as e: 
    print(e)