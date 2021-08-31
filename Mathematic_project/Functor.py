class functor:
    coefficients= []
    points = []
    def __init__(self, x,y):
        pyramid = self.__make_pyramid(x,y)
        for i in range(len(pyramid[0])):
            self.coefficients.append( pyramid[i][0])
            self.points.append(x[i]) 

    def __call__(self, x):

        tmp_return = 0
        tmp = 1
        for i in range(len(self.coefficients)):
            
            tmp_return =tmp_return + self.coefficients[i]*tmp
            tmp = tmp * (x-self.points[i])
        return tmp_return
    
    def __make_pyramid(self,x, y):
        pyramid = []
    
        pyramid.append(y)
        tmp_piramid = len(pyramid[0]) - 1
        
        for j in range(tmp_piramid):
            differences = []
            for i in range(len(pyramid[j]) - 1):

                tmp = (pyramid[j][i+1]- pyramid[j][i])/(x[i+j+1]-x[i])
                differences.append(tmp)
                
            pyramid.append(differences)
        return pyramid

    def equation(self):
        str_return = str(self.coefficients[0])
        tmp_return = ""#"(x-"+str(self.points[0]) +")"
        for i in range(len(self.coefficients)-1):
                    
         tmp_return =tmp_return + "(x-"+str(self.points[i]) +")"
         str_return = str_return + " + " + '{:.5f}'.format(self.coefficients[i+1]) + tmp_return

        return str_return
        