#include <Servo.h>

Servo myServo;
const int trigPin = 7;  // HC-SR04 Trig pin
const int echoPin = 6;  // HC-SR04 Echo pin
const int led = 13;     // LED pin

long distance;
long duration;
bool objectDetected = false;  // Flag for object detection

unsigned long previousMillis = 0; // LED blink timing
const int ledBlinkInterval = 300; // LED blink time

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(led, OUTPUT);
}

// Function to get distance from HC-SR04
float getDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2; // Convert to cm
}

// Function to move servo continuously
void rotate() {
  static int pos = 0;
  static bool movingRight = true;
  
  if (movingRight) {
    pos++;
    if (pos >= 90) movingRight = false;
  } else {
    pos--;
    if (pos <= 0) movingRight = true;
  }
  
  myServo.write(pos);
  //delay(20); // Smooth motion
}

void loop() {
  distance = getDistance();
  Serial.println(distance);

  if (distance > 0 && distance <= 20) {
    if (myServo.attached()) {
      myServo.detach();
      Serial.println("Servo detached");
    }

    // Non-blocking LED blinking
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= ledBlinkInterval) {
      previousMillis = currentMillis;
      digitalWrite(led, !digitalRead(led)); // Toggle LED
    }

  } else {
    if (!myServo.attached()) {
      myServo.attach(9);
      Serial.println("Servo reattached");
    }
    
    digitalWrite(led, LOW); // Turn off LED when no object
    rotate(); // Move servo smoothly
  }
}