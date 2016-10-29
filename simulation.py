#!/usr/bin/python
from random import randrange
import numpy as np
import matplotlib.pyplot as plt
import sys, getopt

def main(argv):
   iterations= ''
   num = ''
   elements=''
   try:
      opts, args = getopt.getopt(argv,"hi:n:e:",["iter=","num=","elements="])
   except getopt.GetoptError:
      print 'correct usage: simulation.py -i <iterations> -n <num> -e <elements>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'simulation.py -i <iterations> -n <num> -e <elements>'
         sys.exit()
      elif opt in ("-i", "--iter"):
         iterations = int(arg)
      elif opt in ("-n", "--num"):
         num = int(arg)
      elif opt in ("-e", "--elements"):
         elements=int(arg)

   
   listOfMean=[]
   label=[]
   for val in range(1,num+1):
      totalsteps=0
      for iter in range(iterations):
         dict={}
         steps=0
         while True:
            irand = randrange(0,elements)
            if irand in dict:
               dict[irand]+=1
            else:
               dict[irand]=1
            steps+=1
            if(dict[irand]==val):
               totalsteps+=steps
               break
      listOfMean.append(totalsteps*1.0/iterations)
      label.append(val)

   print listOfMean
   index = np.arange(num)
   plt.bar(index,listOfMean, align='center', alpha=0.5)
   plt.xticks(index,label)
   plt.ylabel('Expected Value')
   plt.xlabel('Value of n')
   plt.title('Random Simulation')
   plt.show()




if __name__ == "__main__":
   main(sys.argv[1:])

