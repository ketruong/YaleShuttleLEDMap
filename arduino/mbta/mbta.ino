#include <Adafruit_NeoPixel.h>

#define PACKET_SIZE 8

byte packet[PACKET_SIZE];
int packet_index = 0;
int total_bytes = 0;
boolean is_running = 1;

unsigned long last_data;

// Yale Blue Day line 
Adafruit_NeoPixel blue_dayline= Adafruit_NeoPixel(80, 2, NEO_GRB + NEO_KHZ800);

// Yale Red Day line 
Adafruit_NeoPixel redline= Adafruit_NeoPixel(94, 3, NEO_GRB + NEO_KHZ800);

// Yale Orange line 
Adafruit_NeoPixel orange_dayline= Adafruit_NeoPixel(100, 4, NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel *strips[3] = {
    &blue_dayline, &redline, &orange_dayline
//  &greenLineD, &greenLineB, &greenLineCE_blueLine, &orangeLine, &redLine
};



void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(115200);
  for(int i=0;i<3;i++) {
    strips[i]->begin();
    strips[i]->setPixelColor(0,0x000000);
    strips[i]->show();
  }
}

void loop() {
  if(millis() - last_data > 2000) {
    packet_index = 0;
  }
  while(Serial.available()) {
    byte b = Serial.read();
    last_data = millis();
    if(b == 0xFF && packet_index == 0) {
      // Special byte to tell lights to actually update
      /*greenLineD.show();
      greenLineB.show();
      greenLineCE_blueLine.show();
      orangeLine.show();
      redLine.show();*/
      blue_dayline.show();
      redline.show();
      orange_dayline.show();
    } else {
      // Just doing normal stuff
      packet[packet_index] = b;
      packet_index++;
      total_bytes++;
      if(packet_index == PACKET_SIZE) {
        handle_packet(packet);
        // I can't believe I ate the whole thing
        packet_index = 0;
      }
    }
  }
}

void handle_packet(byte *packet) {
  int index = packet[0];
  int16_t start = (int16_t) packet[1] << 8 | (int16_t) packet[2];
  int16_t end = (int16_t) packet[3] << 8 | (int16_t) packet[4];
  int32_t color = (int32_t) packet[5] << 16 | (int32_t) packet[6] << 8 | (int32_t) packet[7];
  for(int16_t j=start;j<=end;j++) {
    strips[index]->setPixelColor(j,color);
  }
}

