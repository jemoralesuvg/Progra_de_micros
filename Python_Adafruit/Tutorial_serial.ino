unsigned char data = 0;
void setup() {
  pinMode(13, OUTPUT);
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("Bienvenidos a Clase!");
  digitalWrite(13,HIGH);
}

void loop() { // run over and over
  if (Serial.available()) {
    data = Serial.read();
    if(data =='a')
    {
      //Apagar LED
      digitalWrite(13,LOW);
      Serial.println(String("Recibo '")+String((char)data)+String("'. Led agapado."));
    }else{
      //Encender LED
      digitalWrite(13,HIGH);
      Serial.println(String("Recibo '")+String((char)data)+String("'. Led encendido"));
    }
  }
}
