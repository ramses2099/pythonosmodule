import os

def main():
    # path = os.getcwd()
    # print("{}".format(path))
    # code = os.system("dir")
    # print("code: {}".format(code))
    for file in os.listdir():
        print(file)

if __name__ == "__main__":
    main()