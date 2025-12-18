from influxdb_client import InfluxDBClient

url = "https://us-east-1-1.aws.cloud2.influxdata.com"
token =  "TOKEN"
org = "Christ University"
bucket = "smart_agri_sensors"

client = InfluxDBClient(
    url=url,
    token=token,
    org=org,
    verify_ssl=False
)

query_api = client.query_api()

farmers = [
    ("Farmer 1", "OsEAPYdE5jVnYDJFdXiurKdaYDS2"),
    ("Farmer 2", "K5aAdSPgCeOydbJ3UuceQGKFNuk2"),
    ("Farmer 3", "3M1RcLAh3NVoxnDzeV3vKYQJNWr1"),
    ("Farmer 4", "4KmU1N4KmgcqIj10tEnvhJozf253"),
    ("Farmer 5", "acxY6VeurBTaJfZTTZEiFzzxQ0a2")
]

for name, farmer_uid in farmers:
    query_user = f'''
    from(bucket: "{bucket}")
      |> range(start: -24h)
      |> filter(fn: (r) => r.user_id == "{farmer_uid}")
    '''

    result = query_api.query(org=org, query=query_user)

    print(f"\n{name}")
    for table in result:
        for record in table.records:
            print(
                record.get_time(),
                record.get_field(),
                record.get_value()
            )

crops = ["crop1", "crop2", "crop3", "crop4", "crop5"]

print("\n Sensor Data for ALL Crops:")

for crop in crops:
    query_crop = f'''
    from(bucket: "{bucket}")
      |> range(start: -24h)
      |> filter(fn: (r) => r.crop_id == "{crop}")
    '''

    result = query_api.query(org=org, query=query_crop)

    print(f"\nCrop: {crop}")
    for table in result:
        for record in table.records:
            print(
                record.get_time(),
                record.get_field(),
                record.get_value()
            )

client.close()
