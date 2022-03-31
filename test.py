name='shushma'
age='22'
fee='2000'
file=open('f1.txt','w')
#print(file.seek(0,0))
#print(file.tell())
file.write(name+'\t'+age+'\t'+fee+'\n')
file.write('hema'+'\t'+age+'\t'+'4000'+'\n')
#file.seek(0,0)
#
fee='5000'
file.write('sowmya'+'\t'+age+'\t'+fee+'\n')
#print(file.tell())
file.close()

#storing data in list of lists
data=[]
file=open('f1.txt','r')
line=file.readline().strip()
while line:
    values=line.split('\t')
    d=[]
    for i in values:
        d.append(i)    
    data.append(d)
    line=file.readline().strip()
print(data)
file.close()


#changing the value
for row in data:
    if row[0]=='hema':
        row[2]='2999'
print(data)


#writing into file
file=open('f1.txt','w')
for row in data:
    file.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\n')
file.close()
