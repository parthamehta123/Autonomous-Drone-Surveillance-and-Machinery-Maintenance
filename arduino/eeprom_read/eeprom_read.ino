int address = 0;
byte value;
#include <EEPROM.h>
float sensorVals[] = {0,0,0,0,0};
int i = 0 ;

void setup() {
  // initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
}

void loop() {
  // read a byte from the current address of the EEPROM
  value = EEPROM.read(address);

  Serial.print(address);
  Serial.print("\t");
  sensorVals[i]=value;
  Serial.println();

  address = address + 1;
  if (address == EEPROM.length()) {
    address = 0;
  }
  i=i+1;
  delay(500);
}
