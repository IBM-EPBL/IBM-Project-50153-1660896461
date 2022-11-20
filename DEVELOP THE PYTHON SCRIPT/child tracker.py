import json
import wiotp.sdk.device
import time

myConfig = {
    "identity":{
        "orgId": "9v4yiu",
        "typeId": "Mydevice_Mahesh",
        "deviceId": "47272"
        },
    "auth": {
        "token": "4MI0KofLVtcGBbSkqW"
    }

}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name= "TCE"

    #in area
    latitude= 17.4225176
    longitude= 78.5458842

    #out area
    #latitude= 17.4219272
    #longitude= 78.5488783

    myData={'name': name, 'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,onPublish=None)
    print("Data published to IBM IoT platform: ",myData)
    time.sleep(5)

client.disconnect()
