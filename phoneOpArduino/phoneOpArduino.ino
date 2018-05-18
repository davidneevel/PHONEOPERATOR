#include <Wire.h>
#define SLAVE_ADDRESS 0x04

#include <AccelStepper.h>
int vstepPin = 9;
int vdirPin = 8;
int venPin = 7;
int hstepPin = 10;
int hdirPin = 11;
int henPin = 12;
AccelStepper vstepper(AccelStepper::DRIVER, vstepPin, vdirPin);
AccelStepper hstepper(AccelStepper::DRIVER, hstepPin, hdirPin);

/* Currently if this is told by raspi to move to the same x or y coordinates twice in a row
 *  it hangs up and never tells the raspi that it's ready!
*/

#include <Servo.h>
Servo servo;
Servo onOffServo;
int servoUp = 65;
int servoDown = 110;
int servoDownLight = 102;

//Variables for first byte of array rec'd from raspi
int moveYCmd = 1;
int moveXCmd = 2;
int servoUpCmd = 3;
int servoDownCmd = 4;
int servoTapCmd = 5;
int servoToCmd = 6;
int zeroCmd = 7;
int moveXYCmd = 8;
int slowTapCmd = 9;
int lightTapCmd = 10;
int onOffCmd = 11;


int tappy = 0;
int slowTappy = 0;
int lightTappy = 0;

int lowerLimitPin = 6;
int upperLimitPin = 13;  // originally pin 5 but switched so i can put the pwm to use on a servo
int leftLimitPin  = 4;
int lowerLimitVar = 1; // goes low when switched
int upperLimitVar = 1; // same
int leftLimitVar = 1;

int mode = 0;   //0 is starting up,1= ready for command 2 is moving

byte thisArray[6];
int pos;
int targetX, targetY, prevTargetX, prevTargetY, currentX, currentY;
int counting;
int distancesToGo;
int hToGo, vToGo;
int doMove;

int onOffClick = 110;
int onOffUp = 70;
int onOff;

void setup() {
  Wire.begin(SLAVE_ADDRESS);                
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(requestEvent);
  Serial.begin(9600);           // start serial for output
  Serial.println("running PHONEOP");

  //  STEPPER SHIT
  vstepper.setMaxSpeed(7000);
  vstepper.setAcceleration(8000);
  vstepper.setPinsInverted(1,0,0);  // 1 inverts, 0 doesn't. (direction, step, enable)
  hstepper.setMaxSpeed(5000);
  hstepper.setAcceleration(8000);
  

  servo.attach(3);
  onOffServo.attach(5);
  onOffServo.write(onOffUp);

  pinMode(vstepPin, OUTPUT);// don't need to set these for accelstepper
  pinMode(vdirPin, OUTPUT); // but for zeroing they are controlled manually
  pinMode(hstepPin, OUTPUT);
  pinMode(hdirPin, OUTPUT);
  pinMode(upperLimitPin, INPUT_PULLUP);
  pinMode(lowerLimitPin, INPUT_PULLUP);
  pinMode(leftLimitPin, INPUT_PULLUP);
  pinMode(henPin, OUTPUT);
  pinMode(venPin, OUTPUT);
}
                                                     
//                                                        _     ___   ___  ____  
//                                                       | |   / _ \ / _ \|  _ \ 
//                                                       | |  | | | | | | | |_) |
//                                                       | |__| |_| | |_| |  __/ 
//                                                       |_____\___/ \___/|_|  


