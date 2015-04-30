import csv
reader = csv.DictReader(open('Data/2S/2S.csv'))
for row in reader:
	print(row['<TICKER>'], row['<DTYYYYMMDD>'], row['<OPEN>'], row['<HIGH>'], row['<LOW>'], row['<CLOSE>'], row['<VOL>'])
