import time
import csv
import io

#Created by LUCCA CIOFFI.
#Github: https://github.com/Nodding/csv-to-vcf

print "Simple CSV to VCF"
print "Make sure input.csv is in same directory."
print "The input.csv file must be formatted correctly!"
print "It requires the columns 'Name', 'Cell', 'Work', and 'Home' to be present."
print "Lastly, each contact needs at least a name. It can be one or two words."

outfile = open("output.vcf", "w")

with open("input.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    num=0
    for row in csv_reader:
        outfile.writelines("BEGIN:VCARD" + "\n")
        outfile.writelines("VERSION:2.1" + "\n")
        name=""
        cell=""
        work=""
        home=""
        namelist=""
        firstname=""
        lastname=""
        print row
        name=row.get("Name")
        cell=row.get("Cell")
        work=row.get("Work")
        home=row.get("Home")
        print name + ", " + cell + ", " + work + ", " + home
        namelist=name.split()
        firstname=namelist[0]
        if len(namelist) > 1:
            lastname=namelist[1]
        outfile.writelines("N:"+lastname+";"+firstname+";;;" + "\n")
        outfile.writelines("FN:"+name + "\n")
        outfile.writelines("TEL;CELL:"+cell + "\n")
        outfile.writelines("TEL;WORK:"+work + "\n")
        outfile.writelines("TEL;HOME:"+home + "\n")
        outfile.writelines("END:VCARD" + "\n")
        num += 1
    print "Contacts Generated: " + str(num)
outfile.close()
   
print "END!"
end = raw_input()