void loop() {
  if(mode == 0){  //startup mode
    zero();           //find zero
  }
  
//    if(doMove == 1){
//      Serial.println("doMove loop");
//      mode = 2;
//      if(targetY != prevTargetY){
//        vstepper.moveTo(targetY);
//        digitalWrite(venPin, LOW);
//        Serial.print("targetY acquired");
//      }
//     if(targetX !=prevTargetX){
//      hstepper.moveTo(targetX);
//      digitalWrite(henPin, LOW);
//      Serial.print("targetX acquired"); 
//     }
//     doMove = 0;
//    }

if(mode == 2){
    if(targetY != vstepper.currentPosition()){
      p("targetY acquired");
      digitalWrite(venPin, LOW);
      vstepper.moveTo(targetY);
      vToGo = vstepper.distanceToGo();
      p("V distance to go:");
      Serial.println(vstepper.distanceToGo());    
    }
    
    Serial.print("targetX = ");Serial.print(targetX); Serial.print(" Current X = "); Serial.println(currentX);
    if(targetX != hstepper.currentPosition()){
      p("x target acquired");
      digitalWrite(henPin, LOW);
      hstepper.moveTo(targetX);
      hToGo = hstepper.distanceToGo();
       Serial.print("H distance to go:"); pp(hToGo);
   
      }
      distancesToGo = abs(hToGo) + abs(vToGo);

      if(distancesToGo != 0){
              Serial.print("distances to go");
              pp(distancesToGo);
        while(distancesToGo != 0){
          hstepper.run();
          vstepper.run();
          hToGo = hstepper.distanceToGo();
          vToGo = vstepper.distanceToGo();
          distancesToGo = abs(hToGo) + abs(vToGo);
        }
        }
        else{
          Serial.println("no move necessary");
        }
        p("done moving xy.");
        p(" ");
//        digitalWrite(venPin, HIGH);
//        digitalWrite(henPin, HIGH);
//targetY = 0;
//targetX = 0;
           // back to readiness!!!!!!!!!
        
      mode = 1;
}
    
//  Serial.println(mode);

if(tappy == 1){
  mode = 2;
  Serial.println("tappy");
  if(lightTappy == 1){
    servo.write(servoDownLight);
    Serial.println("LightTappy");
    lightTappy = 0;
  }else{
     servo.write(servoDown);
  }
  delay(250);
  if(slowTappy == 1){
    delay(300);
    slowTappy = 0;
    Serial.println("SlowTappy");
  }
  servo.write(servoUp);
//  delay(300);
  tappy = 0;
  Serial.println(" ");
  mode = 1;
}

if(onOff == 1){
  mode = 2;
  Serial.write("clicking");
  onOffServo.write(onOffClick);
  delay(500);
  Serial.write("releasing onOff");
  onOffServo.write(onOffUp);
  onOff = 0;
  mode = 1;
}

//prevTargetX = targetX;
//prevTargetY = targetY;
}                  

//                        
//                          _____ _   _ ____    _     ___   ___  ____  
//                         | ____| \ | |  _ \  | |   / _ \ / _ \|  _ \ 
//                         |  _| |  \| | | | | | |  | | | | | | | |_) |
//                         | |___| |\  | |_| | | |__| |_| | |_| |  __/ 
//                         |_____|_| \_|____/  |_____\___/ \___/|_|    
//                                                                    

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent() {
  mode = 1;
byte index = 0;
while(Wire.available() > 0 && index < 5)
{
  thisArray[index] = Wire.read();
  index++;
}
int a = thisArray[0];
int b = thisArray[1];
int c = thisArray[2];
int d = thisArray[3];
int e = thisArray[4];
Serial.print(a); Serial.print(", ");
Serial.print(b); Serial.print(", ");
Serial.print(c); Serial.print(", ");
Serial.print(d); Serial.print(", ");
Serial.println(e); 

if(a == moveXYCmd){
  mode = 2;
  targetX = b * 100 + c;
  targetY = d * 100 + e;
  p("target X "); pp(targetX);
  p("target Y "); pp(targetY);
 
}

if(a == moveYCmd){
  mode = 2;
  targetY = b * 100 +c;  
//  moveY(targetY);
  Serial.print("targetY = "); Serial.println(targetY);
}else{

if(a == moveXCmd){
  mode = 2;
  targetX = b * 100 + c;
  Serial.print("targetX = "); Serial.println(targetX);
}else{

if(a == servoToCmd){
  mode = 2;
  servo.write(c);      //b is sent as 0, c contains position for servoTo command
  delay(250);
  
  mode = 1;
}else{
if(a == zeroCmd){
  mode = 2;
  Serial.println("got a zero command");
  mode = 0;             // make it think it's starting up.
}else{

if(a == servoTapCmd){
  mode = 2;
//  tappy();
  tappy = 1;
}else{
  if(a == slowTapCmd){
    mode = 2;
    tappy = 1;
    slowTappy = 1;
  }else{
    if(a == lightTapCmd){
      mode = 2;
      tappy = 1;
      lightTappy = 1;
    }else{
      if(a == onOffCmd){
        mode = 2;
        onOff = 1;
      }
    }
  }
}
}}}}

}   /////////////////END RECIEVE EVENT




