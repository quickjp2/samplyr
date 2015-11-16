// Variables for the input pins
int P1G = D0;
int P1R = D1;
int P2G = D2;
int P2R = D3;
int P3G = D4;
int P3R = D5;
int P4G = D6;
int P4R = D7;

// Variables to prevent event multisending
bool P1Goff = false;
bool P1Roff = false;
bool P2Goff = false;
bool P2Roff = false;
bool P3Goff = false;
bool P3Roff = false;
bool P4Goff = false;
bool P4Roff = false;


void setup() {
  //Log boot-up to global boot log
  Spark.publish("notifyr/announce", "Samplyr Online!");
  
  pinMode(P1G, INPUT_PULLDOWN);
  pinMode(P1R, INPUT_PULLDOWN);
  pinMode(P2G, INPUT_PULLDOWN);
  pinMode(P2R, INPUT_PULLDOWN);
  pinMode(P3G, INPUT_PULLDOWN);
  pinMode(P3R, INPUT_PULLDOWN);
  pinMode(P4G, INPUT_PULLDOWN);
  pinMode(P4R, INPUT_PULLDOWN);

}

void loop() {
  // Plate 1 Green is pressed
  switch (digitalRead(P1G))
  {
    case HIGH:
      if (P1Goff == false){
        Spark.publish("samplyr-announce","P1G");
        P1Goff = true;
      }
      break;
    
    case LOW:
      if (P1Goff){
        delay(500);
        P1Goff = false;
      }
      break;
  }
  
  // Plate 1 Red is pressed
  switch (digitalRead(P1R))
  {
    case HIGH:
      if (P1Roff == false){
        Spark.publish("samplyr-announce","P1R");
        P1Roff = true;
      }
      break;
    
    case LOW:
      if (P1Roff){
        delay(500);
        P1Roff = false;
      }
      break;
  }
  
  // Plate 2 Green is pressed
  switch (digitalRead(P2G))
  {
    case HIGH:
      if (P2Goff == false){
        Spark.publish("samplyr-announce","P2G");
        P2Goff = true;
      }
      break;
    
    case LOW:
      if (P2Goff){
        delay(500);
        P2Goff = false;
      }
      break;
  }
  
  // Plate 2 Red is pressed
  switch (digitalRead(P2R))
  {
    case HIGH:
      if (P2Roff == false){
        Spark.publish("samplyr-announce","P2R");
        P2Roff = true;
      }
      break;
    
    case LOW:
      if (P2Roff){
        delay(500);
        P2Roff = false;
      }
      break;
  }
  
  // Plate 3 Green is pressed
  switch (digitalRead(P3G))
  {
    case HIGH:
      if (P3Goff == false){
        Spark.publish("samplyr-announce","P3G");
        P3Goff = true;
      }
      break;
    
    case LOW:
      if (P3Goff){
        delay(500);
        P3Goff = false;
      }
      break;
  }
  
  // Plate 3 Red is pressed
  switch (digitalRead(P3R))
  {
    case HIGH:
      if (P3Roff == false){
        Spark.publish("samplyr-announce","P3R");
        P3Roff = true;
      }
      break;
    
    case LOW:
      if (P3Roff){
        delay(500);
        P3Roff = false;
      }
      break;
  }
  // Plate 4 Green is pressed
  switch (digitalRead(P4G))
  {
    case HIGH:
      if (P4Goff == false){
        Spark.publish("samplyr-announce","P4G");
        P4Goff = true;
      }
      break;
    
    case LOW:
      if (P4Goff){
        delay(500);
        P4Goff = false;
      }
      break;
  }
  
  // Plate 4 Red is pressed
  switch (digitalRead(P4R))
  {
    case HIGH:
      if (P4Roff == false){
        Spark.publish("samplyr-announce","P4R");
        P4Roff = true;
      }
      break;
    
    case LOW:
      if (P4Roff){
        delay(500);
        P4Roff = false;
      }
      break;
  }
}
