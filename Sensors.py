import android
from time import sleep
a = android.Android()
a.startSensingTimed(1, 500)
sleep(1)
print a.readSensors().result
