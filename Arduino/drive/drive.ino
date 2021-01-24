void setup() {
  Serial.begin(9600);

  //Setup Channel A
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin

  //Setup Channel B
  pinMode(13, OUTPUT); //Initiates Motor Channel A pin
  pinMode(8, OUTPUT);  //Initiates Brake Channel A pin
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    if (data == "Move forward") {
      leftMotorForward();
      rightMotorForward();
    }

    else if (data == "Turn left") {
      rightMotorForward();
    }

    else if (data == "Turn right") {
      leftMotorForward();
    }

    else if (data == "Stop moving") {
      stopMoving();
    }
    
    Serial.println(data + " from Arduino");
  }
}

void stopMoving() {
  digitalWrite(9, HIGH);  //Engage the Brake for Channel A
  digitalWrite(8, HIGH);  //Engage the Brake for Channel B
}

void leftMotorForward() {
  //Motor A forward @ half speed
  digitalWrite(12, HIGH); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, 255);   //Spins the motor on Channel A at half speed
}

void rightMotorForward() {
  //Motor B forward @ half speed
  digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, 255);   //Spins the motor on Channel B at half speed
}
