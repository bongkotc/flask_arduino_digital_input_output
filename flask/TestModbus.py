from ModbusClientWrapper import ModbusClientWrapper

def main():
    port = 'COM8'  # com port ที่ใช้
    modbus_client = ModbusClientWrapper(port=port)

    #เปิดการเชื่อมต่อ
    if not modbus_client.connect():
        print("Failed to connect to the Modbus RTU server")
        return

    # ทดสอบอ่าน holding registers
    registers = modbus_client.read_holding_registers(address=0, count=1)
    if registers is not None:
        print(f"Read registers: {registers}")
    else:
        print("Failed to read registers")

    # ทดสอบเขียน to a holding register
    if modbus_client.write_register(address=0, value=125):
        print("Write successful")
    else:
        print("Failed to write register")

    #ปิดการเชื่อมต่อ
    modbus_client.close()

if __name__ == "__main__":
    main()
