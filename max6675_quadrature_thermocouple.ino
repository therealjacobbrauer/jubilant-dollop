// this example is public domain. enjoy!
// www.ladyada.net/learn/sensors/thermocouple

#include "max6675.h"

int gndPin = 2;
int vccPin = 3;
int thermoCLK = 4;
int thermoCS1 = 5;
int thermoDO = 6;

int thermoCS2 = 10;
int thermoCS3 = 7;
int thermoCS4 = 8;

MAX6675 thermocouple1(thermoCLK, thermoCS1, thermoDO);
MAX6675 thermocouple2(thermoCLK, thermoCS2, thermoDO);
MAX6675 thermocouple3(thermoCLK, thermoCS3, thermoDO);
MAX6675 thermocouple4(thermoCLK, thermoCS4, thermoDO);

  
void setup() {
  Serial.begin(115200);
  // use Arduino pins 
  pinMode(vccPin, OUTPUT); digitalWrite(vccPin, HIGH);
  pinMode(gndPin, OUTPUT); digitalWrite(gndPin, LOW);
  delay(500);
  
  //Serial.println("MAX6675 test");
  // wait for MAX chip to stabilize
  delay(500);
}

void loop() {
  // basic readout test, just print the current temp
  
   Serial.print(thermocouple1.readCelsius());
   
   Serial.print(","); 
   Serial.print(thermocouple2.readCelsius());
   
   Serial.print(","); 
   Serial.print(thermocouple3.readCelsius());

   Serial.print(","); 
   Serial.println(thermocouple4.readCelsius());

   delay(101);
   
}
