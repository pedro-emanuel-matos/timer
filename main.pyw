from datetime import datetime
from time import sleep
        
def escrita():
        time = datetime.today()
        dia = datetime.today().strftime('%Y-%m-%d')
        arq = open("registro.txt", "a")
        time2 = str(time)
        dia2 = str(dia)
        arq.write("\n")
        arq.write(dia2)
        arq.write("\n")
        arq.write(time2)
        arq.close()


tempo = 1

while tempo < 2:
        for i in range (11):
                if i == 10:
                        escrita()
                        sleep(300)
                        
		
