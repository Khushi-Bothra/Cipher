''' This project allows user to create a database of marks obtained in 
        JEE practice tests as well as read, analyse and visualise the 
        database.
    created by Indira and Khushi, 2020-02-20
    indira.gadhvi@gmail.com
'''
import matplotlib.pyplot as graph
import numpy as np
import statistics

def create_database(filename='tmp_examdata.csv'):
    '''This will generate a database.
        input
            filename : give filename where data is to be saved
    '''
    print('data will be saved in {}'.format(filename))

    with open(filename, 'w') as f1:
        flag = True 
        f1.write('Date      , Rank, Phy, Neg.phy, Math, Neg.math, chem, '\
        		'Neg.chem, Maxmark \n')
        nrec=0
        while flag:
            nrec = nrec + 1
            strd=input('Date of examination (YYYY-MM-DD format):')
            maxmark=int(input('Maximum marks:'))
            rank=int(input('Rank:'))
            phy=int(input('enter physics marks: '))
            negphy=int(input('enter negative physics marks: '))
            math=int(input('enter maths marks: '))
            negmath=int(input('enter negative maths marks: '))
            chem=int(input('enter chemistry  marks: '))
            negchem=int(input('enter negative chemistry  marks: '))
            usropt=input('Do you want to enter more records? y/n: ')
            f1.write('{},{},{},{},{},{},{},{},{} \n'.format(
                strd,rank,phy,negphy,math,negmath,chem,negchem,maxmark))
            if (usropt[0].lower() == 'n'):
                print('{} records were input'.format(nrec))
                flag = False


def read_examdata(filename='tmp_examdata.csv'):
    '''This will read the file in a format where first line is header and 
        columns are in order Date, Rank, Phy, Neg.phy, Math, Neg.math, chem, 
        Neg.chem, Maxmark
    '''
    print('Reading {}'.format(filename))
    with open(filename, 'r') as f1:
        myrec = f1.readlines()

    strd = [m.split(",")[0] for m in myrec[1:]]
    rank = [int(m.split(",")[1]) for m in myrec[1:]]
    phy = [int(m.split(",")[2]) for m in myrec[1:]]
    negphy = [int(m.split(",")[3]) for m in myrec[1:]]
    maths = [int(m.split(",")[4]) for m in myrec[1:]]
    negmaths = [int(m.split(",")[5]) for m in myrec[1:]]
    chem = [int(m.split(",")[6]) for m in myrec[1:]]
    negchem = [int(m.split(",")[7]) for m in myrec[1:]]
    maxmark = [int(m.split(",")[8]) for m in myrec[1:]]
    
    mydata = {'date':strd, 'rank':rank, 'phy':phy, 'chem':chem, 'maths':maths,
    	'negphy':negphy, 'negchem':negchem, 'negmaths':negmaths,'maxmark':maxmark}
    
    return mydata

def exam_stat(mydata):
	pmark = [float(p + m + c)*100.0/mxm for p, m, c, mxm in zip(
		mydata['phy'], mydata['maths'], mydata['chem'], mydata['maxmark'])]
	
	mydataout = mydata.copy()
	mydataout['percent']= pmark
	print("Percentage: Min, Max, Average")
	print(min(pmark), max(pmark), statistics.mean(pmark))
	return mydataout
	
def exam_plot(plotid, mydata):
	
	if plotid == 1: 
		print('Date vs Total % Marks plot')
		fig, ax = graph.subplots()
		p1 = ax.plot(mydata['date'], mydata['percent'])
		ax.set_ylabel('Percentage')
		ax.set_title('Total % Marks')
		
		graph.show()
	if plotid == 2:
		perphy = [float(m)*3.0*100.0/mxm for m, mxm in zip(mydata['phy'], 
														   mydata['maxmark'])]
		perchem = [float(m)*3.0*100.0/mxm for m, mxm in zip(mydata['chem'], 
														   mydata['maxmark'])]
		permaths = [float(m)*3.0*100.0/mxm for m, mxm in zip(mydata['maths'], 
														   mydata['maxmark'])]
		fig, ax = graph.subplots()
		p1 = ax.plot(mydata['date'],perphy,'r-',label='Physics')
		p2 = ax.plot(mydata['date'],perchem,'b-',label='Chemistry')
		p3 = ax.plot(mydata['date'],permaths,'g-',label='Maths')
		ax.legend()
		graph.show()
	if plotid == 3: 
		negpmark = [float(-x1-x2-x3)*100.0/float(mxm) for x1,x2,x3,mxm in 
			zip(mydata['negphy'], mydata['negchem'], mydata['negmaths'],
				mydata['maxmark'])]
		ind = np.arange(len(mydata['date']))
		width = 0.35
		fig, ax = graph.subplots()
		p1 = ax.bar(ind-width/2.0, mydata['percent'], width, label = 'Marks')
		p2 = ax.bar(ind+width/2.0, negpmark, width, label='Negative Marks')
		ax.set_ylabel('Percentage Marks')
		ax.set_xticks(ind)
		ax.set_xticklabels(mydata['date'])
		ax.legend()
		graph.show()
if __name__ == '__main__': 
	usropt = input("Do you want to create new database? (y/n): ")
	if (usropt[0].lower() == 'y'):
		filename = input('Give filename to save data e.g. exam_data.csv: ')
		create_database(filename)
	else:
		filename = input('Give filename of existing database' \
						  ' e.g. exam_data.csv: ')
	d = read_examdata(filename)
	d1= exam_stat(d)
	flag = True
	while flag:
		print("Type your graph choice number from of the following")
		print ("1: date vs total marks\n" \
			 "2: date vs subject marks\n" \
			 "3: bar plot date vs correct,incorrect answers")
		plotid = int(input('Enter choice: '))
		exam_plot(plotid, d1)
		usropt = input("Do you want to display another plot? (y/n): ")
		if (usropt[0].lower() == 'n'):
			flag = False
		
