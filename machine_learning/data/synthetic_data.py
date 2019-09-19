import pandas as pd
import numpy as np
import random

def data_generation(temp,pressure,humidity,q,w,e,label,window,mode=''):
    
    temps=[];pressures=[];humiditys=[];q=[];w=[];e=[];labels=[]
    for a in range(4000):
        a = random_generation(temp,window[:2])
        temps.append(a)
        b = random_generation(pressure,window[2:4])
        pressures.append(b)
        c = random_generation(humidity,window[4:6])
        humiditys.append(c)
        labels.append(label)
        if (mode=="safe"):
            q.append(0)
            w.append(0)
            e.append(1)
        elif mode=="moderate":
            q.append(random.randint(0,1))
            w.append(random.randint(0,1))
            e.append(1)
        else:
            q.append(random.randint(0,1))
            w.append(random.randint(0,1))
            e.append(random.randint(0,1))
      
    df= pd.DataFrame(temps,columns=['Temperature'])  
    df['Pressure']= pressures
    df['Humidity']= humiditys
    df['X']=q
    df['Y']=w
    df['Z']=e
    df['label']=labels
    
    return df
    
def random_generation(list1,list2):
    arr1 = np.random.randint(list1[0],list1[1])
    arr2 = np.random.randint(list2[0],list2[1])
    out = np.stack((arr1,arr2))
    out = np.random.choice(out)  
    return out    

if __name__=="__main__":
   
    
    #safe
    temp =[30,40];pressure=[900,1100];humidity=[30,80];x=[];y=[];z=[];label=0;window=[20,30,800,900,80,90]
    safe = data_generation(temp,pressure,humidity,x,y,z,0,window,mode='safe')
              
    #moderate
    temp =[40,45];pressure=[700,900];humidity=[20,30];x=[];y=[];z=[];label=1;window=[45,47,500,700,10,20]
    moderate= data_generation(temp,pressure,humidity,x,y,z,1,window,mode='moderate')
 
    #danger 
    temp =[0,5];pressure=[100,500];humidity=[90,100];x=[];y=[];z=[];label=1;window=[45,55,1100,1200,0,10]
    danger= data_generation(temp,pressure,humidity,x,y,z,2,window,mode='danger')
    
    # join data
    final_data=safe.append(moderate)
    final_data=final_data.append(danger)
    print(len(final_data))

    final_data.to_csv('datasets.csv', sep=',')