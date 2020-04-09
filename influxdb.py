import time
import random

import influxdb_client
from influxdb_client import InfluxDBClient
from config import Config 
from influxdb_client import Point, WritePrecision

c = Config()
## You can generate a Token from the "Tokens Tab" in the UI
client = InfluxDBClient(url=c.env_vars["INFLUXDB"]["URL"], token=c.env_vars["INFLUXDB"]["TOKEN"])

### option 1
write_api = client.write_api()

data = "mem,host=host1 used_percent=23.43234543 1556896326"
write_api.write("data",c.env_vars["INFLUXDB"]["BUCKET"], data)
###
# time.sleep(5000)
### option 2
point = Point("mem")\
  .tag("host", "host1")\
  .field("used_percent", 23.43234543)

write_api.write("data",c.env_vars["INFLUXDB"]["BUCKET"], point)
###

write_api.flush()


# q = 'from(bucket: "my_bucket") |> range(start:-1h)'
# t = client.query_api().query(q, org="85c0d22689946e37")
# print(t)

for i in range(5000):
  val = random.randint(0, 100)
  print(f"{i}: {val}")

  # point = Point("mem") \
  #   .tag("host", "host1") \
  #   .field("used_percent", val)

  data = f"mem,host=host1 used_percent={val}"

  write_api.write("data", c.env_vars["INFLUXDB"]["BUCKET"], data)
  time.sleep(1)

  write_api.flush()
