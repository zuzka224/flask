#-----------overenie ci subor existuje-------------

import os.path
#subor = input("Zadaj názov súboru: ")

#if os.path.isfile(subor):
 # print("súbor existuje")
#else:
 # print("súbor neexituje")


#-------------GRAYSCALE---------------
import colorsys

def GRAYSCALE(im):
  for x in range(im.width):
    for y in range(im.height):
      rgb = im.getpixel((x,y))
      hls = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
      bw = colorsys.hls_to_rgb(hls[0], hls[1], 0)
      im.putpixel((x,y), (int(bw[0]*255) ,int(bw[1]*255), int(bw[2]*255)))
  return im


#--------------vytvorenie obrazku -----------------


from PIL import Image

def create_image(width, height): 
  
  a = width
  b = height
  return a, b



#---------prevod cisla, farba ------------

def cifra_dec(n):
  if n < 'A':  
    return int(n)
  else:
    return ord(n) - ord('A') + 10   

def to_dec(cislo):
 vysledok = 0
 u = 0
 for i in cislo[::-1]:
  vysledok += cifra_dec(i)*16**u
  u += 1
 return vysledok

def prevod_farba(farba):
  a = to_dec(farba[1:3])
  b = to_dec(farba[3:5])
  c = to_dec(farba[5:7])
  farba = (int(a), int(b), int(c))
  return farba

def clear(im, farba):

 
  for x in range(0, im.width):
    for y in range(0, im.height):
      im.putpixel((x,y), farba)

#-------------fill_rect-------------

def fill_rect(im, x, y, width_2, height_2, color):
  
  for x1 in range(x, (x + width_2)):
    for y1 in range(y, (y + height_2)):
      if 0 <= x1 <im.width and 0 <= y1 < im.height>=0:
       im.putpixel((x1,y1), color)

#-------------triangle, lines-------------------

def linePixels(A, B):
  
  pixels = []
  if A[0] == B[0]:
    if A[1] > B[1]:
      A,B = B,A
    for y in range(A[1], B[1] + 1):
      pixels.append((A[0], y))
  elif A[1] == B[1]:
    if A[0] > B[0]:
      A,B=B,A
    for x in range(A[0], B[0] + 1):
      pixels.append((x, A[1]))
  else:
    if A[0] > B[0]:
      A,B=B,A 
    dx = B[0] - A[0] 
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1],B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0])+ 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        pixels.append((x,y))
  return pixels


def line(im, A, B, color):
  
  pixels = linePixels(A, B)
  for suradnice in pixels:
    if 0<= suradnice[0] < im.width >=0 and 0 <= suradnice[1] < im.height >=0:
      im.putpixel(suradnice, color)



def getY(point):
  return point[1]


def fill_triangle(im, ax, ay, bx,  by, cx, cy, color):
  A, B, C = [ax, ay], [bx, by], [cx, cy]
  V = sorted([A, B, C], key=getY)
  left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
  right = linePixels(V[0], V[2])

  Xmax = max(A[0], B[0], C[0])
  Xmin = min(A[0], B[0], C[0])

  if V[1][0] == Xmax:
    left, right = right, left

  for y in range(getY(V[0]), getY(V[2]) + 1):
    x1 = Xmax
    for X in left:
      if X[1] == y and X[0] < x1:
        x1 = X[0]
    
    x2 = Xmin
    for X in right:
      if X[1] == y and X[0] > x2:
        x2 = X[0]

    if x2 < 0:
      continue
    if x2 > im.width:
      x2 = im.width - 1
    if x1 < 0:
      x1 = 0


    line(im, (x1, y), (x2, y), color)
 
def thick_line(im, A, B, thickness, color):
  pixels = linePixels(A, B)
  for suradnice in pixels:
    if 0 <= suradnice[0] < im.width and 0 <= suradnice[1] < im.height:
     fill_circle(im, suradnice[0], suradnice[1] , thickness/2, color)
    else:
      continue


def triangle(im,ax, ay,bx, by, cx, cy, thickness, color):

  thick_line(im, (ax, ay), (bx, by), thickness, color)
  thick_line(im, (bx, by), (cx, cy), thickness, color)
  thick_line(im, (cx, cy), (ax, ay), thickness, color)
#--------------fill_circle----------------


def fill_circle(im, x, y, r, color):
  S = [x, y]
  for x in range(0, int(r/2**(1/2)) + 1):
    y = int((r**2 - x**2)**(1/2))


    line(im, (x + S[0], y + S[1]), (x + S[0], -y + S[1]),  color)
    line(im, (y + S[0], x + S[1]), (y + S[0], -x + S[1]),  color)
    line(im, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]),  color)
    line(im, (-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), color)



#-------------------circle-----------------

def circle(im, x, y, r,thickness, color):
  S = [x, y]
  for x in range(0, int(r/2**(1/2)) + 1):
    y = int((r**2 - x**2)**(1/2))
    
    fill_circle(im,(x + S[0]), (y + S[1]), thickness/2,  color)
    fill_circle(im,(y + S[0]), (x + S[1]), thickness/2, color)
    fill_circle(im, (y + S[0]),( -x + S[1]), thickness/2, color)
    fill_circle(im, (x + S[0]), (-y + S[1]), thickness/2, color)
    fill_circle(im, (-x + S[0]), (-y + S[1]), thickness/2, color)
    fill_circle(im, (-y + S[0]), (-x + S[1]), thickness/2, color)
    fill_circle(im, (-y + S[0]), (x + S[1]), thickness/2, color)
    fill_circle(im, (-x + S[0]), (y + S[1]),thickness/2, color)


