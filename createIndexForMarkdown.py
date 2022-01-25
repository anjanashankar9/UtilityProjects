import os

def createReadme(rootDir):
    for (root,dirs,files) in os.walk(rootDir, topdown=True):
        print (root)
        print (dirs)
        print (files)
        files.sort()
        readme = root + "/README.md"
        with open(readme, "w") as f:
            for dir in dirs:
                if not dir.startswith("."):
                    f.write("["+dir+"]("+dir+")\n\n")
            for file in files:
                if not file.startswith(".") and not file.startswith("README"):
                    f.write("["+file+"]("+file+")\n\n")
        f.close()


if __name__ == "__main__":
    rootDir = "/Users/anjana.shankar/Documents/scratchpad/personalGithub/courses/martin-klepmann-distributed-systems"
    createReadme(rootDir)