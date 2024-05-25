import logging
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.serial import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException

class ModbusClientWrapper:
    def __init__(self, port, baudrate=38400, timeout=5, stopbits=1, bytesize=8, parity='N', unit=1):
        self.client = ModbusClient(
            method='rtu',
            port=port,
            baudrate=baudrate,
            timeout=timeout,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity
        )
        self.unit = unit
        logging.basicConfig()
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)

    def connect(self):
        return self.client.connect()

    def close(self):
        self.client.close()

    def read_holding_registers(self, address, count):
        try:
            rr = self.client.read_holding_registers(address, count, self.unit)
            if not rr.isError():
                print(f"Read registers: {rr.registers}")
                return rr.registers
            else:
                self.log.error(f"Error reading registers: {rr}")
                return None
        except ModbusException as e:
            self.log.error(f"Modbus error: {e}")
            return None

    def write_register(self, address, value):
        try:
            rq = self.client.write_register(address, value, self.unit)
            if not rq.isError():
                return True
            else:
                self.log.error(f"Error writing register: {rq}")
                return False
        except ModbusException as e:
            self.log.error(f"Modbus error: {e}")
            return False
