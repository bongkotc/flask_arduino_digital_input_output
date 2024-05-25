from ModbusClientWrapper import ModbusClientWrapper

def main():
    port = 'COM8'  # Replace with the correct COM port
    modbus_client = ModbusClientWrapper(port=port)

    if not modbus_client.connect():
        print("Failed to connect to the Modbus RTU server")
        return

    # Read holding registers
    registers = modbus_client.read_holding_registers(address=0, count=1)
    if registers is not None:
        print(f"Read registers: {registers}")
    else:
        print("Failed to read registers")

    # Write to a holding register
    if modbus_client.write_register(address=0, value=125):
        print("Write successful")
    else:
        print("Failed to write register")

    # Close the client connection
    modbus_client.close()

if __name__ == "__main__":
    main()
