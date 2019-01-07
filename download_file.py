import re
import sys
from os import system

if __name__ == "__main__":
    if len(sys.argv)<2:
        sys.exit("Please choose a url to download!")
    else:
        url = sys.argv[1]
        start,end = int(sys.argv[2]), int(sys.argv[3])
        system("wget %s"%url)
        for i in range(start, end+1):
            new_url = re.sub(r"zip$", r"z%.2d"%i, url)
            system("wget %s"%new_url)

        file_name = url.split(r"/")[-1]
        system("zip -s 0 %s --output output.zip"%file_name)
        system("unzip output.zip")
        system("rm output.zip %s.*"%file_name[:-2])