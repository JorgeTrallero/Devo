import math

numbers=[2,4,6,7,10,345,45,2,23,54,542,12,28]

def identificarnumbers(numbers):

        lista_abundantes=[]
        lista_defectivos=[]
        lista_perfectos=[]

        for m in numbers:
                plusnumber=1;
                div=int(math.sqrt(m))
                number=m
                for x in range(div, 1, -1):

                        #el 1 siempre divide a cualquier nmero por eso defino el sumatorio empezando en 1
                        if number%x==0:

                                plusnumber+=number/x;
                                if number/x != x:
                                        plusnumber+=x;
                                #print("suma de plusnumber 1:" + str(plusnumber))
                                #plusnumber+=div//x;
                                #print("el cociente:" + str(div//x))


                if number>plusnumber:
                        print("el numero" + str(number) +" es defectivo")
                        lista_defectivos.append(number)
                elif number<plusnumber :
                        print("el numero" + str(number) +" es abundante")
                        lista_abundantes.append(number)
                elif number==plusnumber:
                        print("el numero" + str(number) +" es perfecto")
                        lista_perfectos.append(number)


        print ("los siguientes n son perfectos : " + (str(lista_perfectos))[1:-1])
        print ("los siguientes n son abundantes : " + (str(lista_abundantes))[1:-1])
        print ("los siguientes n son defectivos : " + (str(lista_defectivos))[1:-1])

identificarnumbers(numbers)
