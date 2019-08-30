import os
import glob
import fnmatch
 
 
'''
Generic function to delete all the files from a given directory based on matching pattern
'''
def removeFilesByMatchingPattern(dirPath, pattern):
    listOfFilesWithError = []
    for parentDir, dirnames, filenames in os.walk(dirPath):
        for filename in fnmatch.filter(filenames, pattern):
            try:
                os.remove(os.path.join(parentDir, filename))
            except:
                print("Error while deleting file : ", os.path.join(parentDir, filename))
                listOfFilesWithError.append(os.path.join(parentDir, filename))
 
    return listOfFilesWithError
 
 
def main():
 
    print('***** Remove files by pattern using glob.glob() & os.remove() *****')
 
    # Get a list of all the file paths that ends with .txt from in specified directory
    fileList = glob.glob('/home/varung/Documents/python/logs/*.log')
 
    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)
 
    print("Recursively Remove files by matching pattern or wildcard using glob.glob() & os.remove()")
 
    # get a recursive list of file paths that matches pattern including sub directories
    fileList = glob.glob('/home/varung/Documents/python/logs/**/*.txt', recursive=True)
 
    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except OSError:
            print("Error while deleting file")
 
    print("Recursively Remove files by matching pattern or wildcard using os.walk()")
 
    # Get a list of all files in directory
    for rootDir, subdirs, filenames in os.walk('/home/varung/Documents/python/logs/'):
        # Find the files that matches the given patterm
        for filename in fnmatch.filter(filenames, '*.txt'):
            try:
                os.remove(os.path.join(rootDir, filename))
            except OSError:
                print("Error while deleting file")
 
 
    print('remove files based on matching pattern and get a list of errors')
 
    listOfErrors = removeFilesByMatchingPattern('/home/varung/Documents/python/logs/', '*.txt')
 
    print('Files that can not be deleted : ')
    for filePath in listOfErrors:
        print(filePath)
 
if __name__ == '__main__':
    main()
