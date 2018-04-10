#include <Wire.h>
#include <AccelStepper.h>

int stepPin = 9;
int dirPin = 8;
int enPin = 7;
AccelStepper stepper(AccelStepper::DRIVER, stepPin, dirPin);
#define SLAVE_ADDRESS 0x04


int got;
int mode = 0;   //0 is starting up,1= ready for command 2 is moving

int pos;
int steps, target;

int lowerLimitPin = 6;
int lowerLimitVar = 1;

void setup() {
  Serial.begin(9600);
  Serial.println("running i2cSendEndlessly");
  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(sendData);
  Wire.onReceive(getData);

  pinMode(lowerLimitPin, INPUT_PULLUP);
  pinMode(enPin, OUTPUT);
  
  //  STEPPER SHIT
  stepper.setMaxSpeed(4000);
  stepper.setAcceleration(2000);
}

////////////////////////////////LOOP


void loop() {
  
  if(mode == 0){           // starting up
    lowerLimitVar = digitalRead(lowerLimitPin);
    Serial.println(lowerLimitVar);
    zero();
  }
  
  
  if(mode == 1){
    if(steps != 0){
    Serial.print("got a step command, moving to "); Serial.println(steps);
    mode = 2;
    digitalWrite(enPin, LOW);
    stepper.moveTo(steps);
    pos = steps;
    steps = 0;
    
  }
}
 if(mode == 2){
   stepper.run();
   
 //Serial.println(stepper.distanceToGo());
  if(stepper.distanceToGo() == 0){
  Serial.println("done steppin'");
  mode = 1;
  }
 }


}




void sendData(){
  //Serial.println("");
  Serial.print("sending ");Serial.println(mode);
  Wire.write(mode);

}

void getData(){
  got = Wire.read();  // get that data
  Serial.print("Just Got "); Serial.println(got);

  if(got == 1){    //1 is a status request. sends back mode and does nothing else
    Serial.print("got status request. Sending "); Serial.println(mode);
  }
    if(got > 1){    //this is a position to go to
      steps = -got * 10;
      
      Serial.println("got a move command");
      Serial.println(steps);
      Serial.println(mode);
  }
  if(got == 255){
    
  }
  
  if (got == 0){
    zero();
  }
  

}




void zero(){
  digitalWrite(dirPin, HIGH);
  while(lowerLimitVar != 0){
    lowerLimitVar = digitalRead(lowerLimitPin);
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(300);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(300);
  }
  stepper.setCurrentPosition(0);
  digitalWrite(enPin, HIGH);
  Serial.println("found lower limit");
  pos = 0;
  mode = 1;  //  into readiness mode
}





