# from pymodbus.client.sync import ModbusSerialClient as ModbusClient
# from pymodbus.exceptions import ModbusException
import logging
import pymodbus
from pymodbus.pdu import ModbusRequest
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.serial import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Replace 'COM8' with the correct COM port for your setup
com_port = 'COM8'

# Create a Modbus client
client = ModbusClient(
    method='rtu',
    port=com_port,
    baudrate=38400,
    timeout=3,  # Increased timeout
    stopbits=1,
    bytesize=8,
    parity='N'
)

# Connect to the client
connection = client.connect()
if not connection:
    print("Failed to connect to the Modbus RTU server")
else:
    try:
        # Read holding registers
        rr = client.read_holding_registers(0, 1, 1)
        if not rr.isError():
            print(f"Read registers: {rr.registers}")
        else:
            print(f"Error reading registers: {rr}")

        # Write to a holding register
        rq = client.write_register(0, 123, 1)
        if not rq.isError():
            print("Write successful")
        else:
            print(f"Error writing register: {rq}")
    except ModbusException as e:
        print(f"Modbus error: {e}")

    # Close the client connection
    client.close()