void requestEvent(){  //When status requested from raspi
  if(mode == 1){ 
    Wire.write(100);             //100 means ready.
    p("ready! sending 100");
  }else{
    Wire.write(69);              //69 means busy
//   p("busy! Sending 69");
  }
 
}


void zero(){
 // zeroTop();
  servo.write(servoUp);
  zeroBottom();
  zeroLeft();
  Serial.println("zeroed");
  mode = 1;
}


void zeroTop(){
  mode = 2;
  digitalWrite(venPin, LOW);
  upperLimitVar = digitalRead(upperLimitPin);
  servo.write(servoUp);
  digitalWrite(vdirPin, HIGH);
   while(upperLimitVar != 0){
    upperLimitVar = digitalRead(upperLimitPin);
    digitalWrite(vstepPin, HIGH);
    delayMicroseconds(300);
    digitalWrite(vstepPin, LOW);
    delayMicroseconds(300);
  }
  p("found upper limit! heading down");
  int counting = 0;
  digitalWrite(venPin, HIGH);
  mode = 2;
}

void zeroBottom(){
  mode = 2;              //moving
  digitalWrite(venPin, LOW);
  lowerLimitVar = digitalRead(lowerLimitPin);
  if(lowerLimitVar == 0){                     // if it's already sitting on the switch, move off and resettle on it
    digitalWrite(vdirPin, LOW);
    for(int i = 0; i < 200; i ++){
      digitalWrite(vstepPin, HIGH);
      delayMicroseconds(300);
      digitalWrite(vstepPin, LOW);
      delayMicroseconds(300);
    }
  }
  lowerLimitVar = digitalRead(lowerLimitPin);  //recheck the switch. it should have moved from closed to open.
  digitalWrite(vdirPin, HIGH);
  while(lowerLimitVar != 0){
    lowerLimitVar = digitalRead(lowerLimitPin);
    digitalWrite(vstepPin, HIGH);
    delayMicroseconds(350);
    digitalWrite(vstepPin, LOW);
    delayMicroseconds(350);
    counting += 1;
  }

  
  vstepper.setCurrentPosition(0);
  digitalWrite(venPin, HIGH);
  Serial.println("found lower limit");
  pos = 0;
  vstepper.setCurrentPosition(0);
  targetY = 0;
  mode = 1;  //  into readiness mode
}

void zeroLeft(){
  mode = 2;           //moving
  digitalWrite(henPin, LOW);
  leftLimitVar = digitalRead(leftLimitPin);
  if(leftLimitVar == 0){
    digitalWrite(hdirPin, HIGH);
    for(int i = 0; i < 150; i++){
      digitalWrite(hstepPin, HIGH);
      delayMicroseconds(300);
      digitalWrite(hstepPin, LOW);
      delayMicroseconds(300);
    }
  }
  leftLimitVar = digitalRead(leftLimitPin);
  Serial.println("zeroing left");
    digitalWrite(hdirPin, LOW);
    while(leftLimitVar != 0){
      leftLimitVar = digitalRead(leftLimitPin);
      digitalWrite(hstepPin, HIGH);
      delayMicroseconds(300);
      digitalWrite(hstepPin, LOW);
      delayMicroseconds(300);
  }
  digitalWrite(henPin, HIGH);
    hstepper.setCurrentPosition(0);
  targetX = 0;
  mode = 1;
}
void p(String a){
  Serial.println(a);
}
void pp(int a){
  Serial.println(a);
  }


