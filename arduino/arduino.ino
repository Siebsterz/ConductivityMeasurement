int analogPin0 = A0;
int v1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  v1 = analogRead(analogPin0);
  Serial.println(v1);
  delay(500);
}
