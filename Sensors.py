import android
import time
droid = android.Android()
droid.startSensingTimed(1, 500)
time.sleep(1)
print droid.readSensors().result