#--------------rectangle-----------------------
def rect(im,ax, ay, width, height, thickness, color):
  thick_line(im, (ax, ay), (ax+width, ay), thickness, color)
  thick_line(im,  (ax+width, ay), (ax+width, ay+height), thickness, color)
  thick_line(im, (ax+width, ay+height), (ax, ay+height), thickness, color)
  thick_line(im,  (ax, ay+height), (ax, ay), thickness, color)

#---------------unknown function--------------
def unknown_function():
  global cislo_riadku, pozicia
  print(f"Syntax error on line {cislo_riadku}: Unknown comman {pozicia[0]}.")



#------------prepocitanie suradnic-------------------
def convert_x(width, output_width, x):
  return int(x/width * output_width)

def convert_y(height, output_height, y):
  return int(y/height * output_height)

def convert_point(width, height, output_width, output_height, X):
  return (convert_x(width, output_width, X[0]), convert_y(height, output_height, X[1]))




#------------citanie suboru----------------

 
def citanie_suboru(subor, im):
  
  
  with open(str(subor), "r") as f:
    prikazy = ["CLEAR", "CIRCLE", "FILL_CIRCLE", "TRIANGLE", "LINE", "FILL_TRIANGLE", "RECT", "FILL_RECT"]




    cislo_riadku = 0
    for riadok in f:
      cislo_riadku += 1
      riadok = riadok.strip()
      pozicia= riadok.split(" ")
      
      try:
        if pozicia[0] != "VES" and pozicia[0]  in prikazy:
          farba  = prevod_farba(pozicia[-1])
          for i in range(1, len(pozicia)-1):
           pozicia[i]= round(float(pozicia[i]), 0)

          

        if pozicia[0] == "VES":

          #-------------------------------konvertovanie-----------------------------
          width= int(pozicia[2])
          height = int(pozicia[3])
          zmena = input(f"Chceš zmeniť veľkosť obrázka? aktuálna veľkosť je {pozicia[2]}:{pozicia[3]}. ZADAJ A/N ").upper()

          if zmena == "A":
            rozmery = input(f"Zadaj požadovanú veľkosť vo fomáte X:Y, zachovaj pomer {pozicia[2]}:{pozicia[3]}! ")
            output_width, output_height = rozmery.split(":")
            output_width = int(output_width)
            output_height = int(output_height)
          elif zmena == "N":
            output_width= int(pozicia[2])
            output_height = int(pozicia[3])
            
            
          else:
            output_width= int(pozicia[2])
            output_height = int(pozicia[3])
    
          
          if zmena == "N": 
           im = Image.new("RGB", (width, height), (255, 255, 255)) 
          elif zmena == "A":
           im = Image.new("RGB", (output_width, output_height),  (255, 255, 255)) 
          else:
           im = Image.new("RGB", (width, height), (255, 255, 255)) 
          


        elif pozicia[0] == "CLEAR":
         clear(im, farba)

        elif pozicia[0] == "FILL_CIRCLE":
          fill_circle(im, convert_x(width, output_width,int(pozicia[1])), convert_y(height, output_height, int(pozicia[2])), int(pozicia[3])*output_width/width,  farba)

        elif pozicia[0] == "FILL_RECT":
          fill_rect(im, convert_x(width, output_width,int(pozicia[1])),  convert_y(height, output_height, int(pozicia[2])), int(int(pozicia[3])*output_width/width), int(int(pozicia[4])*output_width/width), farba)

        elif pozicia[0]== "FILL_TRIANGLE":
          fill_triangle(im, convert_x(width, output_width,int(pozicia[1])),  convert_y(height, output_height, int(pozicia[2])), convert_x(width, output_width,int(pozicia[3])),  convert_y(height, output_height, int(pozicia[4])), convert_x(width, output_width,int(pozicia[5])),  convert_y(height, output_height, int(pozicia[6])), farba)

        elif pozicia[0] == "CIRCLE":
          circle(im, convert_x(width, output_width,int(pozicia[1])), convert_y(height, output_height, int(pozicia[2])),int(pozicia[3])*output_width/width, int(pozicia[4])*output_width/width , farba)

        elif pozicia[0]== "TRIANGLE":
          triangle(im, convert_x(width, output_width,int(pozicia[1])),  convert_y(height, output_height, int(pozicia[2])), convert_x(width, output_width,int(pozicia[3])),  convert_y(height, output_height, int(pozicia[4])), convert_x(width, output_width,int(pozicia[5])),  convert_y(height, output_height, int(pozicia[6])), int(pozicia[7])*output_width/width, farba)

        elif pozicia[0] == "RECT":
          rect(im, convert_x(width, output_width,int(pozicia[1])),  convert_y(height, output_height, int(pozicia[2])), int(int(pozicia[3])*output_width/width), int(int(pozicia[4])*output_width/width),  int(pozicia[5])*output_width/width, farba)

        elif pozicia[0] == "LINE":
          thick_line(im, (convert_x(width, output_width,int(pozicia[1])),  convert_y(height, output_height, int(pozicia[2]))), (convert_x(width, output_width,int(pozicia[3])),  convert_y(height, output_height, int(pozicia[4]))), int(pozicia[5])*output_width/width, farba)
        
        elif riadok == "":
          continue


        else:
          unknown_function()
      except (ValueError, IndexError):
        print("ValueError or IndexError on line:", cislo_riadku)

  return im



