# Collect string / test length


def main():
    str_to_check = input("Please enter a test string: ")

    if len(str_to_check) < 6:
            print("Your string is too short.")
            print("Please enter a string with at least 6 chatacters.")

if __name__=='__main__':
       main()