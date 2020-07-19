import serial
ArduinoData = serial.Serial('COM7',115200)
while(1):
        Raw_Data = ArduinoData.readline()
        All_Data = str(Raw_Data).split(':')
        Data = ['','']
        try:    
                Data[0] = All_Data[0][-1]
                Data[1] = All_Data[1][0]
        except :
                Data[0] = ''
                Data[1] = ''
        try:
                print(Data[0])
        except :
                print("ERROR")
