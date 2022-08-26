import random
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from deepface import DeepFace
import webbrowser

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
list = ["Music", "Video", "Live Joke"]
music = ["https://www.youtube.com/watch?v=lAXsWFkKsK4&list=RDlAXsWFkKsK4&start_radio=1", "https://www.youtube.com/watch?v=MA0aCUxItYA"]
video = ["https://www.youtube.com/shorts/LQ8Gixq2rgA", "https://www.youtube.com/watch?v=LUpb2boy5XA"]
liveJoke = ["https://www.youtube.com/watch?v=RXrTuPxO0UQ", "https://www.youtube.com/watch?v=sKm5Mvaf8eo"]

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 523)
        self.name = ""
        self.mood = ""
        self.LaunchVideo = QtWidgets.QPushButton(Form, clicked = lambda : self.run())
        self.LaunchVideo.setGeometry(QtCore.QRect(0, 480, 101, 41))
        self.LaunchVideo.setObjectName("LaunchVideo")
        self.AddImage = QtWidgets.QPushButton(Form, clicked = lambda : self.addImage())
        self.AddImage.setGeometry(QtCore.QRect(100, 480, 101, 41))
        self.AddImage.setObjectName("AddImage")
        self.ProcessImage = QtWidgets.QPushButton(Form, clicked = lambda : self.processImage())
        self.ProcessImage.setGeometry(QtCore.QRect(200, 480, 101, 41))
        self.ProcessImage.setObjectName("ProcessImage")
        self.No = QtWidgets.QPushButton(Form, clicked = lambda: self.isNo())
        self.No.setGeometry(QtCore.QRect(100, 400, 101, 41))
        self.No.setObjectName("No")
        self.Yes = QtWidgets.QPushButton(Form, clicked = lambda: self.isYes())
        self.Yes.setGeometry(QtCore.QRect(0, 400, 101, 41))
        self.Yes.setObjectName("Yes")
        self.Submit = QtWidgets.QPushButton(Form, clicked =  lambda : self.setEnvironment(self.Submit))
        self.Submit.setGeometry(QtCore.QRect(200, 400, 101, 41))
        self.Submit.setObjectName("Submit")
        self.Display = QtWidgets.QLabel(Form)
        self.Display.setGeometry(QtCore.QRect(10, 10, 381, 361))
        self.Display.setObjectName("Display")
        self.Display.setScaledContents(True)
        self.Suggest = QtWidgets.QPushButton(Form, clicked = lambda : self.setEnvironment(self.Suggest))
        self.Suggest.setGeometry(QtCore.QRect(300, 400, 101, 41))
        self.Suggest.setObjectName("Suggest")
        self.LiveJoke = QtWidgets.QPushButton(Form, clicked = lambda : self.setEnvironment(self.LiveJoke))
        self.LiveJoke.setGeometry(QtCore.QRect(300, 480, 101, 41))
        self.LiveJoke.setObjectName("LiveJoke")
        self.PlayAVideo = QtWidgets.QPushButton(Form, clicked = lambda : self.setEnvironment(self.PlayAVideo))
        self.PlayAVideo.setGeometry(QtCore.QRect(100, 440, 101, 41))
        self.PlayAVideo.setObjectName("PlayAVideo")
        self.PlayAMusic = QtWidgets.QPushButton(Form, clicked =  lambda : self.setEnvironment(self.PlayAMusic))
        self.PlayAMusic.setGeometry(QtCore.QRect(0, 440, 101, 41))
        self.PlayAMusic.setObjectName("PlayAMusic")
        self.Start = QtWidgets.QPushButton(Form, clicked = lambda : self.setEnvironment(self.Start))
        self.Start.setGeometry(QtCore.QRect(200, 440, 201, 41))
        self.Start.setObjectName("Start")
        self.Entry = QtWidgets.QLineEdit(Form)
        self.Entry.setGeometry(QtCore.QRect(0, 380, 401, 20))
        self.Entry.setObjectName("Entry")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def setEnvironment(self, button):
        if button == self.PlayAMusic:
            if self.name == "" and self.mood == "":
                #directory = "C:/Users/nsyfi/OneDrive/Desktop/" + str(random.randint(1, 10))
                directory = music[random.randint(0, 1)]
                self.Display.setText("Below is our suggestion of music for your mood")
                self.Entry.setText(directory)
                webbrowser.open(directory)
            else:
                directory = music[random.randint(0, 1)]
                self.Display.setText(f'Hey {self.name} Below is our suggestion of music for your {self.mood} mood')
                self.Entry.setText(directory)
                webbrowser.open(directory)
        elif button == self.PlayAVideo:
            if self.name == "" and self.mood == "":
                directory = video[random.randint(0, 1)]
                self.Display.setText("Below is our suggestion of video for your mood")
                self.Entry.setText(directory)
                webbrowser.open(directory)
            else:
                directory = video[random.randint(0, 1)]
                self.Display.setText(f'Hey {self.name} Below is our suggestion of Music for your {self.mood} mood')
                self.Entry.setText(directory)
                webbrowser.open(directory)
        elif button == self.Submit:
            if self.Entry.text() == "Yes":
                if self.option == "Music":
                    self.Display.setText("Below is our suggestion of Music for your mood")
                    directory = music[random.randint(0, 1)]
                    self.Entry.setText(directory)
                    webbrowser.open(directory)
                elif self.option == "Video":
                    self.Display.setText("Below is our suggestion of Video for your mood")
                    directory = video[random.randint(0, 1)]
                    self.Entry.setText(directory)
                    webbrowser.open(directory)
                else:
                    self.Display.setText("Below is our suggestion of Live Joke for your mood")
                    directory = liveJoke[random.randint(0, 1)]
                    self.Entry.setText(directory)
                    webbrowser.open(directory)
            elif self.Entry.text() == "No":
                self.Display.setText("Alright, a good time sleep may help you.")
            else:
                self.name = self.Entry.text()
                self.Display.setText(f'Hello {self.name}')
        elif button == self.Start:
            self.Display.setText("What should I call you?")
            self.clear()
        elif button == self.LiveJoke:
            if self.name == "" and self.mood == "":
                directory = liveJoke[random.randint(0, 1)]
                self.Display.setText("Below is our suggestion of live joke for your mood")
                self.Entry.setText(directory)
                webbrowser.open(directory)
            else:
                directory = liveJoke[random.randint(0, 1)]
                self.Display.setText(f'Hey {self.name} Below is our suggestion of Live Joke for your {self.mood} mood')
                self.Entry.setText(directory)
                webbrowser.open(directory)
        elif button == self.Suggest:
            self.option = list[random.randint(0, 2)]
            self.Display.setText(f'Can i suggest you a {self.option}')
        else:
            print("That's a wrong answer!!")

    def clear(self):
        self.Entry.setText("")

    def isYes(self):
        self.Entry.setText("Yes")

    def isNo(self):
        self.Entry.setText("No")

    def run(self):
        #face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(1)
        if not cap.isOpened():
            cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("webCam not found!")
        while True:
            ret, img = cap.read()
            # img = cv2.imread('R.png')
            guess = DeepFace.analyze(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, guess['dominant_emotion'], (0, 50), font, 3, (0, 0, 255), 1, cv2.LINE_4);
            cv2.imshow('Video', img)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        cap.release()
        cv2.destroyAllWindows()

    def addImage(self):
        fname = QFileDialog.getOpenFileName(parent=None, caption='Open File', directory='C:\\Users\\nsyfi\\OneDrive', filter='All Files (*)')
        self.file=fname[0]
        self.px = QPixmap(fname[0])
        self.Display.setPixmap(self.px)

    def processImage(self):
        #self.Display.setText(self.file)
        img1 = cv2.imread(self.file)
        q=DeepFace.analyze(img1)
        #print(q['dominant_emotion'])
        #print(1)
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        we=cv2.putText(img1, q['dominant_emotion'], (0, 50), font, 3, (0, 0, 255), 1, cv2.LINE_4);
        #plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
        self.mood = q['dominant_emotion']
        self.Display.setText(f'{self.name}, your mood is {self.mood}, What do you want me to do?')


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "App"))
        self.LaunchVideo.setText(_translate("Form", "Launch Video"))
        self.AddImage.setText(_translate("Form", "Add Image"))
        self.ProcessImage.setText(_translate("Form", "Process Image"))
        self.No.setText(_translate("Form", "No"))
        self.Yes.setText(_translate("Form", "Yes"))
        self.Submit.setText(_translate("Form", "Submit"))
        self.Display.setText(_translate("Form", "Display"))
        self.Suggest.setText(_translate("Form", "Suggest"))
        self.LiveJoke.setText(_translate("Form", "Live Joke"))
        self.PlayAVideo.setText(_translate("Form", "Play A Video"))
        self.PlayAMusic.setText(_translate("Form", "Play A Music"))
        self.Start.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
