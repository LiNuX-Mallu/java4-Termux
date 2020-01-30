import os
import sys
import time

os.system("clear")
os.system("chmod +x jd+bi && cp jd+bi /data/data/com.termux/files/usr/bin/javalogin")


print("""\033[1;32;25m


                []  [][]  []   []  [][]
                [] []  []  [] []  []  []
             [][]] []  []   [|]   []  []         
                           \n
                            by LINUX-MALLU""")
print("\n\n")

java = input("""\033[1;30;28m
         [ ! ] ENTER to install java on your termux """)

if java == '':
      print("\n \033[1;32;25m installing on process...")
      os.system("pkg install proot -y && proot bash jdk-8.#")

print()
 
print(""""\033[1;40;31m
              instruction >>>

     before using java required tool or java tools
     first run '  javalogin  ' then you can run
     > java , keytool etc... """)
     exit()
