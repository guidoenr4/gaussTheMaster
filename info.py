from datetime import datetime
import cv2,os,socket

class clock():
    def today_date(self):
        now = datetime.now()
        return now.__str__()

class camera():
    @staticmethod
    def takePicture():
        cameras = [0,1,2,3,4,5,6,7,8,9,10]
        for x in cameras:
            cap = cv2.VideoCapture(x)
            leido, frame = cap.read()
            if leido == True:
                if os.path.isdir('C:\GaussTheMaster'):
                    cv2.imwrite('C:\GaussTheMaster\snap.png', frame)
                else:
                    os.mkdir('C:\GaussTheMaster')
                    cv2.imwrite('C:\GaussTheMaster\snap.png', frame)

class ip():
    @staticmethod
    def ipAddress():
        hostName= socket.gethostname()
        return socket.gethostbyname(hostName)


class description():
    def __init__(self,fecha,ipAddress):
        self.date=fecha
        self.ip=ipAddress

    def cuerpo(self):
        return 'date: ' + self.date + '\n' + \
               'ip address: ' + self.ip + '\n'

