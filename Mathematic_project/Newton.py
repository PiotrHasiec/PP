from os import error
import sys
import numpy
import pylab
import consts
import Functor
import IOFunctions as IOF



known_points = []
file = IOF.read_files_names()
try:    
    known_points = IOF.read_points(file[0])


except ValueError:
    print(consts.VALUE_ERROR_COMUNCAT)
    sys.exit()
except FileNotFoundError:
    print(consts.FILE_NOT_FOUND_COMUNICAT)
    sys.exit()
if(file[0]=="" or file[1] == ""):
    sys.exit()


func = Functor.functor(known_points[0], known_points[1])
interpolated_x_points = []
interpolated_y_points = []
parms = IOF.read_parms(file[0])
for i in numpy.arange(parms[0],parms[1],parms[2]):
    interpolated_x_points.append(i)
    interpolated_y_points.append( func(i))
        

pylab.plot(known_points[0],known_points[1],'o')
pylab.xlim(known_points[0][0]-known_points[0][len(known_points[0])-1]*0.5, known_points[0][len(known_points[0])-1]*1.5)
pylab.ylim(numpy.min(known_points[1])- numpy.max(known_points[1])*0.1, numpy.max(known_points[1])*1.5)

pylab.plot(interpolated_x_points,interpolated_y_points)

pylab.show()
output_file = open(file[1],'w')
if parms[3] == 1:
    output_file.write("f(x) = " + func.equation() + "\n" )
IOF.write_to_file(output_file,interpolated_x_points,interpolated_y_points)
