import json
import pandas
#replace file path with file path
with open("test.geojson") as f:
  data = json.load(f)
#gets just the feature set
df = pandas.DataFrame(data["features"])
#replace test with save file path
df.to_csv("test.csv")

