from sseclient import SSEClient
import json, requests, atexit, os, calls

#if __name__ == "__main__":
messages = SSEClient('{0}?access_token={1}'
                       .format(os.environ['PARTICLE-URL'],os.environ['TOKEN']))

for msg in messages:
  #event = str(msg.event).encode('ascii', 'ignore').decode('ascii')
  #data = str(msg.data).encode('ascii', 'ignore').decode('ascii')
  #print(event)
  #print(data)
  # print(msg.event)
  if msg.event == os.environ['EVENT']:
    # print(msg.data)
    dataJson = json.loads(msg.data)
    
    if (dataJson["data"] == "P1G"):
      calls.sendP1G()
    elif (dataJson["data"] == "P1R"):
      calls.sendP1R()
    elif (dataJson["data"] == "P2G"):
      calls.sendP2G()
    elif (dataJson["data"] == "P2R"):
      calls.sendP2R()
    elif (dataJson["data"] == "P3G"):
      calls.sendP3G()
    elif (dataJson["data"] == "P3R"):
      calls.sendP3R()
    elif (dataJson["data"] == "P4G"):
      calls.sendP4G()
    elif (dataJson["data"] == "P4R"):
      calls.sendP4R()
    else:
      print("Could not find right data...")
    # print(dataJson["data"])
