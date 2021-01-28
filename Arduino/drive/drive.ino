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

    String direction = data.substring(0, 1);
    int speed = data.substring(1, 4).toInt();
    if (speed > 255) {
      speed = 255;
    }
    
    if (direction == "f") {
      forward(speed);
    }

    else if (direction == "l") {
      left(speed);
    }

    else if (direction == "r") {
      right(speed);
    }

    else if (direction == "b") {
      backward(speed);
    }

    else if (direction == "s") {
      stopMoving();
    }
    
    Serial.println(data + " from Arduino");
  }
}

void stopMoving() {
  digitalWrite(9, HIGH);  //Engage the Brake for Channel A
  digitalWrite(8, HIGH);  //Engage the Brake for Channel B
}

void forward(int speed) {
  //Motor A forward
  digitalWrite(12, LOW); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, speed);   //Spins the motor on Channel A
  //Motor B forward
  digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, speed);   //Spins the motor on Channel B
}

void backward(int speed) {
  //Motor A backward
  digitalWrite(12, HIGH); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, speed);   //Spins the motor on Channel A
  //Motor B backward
  digitalWrite(13, LOW); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, speed);   //Spins the motor on Channel B
}

void left(int speed) {
  digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, speed);   //Spins the motor on Channel B
}

void right(int speed) {
  digitalWrite(12, LOW); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, speed);   //Spins the motor on Channel A
}
