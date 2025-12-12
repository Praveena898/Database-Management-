const { InfluxDB } = require("@influxdata/influxdb-client");

const url= "https://us-east-1-1.aws.cloud2.influxdata.com";
const token= "aJ_BWqQUs-zasjE9y2T5IjxXhwBHp-yZNV51gjQAz36Wiy-_J0YiS55CSmqc0nI7vv8w_1nNoI8G295RqlbQ2A==";
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
