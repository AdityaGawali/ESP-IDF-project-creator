#!/usr/bin/env python3
import os


project_name = input("Enter ESP-IDF Project name : ")
path = os.getcwd()
project_path = path + '/' + project_name
project_path_main = path + '/' + project_name + '/' + "main"

makefile_1 = "PROJECT_NAME := " + project_name
makefile_2 = "include $(IDF_PATH)/make/project.mk"

cFile_1 = "#include <stdio.h>\n#include <string.h>\n#include \"freertos/FreeRTOS.h\"\n#include \"freertos/task.h\"\n#include \"freertos/event_groups.h\""
cFile_2 = "void app_main(void)\n{\n\tprintf(\"%s\",\"Hello!\\n\");\n}"


try:
    os.mkdir(project_path)
except OSError:
    print ("Creation of the directory %s failed" % project_path)


Makefile = open(project_path+"/Makefile","w+")
Makefile.write(makefile_1)
Makefile.write("\n")
Makefile.write(makefile_2)
Makefile.close()

try:
    os.mkdir(project_path_main)
except OSError:
    print ("Creation of the directory %s failed" % project_path_main)


cFile = open(project_path_main+"/"+project_name+".c","w+")
cFile.write(cFile_1)
cFile.write("\n\n\n")
cFile.write(cFile_2)
cFile.close()

comp_mk = open(project_path_main+"/"+"component.mk","w+")
comp_mk.close()

kconfig = open(project_path_main+"/"+"Kconfig.projbuild","w+")
kconfig.close()

print("Project created sucessfully")

