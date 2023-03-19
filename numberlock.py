import cv2
import numpy as np
import HandTrackingModule as htm
cap=cv2.VideoCapture(0)
detector=htm.handDetector(detectionCon=0.8,maxHands=1)
a=''
b=''
lst=[]
out=[]
s=0
def check(out):
    ver_list=['1245','7896','7412','8965']
    if out in ver_list:
        print('Acess granted')
        cv2.putText(screen,'Acess Granted',(610,320),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
    else:
        cv2.putText(screen,'Acess Denied',(610,320),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
    if len(out)!=4:
        cv2.putText(screen,'Try Again',(610,320),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
   

while True:
    sucess,image=cap.read()
    image=cv2.flip(image,1)
    image=cv2.resize(image,(1280,720))
  
    rec=cv2.rectangle(image,(200,190),(1000,700),cv2.FILLED)
    rec1=cv2.rectangle(image,(300,600),(330,630),(0,0,0),cv2.FILLED)
    cv2.putText(rec1,'0',(305,625),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    equal=cv2.rectangle(image,(430,600),(590,630),(0,255,0),cv2.FILLED)
    cv2.putText(equal,'Enter',(445,620),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec3=cv2.rectangle(image,(300,550),(330,520),(0,0,0),cv2.FILLED)
    cv2.putText(rec3,'1',(305,540),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec4=cv2.rectangle(image,(360,550),(390,520),(0,0,0),cv2.FILLED)
    cv2.putText(rec4,'2',(365,540),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec5=cv2.rectangle(image,(430,550),(460,520),(0,0,0),cv2.FILLED)
    cv2.putText(rec5,'3',(435,540),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec6=cv2.rectangle(image,(300,500),(330,470),(0,0,0),cv2.FILLED)
    cv2.putText(rec6,'4',(305,490),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec7=cv2.rectangle(image,(360,500),(390,470),(0,0,0),cv2.FILLED)
    cv2.putText(rec7,'5',(365,495),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec8=cv2.rectangle(image,(430,500),(460,470),(0,0,0),cv2.FILLED)
    cv2.putText(rec8,'6',(435,490),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec9=cv2.rectangle(image,(300,450),(330,420),(0,0,0),cv2.FILLED)
    cv2.putText(rec9,'7',(305,445),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec10=cv2.rectangle(image,(360,450),(390,420),(0,0,0),cv2.FILLED)
    cv2.putText(rec10,'8',(365,445),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec11=cv2.rectangle(image,(430,450),(460,420),(0,0,0),cv2.FILLED)
    cv2.putText(rec11,'9',(435,445),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
    rec12=cv2.rectangle(image,(300,395),(330,365),(0,0,0),cv2.FILLED)
    cv2.putText(rec12,'C',(305,390),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

    result=cv2.rectangle(image,(305,340),(520,290),(0,0,0),cv2.FILLED)

    screen=cv2.rectangle(image,(605,340),(950,290),(0,0,0),cv2.FILLED)



    image=detector.findHands(image)
    
    lmList = detector.findPosition(image)
    # if len(lmList)!=0:
        
        
    # print(lmlist)

    if lmList:
         x1,y1=lmList[8][1:]
         x2,y2=lmList[12][1:]
         print(x1,y1)

    finger=detector.fingersUp()
    #print(finger)

 


    if finger[1]:
         if  y1<630:
            if 300<x1<330 and 600<y1<630:
                print('0 detected')
                if len(lst)!=0:
                  lst.append('0')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                  for i in range(0,n):
                
                     a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print('. detected')
                  

                else:
                    lst.append('0')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'0',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
         if 300<x1<330 and 520<y1<550:
               if len(lst)!=0:
                  lst.append('1')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

               else:
                    lst.append('1')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'1',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

         if 360<x1<390 and 520<y1<550:
                if len(lst)!=0:
                  lst.append('2')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                else:
                    lst.append('2')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'2',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

         if 430<x1<460 and 520<y1<550:
                if len(lst)!=0:
                  lst.append('3')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                else:
                    lst.append('3')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'3',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

            
         if 430<x1<590 and 600<y1<630:
               if len(lst)==4:
                  
                  a=""

                  for i in range(0,4):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:4]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print('. detected')
                  out=a[0:4]
                  print('output is',out)
                  check(out)
                  #break

            #    else:
            #         lst.append('=')
            #         n=len(set(lst))
            #         del lst[n:]

            #         cv2.putText(result,'=',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

            

           

         if 300<x1<330 and 470<y1<500:
                 if len(lst)!=0:
                  lst.append('4')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                 else:
                    lst.append('4')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'4',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)


         if 360<x1<390 and 470<y1<500:
                if len(lst)!=0:
                  lst.append('5')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                else:
                    lst.append('5')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'5',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)


         if 430<x1<460 and 470<y1<500:
                 if len(lst)!=0:
                  lst.append('6')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                 else:
                    lst.append('6')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'6',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

         

         if 300<x1<330 and 420<y1<450:
                 if len(lst)!=0:
                  lst.append('7')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

                 else:
                    lst.append('7')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'7',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)

         

         if 360<x1<390 and 420<y1<450:
               if len(lst)!=0:
                  lst.append('8')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

               else:
                    lst.append('8')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'8',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)


         if 430<x1<460 and 420<y1<450:
               if len(lst)!=0:
                  lst.append('9')
                  n=len(set(lst))
                  del lst[n:]
                  a=""
                

                  for i in range(0,n):
                
                    a=a+str(lst[i])
                  print(a)
                  cv2.putText(result,str(a[0:n]),(335,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                  print(' detected')

               else:
                    lst.append('9')
                    n=len(set(lst))
                    del lst[n:]

                    cv2.putText(result,'9',(315,330),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)




         if 300<x1<330 and 365<y1<395:
                del lst[0:]
                cv2.putText(result,'',(335,340),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                print(' detected') 
                

           
             
                



            



            

            

            


            



            

            

            

            


    cv2.imshow('calc',image)
    if cv2.waitKey(1) & 0xFF == 27:
        break