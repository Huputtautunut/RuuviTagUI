import asyncio
import os
from quart import Quart, render_template, jsonify  # Use Quart instead of Flask

os.environ["RUUVI_BLE_ADAPTER"] = "bleak"

import ruuvitag_sensor.log
from ruuvitag_sensor.ruuvi import RuuviTagSensor

ruuvitag_sensor.log.enable_console()

app = Quart(__name__)  # Use Quart here

latest_data = None

async def update_data():
    global latest_data
    async for data in RuuviTagSensor.get_data_async():
        latest_data = data
        print(f"Updated data: {latest_data}")

@app.route('/')
async def index():
    return await render_template('index.html')

@app.route('/basic')
async def basic():
    return await render_template('basic.html')

@app.route('/data')
async def get_data():
    if latest_data is None:
        print("No data available")
        return jsonify({"error": "No data available"}), 404
    return jsonify(latest_data)



async def main():
    # Start the data update task
    asyncio.create_task(update_data())
    # Start the Quart server
    await app.run_task(host='localhost', port=5000, debug=True)

if __name__ == "__main__":
    asyncio.run(main())
