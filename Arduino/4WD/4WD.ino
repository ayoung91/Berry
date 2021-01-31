#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *m1 = AFMS.getMotor(1);
Adafruit_DCMotor *m2 = AFMS.getMotor(2);
Adafruit_DCMotor *m3 = AFMS.getMotor(3);
Adafruit_DCMotor *m4 = AFMS.getMotor(4);

void setup() {
  Serial.begin(9600);
  AFMS.begin();
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    String direction = data.substring(0, 1);
    int speed = data.substring(1, 4).toInt();

    m1->setSpeed(speed);
    m2->setSpeed(speed);
    m3->setSpeed(speed);
    m4->setSpeed(speed);

    if (direction == "f") {
      m1->run(FORWARD);
      m2->run(FORWARD);
      m3->run(FORWARD);
      m4->run(FORWARD);
    }

    else if (direction == "r") {
      m1->run(FORWARD);
      m4->run(FORWARD);
    }

    else if (direction == "l") {
      m2->run(FORWARD);
      m3->run(FORWARD);
    }
    
    else if (direction == "b") {
      m1->run(BACKWARD);
      m2->run(BACKWARD);
      m3->run(BACKWARD);
      m4->run(BACKWARD);
    }

    else if (direction == "s") {
      m1->run(RELEASE);
      m2->run(RELEASE);
      m3->run(RELEASE);
      m4->run(RELEASE);
    }
    
    Serial.println(data + " from Arduino");
  }
}
