
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char x;
  x = Serial.read();
  Serial.print(x);
  delay(500);
} 

