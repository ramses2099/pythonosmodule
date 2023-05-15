import os
import subprocess


def main():
    # path = os.getcwd()
    # print("{}".format(path))
    # code = os.system("dir")
    # print("code: {}".format(code))
    # for file in os.listdir():
    #     print(file)

    # filename= 'README.md'

    # if os.path.exists(filename):
    #     print("File Exists")
    #     if os.path.isdir(filename):
    #         print("It's a directory")
    #     else:
    #         print("It's a file")
    # else:
    #     print("File not found")

    # for _, _, files in os.walk("data"):
    #     for file in files:
    #         print(file)
    command = "dir"
    sp = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    rt = sp.wait()
    out, err = sp.communicate()
    print(out)


if __name__ == "__main__":
    main()
