import os
path = "/Users/plakhera/Documents/devops"

def fullpath(path=path):
    full_path = []
    for dirfullpath, dirname, filename in os.walk(path):
        for file in filename:
            fullpath = os.path.join(dirfullpath,file)
            full_path.append(fullpath)
        return full_path

def filepath(path=path):
    file_path = []
    for dirfullpath, dirname, filename in os.walk(path):
        for file in filename:
            file_path.append(file)
        return file_path

def dirpath(path=path):
    dir_path = []
    for dirfullpath, dirname, filename in os.walk(path):
        for dir in dirname:
            dir_path.append(dir)
        return dir_path



if __name__ == "__main__":
    print("Complete path of the directory")
    for comppath in fullpath():
        print(comppath)

    print("All files path: ")
    for filepath in filepath():
        print(filepath)

    print("All directory path: ")
    for dirpath in dirpath():
        print(dirpath)
