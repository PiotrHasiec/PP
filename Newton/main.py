import sys
import numpy
import pylab
class functor:
    coefficients= []
    points = []
    def __init__(self, pyramid, x):
        for i in range(len(pyramid[0])):
            self.coefficients.append( pyramid[i][0])
            self.points.append(x[i]) 

        print(pyramid)
    def __call__(self, x):

        tmp_return = 0
        tmp = 1
        for i in range(len(self.coefficients)):
            
            tmp_return =tmp_return + self.coefficients[i]*tmp
            tmp = tmp * (x-self.points[i])
        return tmp_return
    

def parms():
    if(len(sys.argv)>2):
        for i in range(len(sys.argv)):
            if(sys.argv[i] == "-i"):
                input_file = sys.argv[i+1]
            elif(sys.argv[i] == "-o"):
                output_file = sys.argv[i+1]
    if(len(sys.argv)<2 or input_file == "" or output_file == "" ):
        print("Program uruchamia się z następującymi parametrami wejściowymi: \n-i \"Nazwa pliku wejściowego\" \n-o \"Nazwa pliku wyjściowego\"")



def make_pyramid(x, y):
    pyramid = []
   
    pyramid.append(y)
    tmp_piramid = len(pyramid[0]) - 1
    
    for j in range(tmp_piramid):
        differences = []
        for i in range(len(pyramid[j]) - 1):
            #tmp2 = len(pyramid[j]) - 1
            tmp = (pyramid[j][i+1]- pyramid[j][i])/(x[i+j+1]-x[i])
            differences.append(tmp)
            
        pyramid.append(differences)
        #print(pyramid)
        #differences.clear()

    #print(pyramid)
    return pyramid

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5]
y = [0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ,0,1  ,0,-1  ]
repeats = 1
for i in range(len(x)):
    if (x.count(i)>1):
        raise RuntimeError("Podano dwie wartości funkcji dla jednego argumentu")
        repeats =0

if(not len(x) == len(y)):    
    raise RuntimeError("Podano różną liczbę zmiennych x i y")   
else:
    pyramid = make_pyramid(x,y)
    #print(pyramid)
    func = functor(pyramid,x)
    t_x = []
    t_y = []
    for i in numpy.arange(2,19,0.01):
        t_x.append(i)
        t_y.append( func(i))
        

    pylab.plot(t_x,t_y)
    #pylab.plot(x,y)
    pylab.show()
