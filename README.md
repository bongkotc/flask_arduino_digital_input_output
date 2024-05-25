# Flask Arduino Digital Input/Output

| รันเว็บด้วยชื่อ app.py |
|----------|
| python -u app.py |

<img src="images/flask_web.png" alt="My Image" width="500" height="300">

# อุปกรณ์
|  | รายการ | จำนวน |
|----------|----------|----------|
| 1 | Arduino UNU| 1 |
| 2 | Switch กดติด ปล่อยดับ | 1 |
| 3 | หลอด Led | 1 |
| 4 | ตัวต้านทาง 220 ohm | 1 |

# Wiring
| Arduino PIN | Component |
|----------|----------|
| 2 | LED|
| 9 | Switch |

# Modbus Address
Arduino Device ID = 1
<br>
Holding Register
| Address | Description | Action |
|----------|----------|----------|
| 1 | Switch| Read |
| 2 | LED | Read/Write |


#Software ที่เกี่ยวข้อง
|  | รายการ | ภาษา |
|----------|----------|----------|
| 1 | VS Code| Python |
| 2 | Arduino IDE 1.8 | C/C++ |

#ไลบรารี่ Python
| ชื่อ | Version |
|----------|----------|
| Flask | 3.0.3 |
| pymodbus | 3.6.8 |
| pyserial | 3.5 |
| pymodbus | 3.6.8 |
             
