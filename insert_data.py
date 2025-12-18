from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "https://us-east-1-1.aws.cloud2.influxdata.com/"
token = "TOKEN"
org = "Christ University"
bucket = "smart_agri_sensors"

client = InfluxDBClient(
    url=url,
    token=token,
    org=org,
    verify_ssl=False  
)

write_api = client.write_api(write_options=SYNCHRONOUS)

points = [
    Point("sensor_data")
    .tag("user_id", "OsEAPYdE5jVnYDJFdXiurKdaYDS2")
    .tag("field_id", "field1")
    .tag("crop_id", "crop1")
    .field("temperature", 30.5)
    .field("humidity", 60.0)
    .field("soil_moisture", 45.0),

    Point("sensor_data")
    .tag("user_id", "K5aAdSPgCeOydbJ3UuceQGKFNuk2")
    .tag("field_id", "field2")
    .tag("crop_id", "crop2")
    .field("temperature", 28.0)
    .field("humidity", 70.0)
    .field("soil_moisture", 55.0),

    Point("sensor_data")
    .tag("user_id", "3M1RcLAh3NVoxnDzeV3vKYQJNWr1")
    .tag("field_id", "field3")
    .tag("crop_id", "crop3")
    .field("temperature", 29.0)
    .field("humidity", 65.0)
    .field("soil_moisture", 50.0),

    Point("sensor_data")
    .tag("user_id", "4KmU1N4KmgcqIj10tEnvhJozf253")
    .tag("field_id", "field4")
    .tag("crop_id", "crop4")
    .field("temperature", 31.0)
    .field("humidity", 58.0)
    .field("soil_moisture", 48.0),

    Point("sensor_data")
    .tag("user_id", "acxY6VeurBTaJfZTTZEiFzzxQ0a2")
    .tag("field_id", "field5")
    .tag("crop_id", "crop5")
    .field("temperature", 27.5)
    .field("humidity", 72.0)
    .field("soil_moisture", 60.0)
]

write_api.write(bucket=bucket, org=org, record=points)

print("✅ Sensor data inserted successfully")
