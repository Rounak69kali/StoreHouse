// Define IR sensor pins
#define IR_SENSOR_RIGHT 11
#define IR_SENSOR_LEFT 12
#define MOTOR_SPEED 180 // You can adjust this

// Right motor pins
int enableRightMotor = 6;
int rightMotorPin1 = 7;
int rightMotorPin2 = 8;

// Left motor pins
int enableLeftMotor = 5;
int leftMotorPin1 = 9;
int leftMotorPin2 = 10;

void setup() {
  // Increase PWM frequency for smooth motor control
  TCCR0B = TCCR0B & B11111000 | B00000010; // Sets PWM freq to 7812.5 Hz for pins 5 & 6

  // Set motor pins as outputs
  pinMode(enableRightMotor, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  pinMode(enableLeftMotor, OUTPUT);
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);

  // Set IR sensor pins as inputs
  pinMode(IR_SENSOR_RIGHT, INPUT);
  pinMode(IR_SENSOR_LEFT, INPUT);

  // Optional: Start Serial for debugging
  // Serial.begin(9600);

  // Initially stop both motors
  rotateMotor(0, 0);
}

void loop() {
  // Read sensor values
  int rightIR = digitalRead(IR_SENSOR_RIGHT); // LOW = white surface, HIGH = black line
  int leftIR = digitalRead(IR_SENSOR_LEFT);

  // Optional: Debugging
  // Serial.print("Right: "); Serial.print(rightIR);
  // Serial.print(" | Left: "); Serial.println(leftIR);

  if (rightIR == LOW && leftIR == LOW) {
    // Both sensors see white surface -> move forward
    rotateMotor(MOTOR_SPEED, MOTOR_SPEED);
  }
  else if (rightIR == HIGH && leftIR == LOW) {
    // Right sensor sees black line -> stop right motor to turn right
    rotateMotor(0, MOTOR_SPEED);
  }
  else if (rightIR == LOW && leftIR == HIGH) {
    // Left sensor sees black line -> stop left motor to turn left
    rotateMotor(MOTOR_SPEED, 0);
  }
  else {
    // Both sensors see black line -> stop
    rotateMotor(0, 0);
  }
}

// Motor control function
void rotateMotor(int rightSpeed, int leftSpeed) {
  // Right Motor Control
  if (rightSpeed > 0) {
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);
  } else {
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, LOW);
  }

  // Left Motor Control
  if (leftSpeed > 0) {
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
  } else {
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, LOW);
  }

  // Apply speed using PWM
  analogWrite(enableRightMotor, abs(rightSpeed));
  analogWrite(enableLeftMotor, abs(leftSpeed));
}
