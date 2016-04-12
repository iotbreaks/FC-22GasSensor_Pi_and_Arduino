/*
  FC-22_Polling.ino
  Created by Kenny from www.iotbreaks.vn, April 12, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte gasInPin = 12;  // FC-22 DOut connected to digital pin 12
volatile byte val = HIGH; // variable to store the read value from gas sensor. 
                          // Default is HIGH for inactive state of gas sensor

void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(gasInPin, INPUT);
}

void loop() {
  val = digitalRead(gasInPin);
  digitalWrite(ledOutPin, val);
  delay(200);
}
