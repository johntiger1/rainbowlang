import ruamel.yaml
#IMPORTANT FOR FUTURE STUFF PIP is for Python version 2.7 !!!
import yaml
import json
import subprocess

file_name = 'languages.yml'

from ruamel.yaml.util import load_yaml_guess_indent

config, ind, bsi = load_yaml_guess_indent(open(file_name))

#language_extensions = config["main"]["extensions"]
#print (language_extensions)



#print("heel")
#"extensions"
datastring = open("languages.json").read()
langdict = json.loads(datastring)
#print(type(datastring))
#print(langdict["ABAP"]) #keys can't be integers

for dictionary in langdict:
    try:
        john = langdict[dictionary]["extensions"]
        sourcefile1 = open("yolo" + john[0], "w")
        subprocess.run(["echo", langdict[dictionary]], stdout=sourcefile1)

        #apparently with takes care of closing and such for you
        #with open("yolo" + john[0], "w") as sourcefile:
        #    john = langdict[dictionary]["extensions"]
        #    subprocess.run(["echo", langdict[dictionary]], stdout=sourcefile)

        #subprocess.run(["echo", langdict[dictionary], ">", "yolo" + john[0] ])

    except KeyError:
        print(langdict[dictionary])


    #print (langdict[dictionary]["extensions"])
    #print(john[0])

    #now we can just get the first one from each one
    #print (langdict[dictionary]["extensions"][0])
#print (datastring[0])
#for dictionary in langdict:
    #print (type(dictionary))
    #print (dictionary[0:-1])
#print(langdict)