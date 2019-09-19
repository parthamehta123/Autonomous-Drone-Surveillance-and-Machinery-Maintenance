import processing.serial.*;
Serial myPort; 
Table dataTable; 
 
int numReadings = 500;
int readingCounter = 0; 
 
String fileName;
void setup()
{
  String portName = Serial.list()[1]; 
 
  
  myPort = new Serial(this, portName, 9600); 
   
  table.addColumn("Temperature");
  table.addColumn("Pressure");
  table.addColumn("Humidity");
  table.addColumn("X");
  table.addColumn("Y");
  table.addColumn("Z");
  
}
 
void serialEvent(Serial myPort){
  val = myPort.readStringUntil('\n'); //The newline separator separates each Arduino loop. We will parse the data by each newline separator. 
  if (val!= null) { //We have a reading! Record it.
    val = trim(val); //gets rid of any whitespace or Unicode nonbreakable space
    println(val); //Optional, useful for debugging. If you see this, you know data is being sent. Delete if  you like. 
    float sensorVals[] = float(split(val, ',')); //parses the packet from Arduino and places the valeus into the sensorVals array. I am assuming floats. Change the data type to match the datatype coming from Arduino. 
   
    TableRow newRow = dataTable.addRow(); //add a row for this new reading
    newRow.setInt("id", table.lastRowIndex());//record a unique identifier (the row's index)
    
    //record time stamp
    newRow.setInt("Temperature", sensorVals[0]);
    newRow.setInt("Pressure", sensorVals[1]);
    newRow.setInt("Humidity", sensorVals[2]);
    newRow.setInt("X", sensorVals[3]);
    newRow.setInt("Y", sensorVals[4]);
    newRow.setInt("Z", sensorVals[5]);
        
    readingCounter++;
    
    if (readingCounter % numReadings ==0)//The % is a modulus, a math operator that signifies remainder after division. The if statement checks if readingCounter is a multiple of numReadings (the remainder of readingCounter/numReadings is 0)
    {
      fileName = "pi_data" //this filename is of the form year+month+day+readingCounter
      saveTable(dataTable, fileName); //Woo! save it to your computer. It is ready for all your spreadsheet dreams. 
    }
   }
}
 
void draw()
{ 
  
}
