import numpy as np
import cv2
import math



def angle(pt1,pt2,pt0):
	dx1 = pt1[0][0] - pt0[0][0]
	dy1 = pt1[0][1] - pt0[0][1]
	dx2 = pt2[0][0] - pt0[0][0]
	dy2 = pt2[0][1] - pt0[0][1]
	return float((dx1*dx2 + dy1*dy2))/math.sqrt(float((dx1*dx1 + dy1*dy1))*(dx2*dx2 + dy2*dy2) + 1e-10)


def tracking_red(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

		red_lower=np.array([136,87,111],np.uint8)
		red_upper=np.array([180,255,255],np.uint8)
		red=cv2.inRange(hsv, red_lower, red_upper)
		kernal = np.ones((5 ,5), "uint8")
		red=cv2.dilate(red, kernal)
		res=cv2.bitwise_and(frame, frame, mask = red)
			       #Tracking the Red Color
		(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
				red = cv2.putText(frame,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
				print(x,y, "merah")

		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)

			


def tracking_blue(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

		blue_lower=np.array([99,115,150],np.uint8)
		blue_upper=np.array([110,255,255],np.uint8)
		blue=cv2.inRange(hsv,blue_lower,blue_upper)
		kernal = np.ones((5 ,5), "uint8")
		blue=cv2.dilate(blue,kernal)
		res1=cv2.bitwise_and(frame, frame, mask = blue)

		(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)	
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
				print(x,y,"biru")
		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)


def tracking_yellow(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

		yellow_lower=np.array([22,60,200],np.uint8)
		yellow_upper=np.array([60,255,255],np.uint8)
		yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
		kernal = np.ones((5 ,5), "uint8")
		yellow=cv2.dilate(yellow,kernal)
		res2=cv2.bitwise_and(frame, frame, mask = yellow)

		(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)	
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
				cv2.putText(frame,"yellow",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255))  
				print(x,y,"kuning")
		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)

def tracking_green(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		green_lower = np.array([50,50,50])
		green_upper = np.array([70,255,255])
		green=cv2.inRange(hsv,green_lower,green_upper)
		kernal = np.ones((5 ,5), "uint8")
		green=cv2.dilate(green,kernal)
		res2=cv2.bitwise_and(frame, frame, mask = green)

		(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)	
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
				cv2.putText(frame,"green",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
				print(x,y,"Hijau")
		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)

def tracking_cyan(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		cyan_lower = np.array([80,50,50])
		cyan_upper = np.array([100,255,255])
		cyan=cv2.inRange(hsv,cyan_lower,cyan_upper)
		kernal = np.ones((5 ,5), "uint8")
		cyan=cv2.dilate(cyan,kernal)
		res2=cv2.bitwise_and(frame, frame, mask = cyan)

		(_,contours,hierarchy)=cv2.findContours(cyan,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)	
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
				cv2.putText(frame,"cyan",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,0))
				print(x,y,"cyan")
		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)

def tracking_orange(cap,out):
	ret, frame = cap.read()
	if ret==True:
			        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			        #Canny
		canny = cv2.Canny(frame,80,240,3)
			        
			#converting frame(img i.e BGR) to HSV (hue-saturation-value)

		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		white_lower = np.array([5,50,50])
		white_upper = np.array([15,255,255])
		kernal = np.ones((5 ,5), "uint8")
		white=cv2.inRange(hsv,white_lower,white_upper)
		white=cv2.dilate(white,kernal)
		res2=cv2.bitwise_and(white, white, mask = white)        

		(_,contours,hierarchy)=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area>300):
				x,y,w,h = cv2.boundingRect(contour)	
				frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,125,255),2)
				cv2.putText(frame,"jingga",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0))        
				print(x,y,"jingga")
		out.write(frame)
		cv2.imshow('canny',canny)
		cv2.imshow('frame',frame)
		cv2.waitKey(1)	        



def tracking_segitiga(cap,contours,out,scale):
	ret, frame = cap.read()
		
	if ret==True:
		        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		        #Canny
		canny = cv2.Canny(frame,80,240,3)
		#converting frame(img i.e BGR) to HSV (hue-saturation-value)
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   	#contours
		canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for i in range(0,len(contours)):
	           #approximate the contour with accuracy proportional to
	           #the contour perimeter
			approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)

	            #Skip small or non-convex objects
			if(abs(cv2.contourArea(contours[i]))<100 or not(cv2.isContourConvex(approx))):
				continue

	            #triangle
			if(len(approx) == 3):
				x,y,w,h = cv2.boundingRect(contours[i])
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				cv2.putText(frame,'Segitiga',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,0,0),2,cv2.LINE_AA)
				print(x,y,"segitiga")
		out.write(frame)
		cv2.imshow('frame',frame)
		cv2.imshow('canny',canny)
		cv2.waitKey(1)


def tracking_kotak(cap,contours,out,scale):
	ret, frame = cap.read()
		
	if ret==True:
		        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		        #Canny
		canny = cv2.Canny(frame,80,240,3)
		#converting frame(img i.e BGR) to HSV (hue-saturation-value)
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		#contours
		canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for i in range(0,len(contours)):
            #approximate the contour with accuracy proportional to
            #the contour perimeter
			approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)

            #Skip small or non-convex objects
			if(abs(cv2.contourArea(contours[i]))<100 or not(cv2.isContourConvex(approx))):
				continue
			if(len(approx)>=4 and len(approx)<=6):
	                #nb vertices of a polygonal curve
				vtc = len(approx)
	                #get cos of all corners
				cos = []
				for j in range(2,vtc+1):
					cos.append(angle(approx[j%vtc],approx[j-2],approx[j-1]))
	                #sort ascending cos
				cos.sort()
	                #get lowest and highest
				mincos = cos[0]
				maxcos = cos[-1]

	                #Use the degrees obtained above and the number of vertices
	                #to determine the shape of the contour
				x,y,w,h = cv2.boundingRect(contours[i])
				if(vtc==4):
					cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
					cv2.putText(frame,'Kotak',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,0,0),2,cv2.LINE_AA)
					print(x,y,("kotak"))
				elif(vtc==5):
					cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
					cv2.putText(frame,'PENTA',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,0,0),2,cv2.LINE_AA)
					print(x,y,("penta"))
				elif(vtc==6):
					cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
					cv2.putText(frame,'HEXA',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,0,0),2,cv2.LINE_AA)
					print(x,y,("hexa"))
		out.write(frame)
		cv2.imshow('frame',frame)
		cv2.imshow('canny',canny)
		cv2.waitKey(1)

def tracking_lingkaran(cap,contours,out,scale):
	
	ret, frame = cap.read()
		
	if ret==True:
		        #grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		        #Canny
		canny = cv2.Canny(frame,80,240,3)
		#converting frame(img i.e BGR) to HSV (hue-saturation-value)
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

		canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		for i in range(0,len(contours)):
		            #approximate the contour with accuracy proportional to
		            #the contour perimeter
			approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)
		            #Skip small or non-convex objects
			if(abs(cv2.contourArea(contours[i]))<100 or not(cv2.isContourConvex(approx))):
					continue
		    	#detect and label circle
			area = cv2.contourArea(contours[i])
			x,y,w,h = cv2.boundingRect(contours[i])
			radius = w/2
			if(abs(1 - (float(w)/h))<=2 and abs(1-(area/(math.pi*radius*radius)))<=0.2):
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				cv2.putText(frame,'Lingkaran',(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
				print(x,y,"lingkaran")

	out.write(frame)
	cv2.imshow('frame',frame)
	cv2.imshow('canny',canny)
	cv2.waitKey(1)		
			
                    




