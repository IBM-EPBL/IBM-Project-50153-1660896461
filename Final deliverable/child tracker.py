import wiotp.sdk.device
import time
import random
myData = { 
    "identity": {
        "orgId": "9v4yiu",
        "typeId": "MyDevice_Mahesh",
        "deviceId": "12345"
    },
    "auth": {
        "token": "wsz!FA8hKQp9KqlmEr"
    }
}

client = wiotp.sdk.device.DeviceClient(config=myData, logHandlers=None)
client.connect()
while True:
    name= "Smartbridge" #in area location
    #latitude=17.4225176 #longitude=78.5458842
    #out area location
    latitude=17.4219272
    longitude=78.5488783
    myData={'name': name, 'lat': latitude,'lon': longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Data published to IBM IOT platform :",myData)
    time.sleep(5)
client.disconnect();
