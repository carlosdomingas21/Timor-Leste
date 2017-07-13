import cv2
import numpy as np
import math
from cobainaja import tracking_red
from cobainaja import tracking_blue
from cobainaja import tracking_green
from cobainaja import tracking_yellow
from cobainaja import tracking_orange
from cobainaja import tracking_cyan
from cobainaja import tracking_lingkaran
from cobainaja import tracking_kotak
from cobainaja import tracking_segitiga
from cobainaja import angle


#dictionary of all contours
contours = {}
#array of edges of polygon
approx = []
#scale of the text
scale = 0.7
#camera

cap = cv2.VideoCapture(0)

print("kita masih coba RnEST")


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#Capture frame-by-frame

input1=input("masukan bentuk :")
input2=input("masukan warna :")
if(input1=="" or input2=="" or input1=="" and input2==""):
	print("bentuk atau warna tidak boleh kosong")
if (input1=="lingkaran" and input2=="merah"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_red(cap,out)

if (input1=="lingkaran" and input2=="biru"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_blue(cap,out)
		
if (input1=="lingkaran" and input2=="hijau"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_green(cap,out)

if (input1=="lingkaran" and input2=="kuning"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_yellow(cap,out)
		
if (input1=="lingkaran" and input2=="cyan"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_cyan(cap,out)
		
if (input1=="lingkaran" and input2=="jingga"): 
	while(cap.isOpened):
		tracking_lingkaran(cap,contours,out,scale)
		tracking_orange(cap,out)
		

if (input1=="kotak" and input2=="merah"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_red(cap,out)

if (input1=="kotak" and input2=="biru"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_blue(cap,out)
		
if (input1=="kotak" and input2=="hijau"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_green(cap,out)

if (input1=="kotak" and input2=="kuning"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_yellow(cap,out)
		
if (input1=="kotak" and input2=="cyan"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_cyan(cap,out)
		
if (input1=="kotak" and input2=="jingga"): 
	while(cap.isOpened):
		tracking_kotak(cap,contours,out,scale)
		tracking_orange(cap,out)


if (input1=="segitiga" and input2=="merah"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_red(cap,out)

if (input1=="segitiga" and input2=="biru"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_blue(cap,out)
		
if (input1=="segitiga" and input2=="hijau"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_green(cap,out)

if (input1=="segitiga" and input2=="kuning"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_yellow(cap,out)
		z
if (input1=="segitiga" and input2=="cyan"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_cyan(cap,out)
		
if (input1=="segitiga" and input2=="jingga"): 
	while(cap.isOpened):
		tracking_segitiga(cap,contours,out,scale)
		tracking_orange(cap,out)
