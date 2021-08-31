import consts
import sys
def read_files_names():
    input_file = ""
    output_file= ""
    if(len(sys.argv)>2):
        for i in range(len(sys.argv)):
            if(sys.argv[i] == "-i"):
                input_file = sys.argv[i+1]
            elif(sys.argv[i] == "-o"):
                output_file = sys.argv[i+1]
    if(len(sys.argv)<2 or input_file == "" or output_file == "" ):
        print(consts.HELP)
    params = []
    params.append(input_file)
    params.append(output_file)
    return params

def read_points(input_file):
    x = []
    y = []
    with open(input_file) as plik:
        for linia in plik:
            if linia.strip() == "Points:":
              for linia in plik:  
                xy = linia.strip().split()
                x.append(int(xy[0]))
                y.append(int(xy[1]))
    return [x,y]

def read_parms(input_file):
    parms = [0.0,0.0,0.0,0.0]
    parms_number = 0
    with open(input_file) as plik:
        for linia in plik:
                    if linia.strip() == "Range:":
                        tmp_range =  plik.readline().strip().split(',')
                        parms[0] = tmp_range[0]
                        parms[1] =  tmp_range[1]
                        parms_number = parms_number+1
                        if parms_number ==consts.NUMBER_OF_PARMS:
                            break
                    elif linia.strip() == "Step:": 
                        tmp_step =plik.readline().strip()
                        parms[2] = tmp_step
                        parms_number = parms_number+1
                        if parms_number ==consts.NUMBER_OF_PARMS:
                            break
                    elif linia.strip() == "Equation:": 
                        tmp_step =plik.readline().strip()
                        parms[3] = tmp_step
                        parms_number = parms_number+1
                        if parms_number ==consts.NUMBER_OF_PARMS:
                            break
    return [float(parms[0]),float(parms[1]), float(parms[2]), int(parms[3])]
                    


                        
def write_to_file(output_file,x,y):
    if len(x) == len(y):
        for i in range(len(x)):
            out = '{:.3f}'.format(x[i])+";"+ '{:.3f}'.format(y[i]) + '\n'
            output_file.write(out)

