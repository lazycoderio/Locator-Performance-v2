import influxdb_client
from influxdb_client import InfluxDBClient
from config import Config 
from influxdb_client import Point, WritePrecision
from datetime import datetime

c = Config()
print(c)
## You can generate a Token from the "Tokens Tab" in the UI
client = InfluxDBClient(url=c.env_vars["INFLUXDB"]["URL"], token=c.env_vars["INFLUXDB"]["TOKEN"])

### option 1
write_api = client.write_api()

data = "mem,host=host1 used_percent=23.43234543 1556896326"
attempt_1 = write_api.write("bucketID", c.env_vars["INFLUXDB"]["BUCKET"], data)
###

### option 2
point = Point("mem")\
  .tag("host", "host1")\
  .field("used_percent", 23.43234543)

attempt_2 = write_api.write("bucketID", c.env_vars["INFLUXDB"]["BUCKET"], point)
###

print(write_api.)
print(attempt_1)
print(attempt_2)