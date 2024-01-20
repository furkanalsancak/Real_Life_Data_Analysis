import csv


print("------------------------------------------------------------------")

with  open('Plane_Price.csv', 'r') as csv_file: # opening file
    csv_reader = csv.reader(csv_file) #reading file

    next(csv_reader)

    with open('new_names.csv', 'w') as new_file: #creating new file
        csv_writer = csv.writer(new_file, delimiter='\t') #writing to that new file

        for line in csv_reader: # writing each line of the plane price file into the new file
            csv_writer.writerow(line)
            #print(line[2])

print("------------------------------------------------------------------")

with  open('Plane_Price.csv', 'r') as csv_file: # opening file
    csv_reader = csv.DictReader(csv_file) #reading file

    for line in csv_reader:
        print(line['Model Name'])

print("------------------------------------------------------------------")



'''
with  open('Plane_Price.csv', 'r') as csv_file: # opening file
    csv_reader = csv.DictReader(csv_file) #reading file

    with open('new_names.csv', 'w') as new_file: #creating new file
        field_names = ['Model Name','Max speed Knots','Rcmnd cruise Knots']
        
        csv_writer = csv.DictWriter(new_file,fieldnames=field_names,delimiter='\t') #writing to that new file

        csv_writer.writeheader()

        for line in csv_reader: # writing each line of the plane price file into the new file
            del line['Model Name']
            csv_writer.writerow(line)
            #print(line[2])
'''