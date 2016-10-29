#!/usr/bin/python
from random import randrange
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
         if(dict[irand]==num):
            totalsteps+=steps
            break
   print totalsteps*1.0/iterations




if __name__ == "__main__":
   main(sys.argv[1:])

