#!/usr/bin/python3
import subprocess
import time
 

i=0
fout=open('output.txt','w')
while True:
    try:
        i=i+1
        print('i',i)
        dus=[]
        for adir in ["/opt/alfresco414Pgsolr/alf_data/contentstore/","/opt/alfresco414Pgsolr/solr/alexindexes/"]:
            
            out=subprocess.check_output(["du", "-s",adir])
            
            print("out",out)
            splitted=out.split(b'\t')
            du=splitted[0]
            print('du',du)
            dus.append(int(du))
        print(i,dus[0],dus[1],file=fout,sep=',')
        time.sleep(0.1)
    except:
        pass
fout.close()
