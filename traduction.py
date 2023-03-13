import opencc
import os

# From simplified chinese to traditional chinese
converter = opencc.OpenCC('s2t.json')

def convert(dirPath, dirName, converter=converter):
    # Creating a new directory for the translated files
    parentDir = os.path.dirname(dirPath)
    new_dir = os.path.join(parentDir, "Translated_" + dirName)
    os.mkdir(new_dir)
    print("Translated " + new_dir +" created")
    # For each file listed
    for filename in os.listdir(dirPath):
        f = os.path.join(dirPath, filename)
        if os.path.isfile(f):
            # Opening and reading the file line by line
            file = open(f, "r")
            file_translated = open(new_dir + "/" + filename, "a")

        for line in file.readlines():
            # Translate every line 
            line_translated = converter.convert(line)
            # Write the translated line in the new file
            file_translated.write(line_translated)

        # Closing both files
        file.close()
        file_translated.close()
