const int buttonPin = 2;     //Se reserva el numero de pin de entrada
const int buttonPin2 = 3;    //Se reserva el numero de pin de entrada
const int buttonPin3 = 4;    //Se reserva el numero de pin de entrada
const int buttonPin4 = 5;    //Se reserva el numero de pin de entrada
const int buttonPin5 = 6;     //Se reserva el numero de pin de entrada
const int buttonPin6 = 7;    //Se reserva el numero de pin de entrada
const int buttonPin7 = 8;    //Se reserva el numero de pin de entrada
const int buttonPin8 = 9;    //Se reserva el numero de pin de entrada
const int buttonPin9= 10;     //Se reserva el numero de pin de entrada
const int buttonPin10 = 11;    //Se reserva el numero de pin de entrada



int buttonState = 0;         //variable que almacena el valor del estado del pin de entrada buttonPin
int buttonState2 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin2
int buttonState3 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin3
int buttonState4 = 0; 
int buttonState5 = 0;         //variable que almacena el valor del estado del pin de entrada buttonPin
int buttonState6 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin2
int buttonState7 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin3
int buttonState8 = 0;
int buttonState9 = 0;         //variable que almacena el valor del estado del pin de entrada buttonPin
int buttonState10 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin2

int buttonStateFinal5 = 0;         //variable que almacena el valor del estado del pin de entrada buttonPin
int buttonStateFinal6 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin2
int buttonStateFinal7 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin3
int buttonStateFinal8 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin4
int buttonStateFinal9 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin3
int buttonStateFinal10 = 0;        //variable que almacena el valor del estado del pin de entrada buttonPin4


int leerDatos=0; //variable para indicar si se continua leyendo o no;
void setup(){
  //Serial.begin(115200); //Open the serial port
  Serial.begin(9600); //se abre el puerto serial
  //se inicializan los pines salida en caso de que se necesiten

  //se inicializan los pines de entrada y que seran los que se tienen que leer
  //para saber cual es estado de cada boton
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
  pinMode(buttonPin5, INPUT);
  pinMode(buttonPin6, INPUT);
  pinMode(buttonPin7, INPUT);
  pinMode(buttonPin8, INPUT);
  pinMode(buttonPin9, INPUT);
  pinMode(buttonPin10, INPUT);

  
}

void loop(){
    //leerDatos = Serial.read();
    //if(leerDatos=='1'){
      // se leen los estados de cada uno de los pines de entrada
      buttonState = digitalRead(buttonPin);
      buttonState2 = digitalRead(buttonPin2);
      buttonState3 = digitalRead(buttonPin3);
      buttonState4 = digitalRead(buttonPin4);
      buttonState5 = digitalRead(buttonPin5);
      buttonState6 = digitalRead(buttonPin6);
      buttonState7 = digitalRead(buttonPin7);
      buttonState8 = digitalRead(buttonPin8);
      buttonState9= digitalRead(buttonPin9);
      buttonState10 = digitalRead(buttonPin10);
      
      //sensorValue = analogRead(sensorPin);
      // verifica el valor leido de cada pin
      // si el valor es 1 los leds se encienden, en caso contrario
      // el led continua apagado
      if(buttonState != HIGH){
         Serial.println(1);
      }
    
      if(buttonState2 != HIGH){
          Serial.println(2);
       
      }
      if(buttonState3 != HIGH){
       Serial.println(3);
      }
      if(buttonState4 != HIGH){
        Serial.println(4);
      }
       if(buttonState5 != HIGH){
         Serial.println(5);
      }
    
      if(buttonState6 != HIGH){
          Serial.println(6);
       
      }
      if(buttonState7 != HIGH){
       Serial.println(7);
      }
      if(buttonState8 != HIGH){
        Serial.println(8);
      }
       if(buttonState9 != HIGH){
         Serial.println(9);
      }
    
      if(buttonState10 != HIGH){
          Serial.println(10);
       
      }
      
      //se imprimen los valores leidos a pantalla, este proceso es necesario
      //de aqui depende para que desde java se puedan leer dichos valores
      
      
      
      
      //Serial.println(sensorValue);
      //el programa se espera un tiempo de 100 milisegundos antes de volver
      //a realizar una lectura, no es tan necesario el retardo, para
      //para que java no se le haga pesado, es necesario un retardo
    //}
   // delay(1000); /detiene el programa por 100 milisegundos antes de volver a leer los puerto/

}
