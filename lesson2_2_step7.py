import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
print(file_path)
time.sleep(2)
print(os.path.abspath(__file__))
time.sleep(2)
print(os.path.abspath(os.path.dirname(__file__)))
time.sleep(2)