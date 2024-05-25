#include<Arduino.h>
#include <SoftwareSerial.h>
#include <ModbusRTUSlave.h>

/*
 * เกี่ยวกับตัวแปร Pin
 */
const byte ledPin = 9;//Pin เอาท์พุตที่ต้องการแสดงผล LED
const byte buttonPin = 2;//Pin อินพุต ที่อ่านจากสวิตช์
const byte rxPin = 10;//SoftwareSerial
const byte txPin = 11;//SoftwareSerial

/*
 * เกี่ยวกับตัวแปร Modbus
 * 1 word = 2 bytes
 */
const word bufSize = 256;//กำหนดค่าการจอง memory ไว้ 256 bytes
const word buttonHoldingRegisters = 2;//Address ที่ต้องการอ่านสวิตช์
const word ledHoldingRegisters = 3;//Address ที่ต้องเขียนสั่งงานหลอดไฟ LED
const word buttonAddress = 0;//เริ่มที่ 0
const word ledAddress = 1;
const unsigned long baud = 38400;//สัญญาณการสื่อสาร
const byte id = 1;//เป็นหมายเลข ID ของอุปกรณ์
byte buf[bufSize];//จอง memory ไว้ 256 bytes


byte ledValue = 0;//เก็บสถานะล่าสุดของ Led ,0=ดับ และ 1=ติด
byte buttonValue = 0;//เก็บสถานะล่าสุดของ สวิตช์ ,0=ดับ และ 1=ติด

//เรียกใช้งาน SoftwareSerial โดยตั้งค่า Pin เรื่มต้น
SoftwareSerial mySerial(rxPin, txPin);

//เรียกใช้งาน ModbusRTUSlave โดยตั้งค่า เรื่มต้น
//mySerial ให้ modbus ผูกกับตัวแปร mySerial ที่รับส่งข้อมูล
ModbusRTUSlave modbus(mySerial, buf, bufSize);

//เมื่อ Client อ่านข้อมูล holdingRegister จะ callback มาที่ฟังก์ชันนี้
long holdingRegisterRead(word address) {
  if (address == buttonAddress){
    buttonValue = !digitalRead(buttonPin);
    return buttonValue;
  } 
  else if (address == ledAddress) return ledValue;
  else return false;
}

//เมื่อ Client เขียนข้อมูล holdingRegister จะ callback มาที่ฟังก์ชันนี้
boolean holdingRegisterWrite(word address, word value) {
  if (address == ledAddress) {
    ledValue = value;
    digitalWrite(ledPin, (ledValue==1)?HIGH:LOW);
  }
  return true;
}

void setup() {
  //ตั้งค่า Pin
  pinMode(ledPin, OUTPUT);//ให้ Pin ที่สั่งงาน Led เป็น Output 
  pinMode(buttonPin, INPUT_PULLUP);//ให้ Pin ที่อ่านค่าจากสิตช์ เป็น Input Pullup ซึ่งใช้ ตัวต้านทานภายใน MCU

  //ตั้งค่าความเร็วในการสื่อสาร
  mySerial.begin(baud);

  //ตั้งค่า Modbus ด้วยการระบุ ID ของตัวเอง และความเร็วในการสื่อสาร
  modbus.begin(id, baud);

  //ตั้งค่า HoldingRegister ด้วยหมายเลข Address และผูกกับฟังก์ชัน Callback
  modbus.configureHoldingRegisters(buttonHoldingRegisters, holdingRegisterRead, holdingRegisterWrite);
  modbus.configureHoldingRegisters(ledHoldingRegisters, holdingRegisterRead, holdingRegisterWrite);
}

void loop() {
  // Modbus โปรโตคอลจะรัน ใน Loop นี้
  modbus.poll();
}
