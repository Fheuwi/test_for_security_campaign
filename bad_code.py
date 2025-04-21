import os

def insecure_function():
    user_input = input("Enter command: ")
    os.system(user_input)  # <-- 這會被 CodeQL 掃出問題

insecure_function()
secure
