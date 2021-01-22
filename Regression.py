
import numpy as np
import math
import PySimpleGUI as sg

sg.theme('DarkBlue17')  # Add a touch of color
# All the stuff inside your window.
radio_choices2=['a','b','c','d','e','f','g','h']
radio_choices = ['y=1/(a+bX)', 'y=aX/(1+bX)', 'y=1/(a+bX^2)','y=X/b+cX','y=exp(a+b/x)','y= C*exp((x-a)^2/b) ',' y=a*exp(-b(x^2))','y=a+bx (simple form)','y=a+bx+cx^2 (MultiLinear)']
layout = [ [sg.Text('''                    Regression Calculator                '''
                    , font=("Helvetica", 25))], [sg.Text('''\nChoose one of the formats to calculate correlation factor:   ''',text_color='burlywood3'
                    , font=("Helvetica", 15))],[sg.Radio(text, 1,key=i) for text,i in zip( radio_choices[:4],radio_choices2[:4])],[sg.Radio(text, 1,key=i) for text,i in zip(radio_choices[4:7],radio_choices2[4:7])],[sg.Radio(text, 1,key=i) for text,i in zip(radio_choices[7:9],radio_choices2[7:9])],
        
         
            [sg.Text('Enter Values of  X          ',text_color='burlywood3',font=("Helvetica")), sg.InputText()],
            [sg.Text('Enter values of  Y           ',text_color='burlywood3',font=("Helvetica")), sg.InputText()],[sg.Output(size=(100,20),key='Op')],
            [sg.Button('Solve'),sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Regression Calculator', layout)



# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
   
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
   
    X=[]
    X2=[]
    Y=[]
    X_sqr=[]
    X_sqr_inv=[]
    Y_sqr_inv=[]
    n=0
    if(values['a']==True):
        choice='a'
    elif(values['b']==True):
        choice='b'
    elif(values['c']==True):
        choice='c'
    elif(values['d']==True):
        choice='d'
    elif(values['e']==True):
        choice='e'
    elif(values['f']==True):
        choice='f'
    elif(values['g']==True):
        choice='g'
    elif(values['h']==True):
        choice='h'
    elif(values['i']==True):
        choice='i'
    else:
        sg.Popup("choose method!")
    ##choice=input("Choose one of the formats to calculate correlation factor: \n \n a)y=1/(a+bX)  b)y=aX/(1+bX) c)y=1/(a+bX^2) d)y=X/b+cX \n \n e) y= exp(a+b/x) f)y= C*exp((x-a)^2/b)  g)y=a*exp(-b(x^2)) \n \n h)y=a+bx (simple form)  i)y=a+bx+cx^2 (MultiLinear) \n \n")
    if choice=='a'or choice=='h':
        y_inv=[]
    
        for inp in values[0].split():
            X.append(float(inp))
            X_sqr.append((float(inp))**2)
            n+=1
   
   
        for inp in values[1].split():   
            Y.append(float(inp))
            y_inv.append(1/float(inp))
            
        sum_x=sum(X)
        sum_y=sum(Y)
        sum_y_inv=sum(y_inv)
        if choice=='a':
            y_inv_avg=sum_y_inv/n
            XY = [a * b for a, b in zip(X, y_inv)]
        else:
            y_inv_avg=sum_y/n
            XY = [a * b for a, b in zip(X,Y)]
        sum_XY=sum(XY)
        sum_X_sqr=sum(X_sqr)
        a = np.array([ [n,sum_x], [sum_x,sum_X_sqr] ])
        if choice=='a':
            b = np.array([sum_y_inv,sum_XY])
            z = np.linalg.solve(a,b)
            St=sum([(a- y_inv_avg)**2for a in y_inv])
            Sr=sum([(a-(z[0]+z[1]*b))**2for a,b in zip(y_inv,X)])
            print("The Best Fit Is : \n                                1 \n  Y = _____________________________________________ \n        ",z[0],"+ ",z[1],"X",'\n')
            ##sg.ScrolledTextBox("The Best Fit Is : \n                 1 \n  Y =  __________________________________________________ \n   ",z[0],"+ ",z[1],"X\n")
        else:
            b = np.array([sum_y,sum_XY])
            z = np.linalg.solve(a,b)
            St=sum([(a- y_inv_avg)**2for a in Y])
            Sr=sum([(a-(z[0]+z[1]*b))**2for a,b in zip(Y,X)])
            print("The Best Fit Is : Y = ",z[0]," +",z[1],"X \n")
        r=((St-Sr)/St)**0.5
        print("Rgeression Error : Sr = ",Sr,'\n \n')
        print("True Error  : St = ",St,'\n \n')
        print("correlation coeff : r= ",r,'\n \n')
        print("r %= ",r*100," %",'\n',"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
            ################################################################################

    elif choice=='b'or choice=='d' or choice=='e':

        y_inv=[]
        x_inv=[]
        y_ln=[]
   
    
        for inp in values[0].split():
            x_inv.append(1/float(inp))
            X_sqr_inv.append((1/(float(inp)))**2)
        
            n+=1
        for inp in values[1].split():    
            Y.append(float(inp))
            y_inv.append(1/float(inp))
            y_ln.append(math.log(float(inp)))
            Y_sqr_inv.append((1/(float(inp)))**2)
        
        sum_x=sum(x_inv)
        sum_y=sum(Y)
        sum_y_inv=sum(y_inv)
        sum_y_ln=sum(y_ln)
        if(choice!='e'):
            y_inv_avg=sum_y_inv/n
            XY = [a * b for a, b in zip(x_inv, y_inv)]
        else:
            y_inv_avg=sum_y_ln/n
            XY = [a * b for a, b in zip(x_inv, y_ln)]
        sum_XY=sum(XY)
        sum_X_sqr_inv=sum(X_sqr_inv)
        sum_Y_sqr_inv=sum(Y_sqr_inv)
        a = np.array([ [n,sum_x], [sum_x,sum_X_sqr_inv] ])
        if(choice!='e'):
            b = np.array([sum_y_inv,sum_XY])
        else:
            b = np.array([sum_y_ln,sum_XY])
        z = np.linalg.solve(a,b)
        if(choice=='b'):
            a=1/z[1]
            b=a*z[0]
            St=sum([(a- y_inv_avg)**2for a in y_inv])
            Sr=sum([(c-(z[0]+z[1]*d))**2for c,d in zip(y_inv,x_inv)])
        elif(choice=='d'):
            b=z[0]
            a=z[1]
            St=sum([(a- y_inv_avg)**2for a in y_inv])
            Sr=sum([(c-(z[0]+z[1]*d))**2for c,d in zip(y_inv,x_inv)])
        else:
            a=z[0]
            b=z[1]
            St=sum([(a- y_inv_avg)**2for a in y_ln])
            Sr=sum([(c-(z[0]+z[1]*d))**2for c,d in zip(y_ln,x_inv)])
   
    
        r_sqr=((St-Sr)/St)
        if(r_sqr<0):
            r=-(abs(r_sqr)**0.5)
        else:
            r=(abs(r_sqr)**0.5)
        if(choice=='b'):
            print("The Best Fit is : \n           ",a,"X \n Y=   __________________________________ \n         (1+",b,"X) \n")
        elif(choice=='d'):
            print("The Best Fit is : \n                               X \n Y=     ____________________________________________ \n                (",a,"+",b,"X)")
        else:
            print("The Best Fit is : Y= e^(",a,"+ ","(",b,"/X))")
        print("Rgeression Error : Sr = ",Sr,'\n \n')
        print("True Error  : St = ",St,'\n \n')
        print("correlation coeff : r= ",r,'\n \n')
        print("r %= ",r*100," %",'\n',"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
        ############################################################################################
    elif choice=='c'or choice=='g':
        y_inv=[]
        y_ln=[]
   
    
        for inp in values[0].split():
            X.append(float(inp)**2)
            X_sqr.append((float(inp))**4)
        
            n+=1
        for inp in values[1].split():  
            Y.append(float(inp))
            y_inv.append(1/float(inp))
            y_ln.append(math.log(float(inp)))
        
        sum_x=sum(X)
        sum_y=sum(Y)
        sum_y_inv=sum(y_inv)
        sum_y_ln=sum(y_ln)
        if(choice!='g'):
            y_inv_avg=sum_y_inv/n
            XY = [a * b for a, b in zip(X, y_inv)]
        else:
            y_inv_avg=sum_y_ln/n
            XY = [a * b for a, b in zip(X, y_ln)]
    
        sum_XY=sum(XY)
        sum_X_sqr=sum(X_sqr)

        a = np.array([ [n,sum_x], [sum_x,sum_X_sqr] ])
        if(choice!='g'):
            b = np.array([sum_y_inv,sum_XY])
            z = np.linalg.solve(a,b)
            St=sum([(a- y_inv_avg)**2for a in y_inv])
            Sr=sum([(a-(z[0]+z[1]*b))**2for a,b in zip(y_inv,X)])
        else:
            b = np.array([sum_y_ln,sum_XY])
            z = np.linalg.solve(a,b)
            St=sum([(a- y_inv_avg)**2for a in y_ln])
            Sr=sum([(a-(z[0]+z[1]*b))**2for a,b in zip(y_ln,X)])
    
    
        r=((St-Sr)/St)**0.5
        if(choice!='g'):
            print("The Best Fit Is : \n                              1 \n  Y =  ___________________________________________\n        ",z[0],"+ ",z[1],"X^2",'\n')
        else:
            print("The Best Fit is : Y= ",math.exp(z[0]),"e^(",z[1],"X^2)")
        print("Rgeression Error : Sr = ",Sr,'\n \n')
        print("True Error  : St = ",St,'\n \n')
        print("correlation coeff : r= ",r,'\n \n')
        print("r %= ",r*100," %",'\n',"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
        #############################################################################################
    elif(choice=='i' or choice=='f'):
        y_ln=[]

        for inp in values[0].split():
            X.append(float(inp))
            X_sqr.append((float(inp))**2)
            n+=1
        for inp in values[1].split():
            Y.append(float(inp))
            y_ln.append(math.log(float(inp)))
        
        sum_x=sum(X)
        sum_X_sqr=sum(X_sqr)
        sum_X_sqr_sqr=(sum([a**2 for a in X_sqr ]))
        sum_X_cub=(sum([a**3 for a in X ]))
        if(choice=='i'):
            sum_y=sum(Y)
            sum_y_x=sum([a*b for a,b in zip(X , Y)])
            sum_y_x_sqr=sum([a*b for a,b in zip(X_sqr , Y)])
        else:
            sum_y=sum(y_ln)
            sum_y_x=sum([a*b for a,b in zip(X , y_ln)])
            sum_y_x_sqr=sum([a*b for a,b in zip(X_sqr , y_ln)])
        y_avg=sum_y/n
    
        a = np.array([ [n,sum_x,sum_X_sqr], [sum_x,sum_X_sqr,sum_X_cub ],[sum_X_sqr,sum_X_cub,sum_X_sqr_sqr]])
        b = np.array([sum_y,sum_y_x,sum_y_x_sqr])
        z = np.linalg.solve(a,b)
        s1=1/z[2]
        s0=z[1]*s1/-2
        s2=math.exp(z[0]-(s0**2/s1))
        if(choice=='i'):
            print("The Best Fit Is : Y = ",z[0]," +",z[1],"X +",z[2],"X^2")
            St=sum([(a- y_avg)**2for a in Y])
            Sr=sum([(a-(z[0]+z[1]*b+z[2]*c))**2 for a,b ,c in zip(Y,X,X_sqr)])
        
        else:
            print("The Best Fit is : Y= ",s2,"e^((X-",s0,")^2)/",s1,")")
            St=sum([(a- y_avg)**2for a in y_ln])
            Sr=sum([(a-(z[0]+z[1]*b+z[2]*c))**2 for a,b ,c in zip(y_ln,X,X_sqr)])
    
        r=((St-Sr)/St)**0.5
        print("Rgeression Error : Sr = ",Sr,'\n \n')
        print("True Error  : St = ",St,'\n \n')
        print("correlation coeff : r= ",r,'\n \n')
        print("r %= ",r*100," %",'\n',"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    else:
        sg.Popup("invalid  input")
