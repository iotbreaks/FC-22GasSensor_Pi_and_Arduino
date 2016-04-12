/*
  FC-22_Interrupt.ino
  Created by Kenny from www.iotbreaks.vn, April 12, 2016.
  Released into the public domain.
  Tutorial: 
*/
const byte ledOutPin = 13; // LED connected to digital pin 13
const byte gasInPin = 2;  // FC-22 DOut connected to interrupt pin 2 (Int.0)
volatile byte val = HIGH; // variable to store the read value from gas sensor. 
                          // Default is HIGH for inactive state of gas sensor
void setup() {
  pinMode(ledOutPin, OUTPUT);
  pinMode(gasInPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(gasInPin), gasSensorDidChange, CHANGE);
  digitalWrite(ledOutPin,1);
}

void loop() {
  // Do nothing here
}

void gasSensorDidChange() {
  val = digitalRead(gasInPin);
  digitalWrite(ledOutPin, val);
}
