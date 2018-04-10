
#include <Wire.h>

/*
 * arduino A4 ---> RasPi SDA1 (pin 3)
 * arduino A5 ---> RasPi SCL1 (pin 5)
 */

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
int testint;

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);         // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);

    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);

    Serial.println("running i2cArduino");
}

void loop() {
    delay(100);
}

// callback for received data
void receiveData(int byteCount){

    while(Wire.available()) {
        number = Wire.read();
        if (Wire.available() > 1)  // at least 2 bytes
        {
          number = Wire.read() * 256 + Wire.read();
        }

        if(number == 69){
          Serial.println("nice");
          
        }
        Serial.print("data received: ");
        Serial.println(number);
        testint = number * 2;
        
        sendData();
        if (number == 1){
            if (state == 0){
                digitalWrite(13, HIGH); // set the LED on
                state = 1;
            }
            else{
                digitalWrite(13, LOW); // set the LED off
                state = 0;
            }
         }
     }
}

// callback for sending data
void sendData(){
    
    Wire.write(number);
    Serial.print("sendData "); Serial.println(number);
}

void sendConfirmation(int a){
  int b = a;
  Wire.write(b);
  Serial.print("sent confirmation ");Serial.println(b);
}

