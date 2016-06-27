import csv
file = open("/Users/HuangYungHan/Desktop/stationss.txt", 'r', encoding = 'UTF-8')
stations = list()
for row in file.readlines():
	row = row.strip('\n')
	stations.append(row)

file.close()


for filename in stations:
	f = open('/Users/HuangYungHan/Desktop/20140101-31DIGES.csv', 'r')
	fw = open("/Users/HuangYungHan/Desktop/ubike/"+filename+".csv","w") 
	w = csv.writer(fw)   
	temp = list()
	for row in csv.reader(f):  
		temp = row
		if filename in temp[2]:
			w.writerow(row) 
	fw.close() 
	f.close()




