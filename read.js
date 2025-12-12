const { InfluxDB } = require("@influxdata/influxdb-client");

const url= "https://us-east-1-1.aws.cloud2.influxdata.com";
const token= "<YOUR API TOKEN>";
const org= "Christ University";

const query= `
from(bucket: "sensor_data")
|> range(start: -1d)
|> filter(fn: (r) => r._measurement == "device_readings")
`;

const client = new InfluxDB({ url, token });

async function getData(){
    const queryApi = client.getQueryApi(org);
    const rows = [];

    for await (const{values } of queryApi.iterateRows(query)){
        rows.push(values);
    }

    console.log("InfluxDB Sensor Data: ");
    console.table(rows);
}

getData();

