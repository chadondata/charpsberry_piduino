const int LED_PIN = 9;
const int SENSOR_PIN = A0;
const float MAX_FADE = 255.0;
const float MAX_POT = 1023.0;

int sensor_value = 0;
int fade_value = 0;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor_value = analogRead(SENSOR_PIN);
  //Serial.println(sensor_value);

  fade_value = int((float(sensor_value) / MAX_POT) * MAX_FADE);
  analogWrite(LED_PIN, fade_value);
  delay(15);
}
