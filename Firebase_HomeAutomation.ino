#include <WiFi.h>
#include "time.h"
//2. Include Firebase ESP32 library (this library)
#include "FirebaseESP32.h"
#define FIREBASE_HOST "agricare-2020-7ca0c.firebaseio.com"                     //Your Firebase Project URL goes here without "http:" , "\" and "/"
#define FIREBASE_AUTH "Onm6L5x0nzUbRgCQJtOndegvFwsaVBfQILSBScrO"       //Your Firebase Database Secret goes here
#define WIFI_SSID "BB 218"                                               //your WiFi SSID for which yout NodeMCU connects
#define WIFI_PASSWORD "Vadtaldham"      
FirebaseData firebaseData;//Password of your wifi network 


const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 19800;
const int   daylightOffset_sec = 3600;

void setup() 
{
  pinMode(35,INPUT);
  pinMode(25,OUTPUT);
  digitalWrite(25,HIGH);
  Serial.begin(115200);
  pinMode(2,OUTPUT);
  WiFi.begin(WIFI_SSID,WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status()!=WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected:");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST,FIREBASE_AUTH);
   configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);

  
}
void firebasereconnect()
{
  Serial.println("Trying to reconnect");
    Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  }

void loop() 
{
   struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
   
  }
  //Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
  String year=String(timeinfo.tm_year+1900);
  String month=String(timeinfo.tm_mon+1);
  String month_day=String(timeinfo.tm_mday);
  Serial.print("year"+String(timeinfo.tm_year+1900));
  Serial.print("  Month:"+String(timeinfo.tm_mon+1));
  Serial.print("  Month day"+String(timeinfo.tm_mday));
//  Serial.print(String(timeinfo.tm_wday));
    String date=String(timeinfo.tm_mday)+"/"+String(timeinfo.tm_mon+1)+"/"+String(1900+timeinfo.tm_year);

   // Serial.print(date);
    String day;
    switch(timeinfo.tm_wday+1)
    {
        case 1: 
            day="Sunday";
            break;
        case 2: 
            day="Monday";
            break;
        case 3: 
            day="Tuesday";
            break;
        case 4: 
            day="Wednesday";
            break;
        case 5: 
            day="Thursday";
            break;
        case 6: 
            day="Friday";
            break;
        case 7: 
            day="Saturday";
            break;
        default:
            printf("%d : Invalid Day Option",day);
    }
    Serial.println(day);
  int val;
  Serial.println("l1:");
    //Serial.println(Firebase.getInt(firebaseData, "agricare-2020-7ca0c/l1"));
     if (Firebase.getInt(firebaseData, "l1")) {

    if (firebaseData.dataType() == "int") {
      Serial.println("Code");
      Serial.println(firebaseData.intData());
      val=firebaseData.intData();
    }

  } else {
    Serial.println(firebaseData.errorReason());
  }
     
 
  String   h=String(Firebase.getString(firebaseData,"agricare-2020-7ca0c/humidity"));
  Serial.print("Humidity Server:");
  Serial.println(h);
  delay(1000);
  Serial.println(val);   
  if(val==1)                                                             // If, the Status is 1, turn on the Relay1
     {
      digitalWrite(2,LOW);
      Serial.println("light 1 OFF");
    }
    if(val==0)                                                      // If, the Status is 0, turn Off the Relay1
    {                                      
      digitalWrite(2,HIGH);
      Serial.println("light 1 ON");
    }
    Serial.println("MOISTURE:");
   delay(5000);
    int val1=analogRead(35);
      Serial.println(val1);
    val1=map(val1,4095,0,0,100);
    Serial.println(val1);
    Firebase.setInt(firebaseData,"esp32-jemis/humidity/"+year+"/"+month+"/"+month_day,val1);
     Firebase.setInt(firebaseData,"esp32-jemis/humidity/current",val1);
    
   
}
    
