#!/usr/bin/env python
#!/usr/bin/python -tt
# coding: utf-8

# In[1]:



import os
import time
import pickle
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import pandas
import math
import numpy as np
import sys
from datetime import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from pandas.errors import EmptyDataError
#sys.exit()


# In[2]:

counter=1

flag2=1
def packets(command,password):
    #print("*")
    os.popen("sudo -S %s"%(command), 'w').write(password)
    time.sleep(2)
    return None


# In[3]:
def terminate():
    Button_start.configure(text="Stopped!")
    root.update_idletasks()
    global counter
    global flag2
    counter = 0
    if counter==0 and flag2==1:
	    root3=tk.Tk()
	    root3.title("Graph")
	    data1 = {'Parameters': ['Normal','Attack','Total'],'Data': [int(normal1),int(attack),int(total)]}		
	    d=DataFrame(data1,columns=['Parameters','Data'])
	    figure1 = plt.Figure(figsize=(6,9), dpi=70)
	    ax1 = figure1.add_subplot(111)
	    bar1 = FigureCanvasTkAgg(figure1, root3)
	    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	    d= d[['Parameters','Data']].groupby('Parameters').sum()
	    d.plot(kind='bar',  ax=ax1)	
	    print("Normal1=",normal1)
	    flag2=0


# In[4]:


def submit():
    #global stop
   
    count1=count=0
    #timer=k.get()
    loc=l.get()
    password=m.get()
    
    style=ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",background="white",foreground="black",fieldbackground="pink")
    style.map('Treeview',background=[('selected','blue')])
    root2 = tk.Tk()
    root2.geometry("1300x600") # set the root dimensions
    root2.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    root2.resizable(0, 0) # makes the root window fixed in size.
    root2.title("Real-Time Prediction")
    frame1 = tk.LabelFrame(root2, text="Prediction")
    frame1.place(height=600, width=1300)
    ## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
    #tv1.configure(treescrolly=treescrolly.set) 
    '''
      # The file/file path text
    label_file = ttk.Label( text="")
    label_file.place(rely=0, relx=0)
    
    # Frame for TreeView
    frame1 = tk.LabelFrame(root2, text="Prediction")
    frame1.place(height=600, width=1000)
    '''
     #'/home/shankhadeep/Documents/CICFlowMeter'      #input("Enter the location to get the CICFlowMeter Folder: ")
    loc=loc+'/CICFlowMeter'
    file_pcap=loc+'/store.pcap'
    file_csv=loc+'/store_ISCX.csv'
    if os.path.isfile(file_pcap):
        os.remove(file_pcap)
    if os.path.isfile(file_csv):
        os.remove(file_csv)
    command ='timeout 4'+' tcpdump -w '+file_pcap
    label5.configure(text="Capturing Packets...",bg="yellow",fg="blue")
    #Button_start.configure(text="Stop!",command=quit(),font=('calibre',12,'bold'))
    root.update_idletasks()
    #'/home/shankhadeep/Documents/store.pcap'
    #Button_start.destroy()
    #Button_start=tk.Button(root,text="Stop!",command=terminate,font=('calibre',12,'bold'))
    #Button_start.place(x=220,y=220)
    flag=0
    count=0
    global attack
    global total
    global normal
    global normal1
    global percent
    attack=0
    total=0
    normal=0
    percentage=0
    label6=tk.Label(root,text="Normal-: ",font=('calibre',12,'bold'),bg="yellow",fg='green')
    label6.place(x=110,y=285)
    label7=tk.Label(root,text="Attacks-: ",font=('calibre',12,'bold'),bg="yellow",fg='red')
    label7.place(x=110,y=315)
    label8=tk.Label(root,text="Total Captured-: ",font=('calibre',12,'bold'),bg="yellow")
    label8.place(x=110,y=345)
    label12=tk.Label(root,text="Attack Percentage-: ",font=('calibre',12,'bold'),bg="yellow",fg='purple')
    label12.place(x=110,y=375)
    label9=tk.Label(root,text=normal,font=('calibre',12,'bold'),bg="white")
    label9.place(x=200,y=285)
    label10=tk.Label(root,text=attack,font=('calibre',12,'bold'),bg="white")
    label10.place(x=200,y=315)
    label11=tk.Label(root,text=total,font=('calibre',12,'bold'),bg="white")
    label11.place(x=280,y=345)
    label13=tk.Label(root,text=percentage,font=('calibre',12,'bold'),bg="white")
    label13.place(x=290,y=375)
    #x=[]
    #ij=int(timer)
    while(counter):
        Button_start.configure(text="Stop!",command=terminate,font=('calibre',12,'bold'))
        root.update_idletasks()
        label9.configure(text=normal)
        label10.configure(text=attack)
        label13.configure(text=percentage)
        label11.configure(text=total)
        root.update()
        packets(command,password)
        print("****")
        command1=loc+'/./convert_pcap_csv.sh'
        os.popen("%s"%(command1), 'w').write(loc)
        time.sleep(4)
        
        try:
            my = pd.read_csv(file_csv,low_memory=False)
            my = my[~my['Flow ID'].isin(['Flow ID'])]
            my = my.reset_index(drop = True)
            #my=my.replace([np.inf, -np.inf], np.nan)
            pd.set_option('mode.use_inf_as_na', True)
            my.dropna(inplace=True)
            my=my.fillna(0)
            df=my
            #my[my<0]=0
            my=my.drop(['Flow ID', 'Src IP','Src Port','Dst IP','Protocol','Timestamp','Label'], axis = 1)
            #my=my.iloc[3:,:]
            my.columns = [ ' Destination Port', ' Flow Duration', ' Total Fwd Packets', ' Total Backward Packets','Total Length of Fwd Packets', ' Total Length of Bwd Packets', ' Fwd Packet Length Max', ' Fwd Packet Length Min', ' Fwd Packet Length Mean', ' Fwd Packet Length Std','Bwd Packet Length Max', ' Bwd Packet Length Min', ' Bwd Packet Length Mean', ' Bwd Packet Length Std','Flow Bytes/s', ' Flow Packets/s', ' Flow IAT Mean', ' Flow IAT Std', ' Flow IAT Max', ' Flow IAT Min','Fwd IAT Total', ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max', ' Fwd IAT Min','Bwd IAT Total', ' Bwd IAT Mean', ' Bwd IAT Std', ' Bwd IAT Max', ' Bwd IAT Min','Fwd PSH Flags', ' Bwd PSH Flags', ' Fwd URG Flags', ' Bwd URG Flags', ' Fwd Header Length', ' Bwd Header Length','Fwd Packets/s', ' Bwd Packets/s', ' Min Packet Length', ' Max Packet Length', ' Packet Length Mean', ' Packet Length Std', ' Packet Length Variance','FIN Flag Count', ' SYN Flag Count', ' RST Flag Count', ' PSH Flag Count', ' ACK Flag Count', ' URG Flag Count', ' CWE Flag Count', ' ECE Flag Count', ' Down/Up Ratio', ' Average Packet Size', ' Avg Fwd Segment Size', ' Avg Bwd Segment Size','Fwd Avg Bytes/Bulk', ' Fwd Avg Packets/Bulk', ' Fwd Avg Bulk Rate', ' Bwd Avg Bytes/Bulk', ' Bwd Avg Packets/Bulk','Bwd Avg Bulk Rate','Subflow Fwd Packets', ' Subflow Fwd Bytes', ' Subflow Bwd Packets', ' Subflow Bwd Bytes','Init_Win_bytes_forward', ' Init_Win_bytes_backward', ' act_data_pkt_fwd', ' min_seg_size_forward','Active Mean', ' Active Std', ' Active Max', ' Active Min','Idle Mean', ' Idle Std', ' Idle Max', ' Idle Min']
            #my = my[~my['Total Length of Fwd Packets'].isin(['Total Length of Fwd Packets'])]
            #my=my[my["Total Length of Fwd Packets"].str.contains("Total Length of Fwd Packets")==False]
            #Binary
            #my=[my<0]=0
            a=[]
            b=[' Fwd URG Flags', ' SYN Flag Count', ' Fwd Packet Length Min', ' Destination Port', ' Flow IAT Min', ' Down/Up Ratio','Bwd Packet Length Max', ' min_seg_size_forward', ' Active Min', ' Active Std','Init_Win_bytes_forward', ' RST Flag Count', ' Idle Max', ' Fwd Packet Length Max', ' Total Fwd Packets', ' Min Packet Length', ' Fwd Avg Bulk Rate', ' Packet Length Variance']
            for i in b:
                for j in my.columns:
                    if i==j:
                        a.append(i)
                        break

            #Multiclass
            d=[]           
            c=[' Total Fwd Packets', ' Fwd Packet Length Mean', ' Bwd Packet Length Mean', ' Flow Packets/s', ' Flow IAT Mean', ' Flow IAT Std', ' Bwd IAT Max','Fwd PSH Flags', ' Bwd PSH Flags', ' Fwd URG Flags', ' ACK Flag Count', ' ECE Flag Count', ' Bwd Avg Bytes/Bulk','Bwd Avg Bulk Rate','Init_Win_bytes_forward', ' Init_Win_bytes_backward', ' Idle Min']
            for i in c:
                for j in my.columns:
                    if i==j:
                        d.append(i)
                        break
            #print(d)
            #print(count1) 
            #For Binary
            b=[]
            for j in a:
                x= my[j].copy()
                b.append(x)
            #print(b)
            b=pd.DataFrame(b)
            #print(b)
            x= b.transpose()


            #For Multiclass
            c=[]
            for j in d:
                y= my[j].copy()
                c.append(y)
            #print(b)
            c=pd.DataFrame(c)
            #print(b)
            y= c.transpose()
            
    
            import warnings
            warnings.filterwarnings('ignore')
            try:
                #Binary_trained_pickle
                with open(loc+'/Pickle_file/DT_pickle','rb') as file1: ##Enter the 'binary pickle' file location
                    dt = pickle.load(file1)
                start_time = time.time()
                y1=dt.predict(x)
                '''
                #############################
                if flag==2 or flag==5:
                    y1[1]=1
                ############################
                '''
                print("--- %s Binary Test seconds ---" % (time.time() - start_time))
                #x['Binary_prediction']=y1
    	      
                #Multiclass_trained_pickle
                #y.replace([np.inf, -np.inf], np.nan ,inplace=True)
                #y.dropna(inplace=True)
                #y.fillna(0)
                with open(loc+'/Pickle_file/catboost_pickle','rb') as file2: ##Enter the 'binary pickle' file location
                    ct = pickle.load(file2)
                start_time = time.time()
                y2=ct.predict(y)
                print("--- %s Multiclass Test seconds ---" % (time.time() - start_time))
                '''
                ##########################
                if flag==2 or flag==5:
                    if flag==2:
                        y2[1]=6
                    else:
                        y2[0]=2
                        y2[1]=1
                #########################
                '''
                #y['Multiclass_prediction']=y2
                #y.to_csv(loc+'/csv/multi.csv')
                i=0
                #i=len(y1)
                print(i)
             
                df=df.iloc[:,:-1]
                df.insert(loc = 0,column = 'Binary',value = y1)
                df.insert(loc = 1,column = 'Multiclass',value = y2)
                #df.insert(loc = 2,column = 'TimeStamp',value = y3)
                #del(y3)
                columns_titles = ["Binary","Multiclass","Timestamp","Src IP","Src Port","Dst IP","Dst Port"]
                df=df.reindex(columns=columns_titles)
           
                if count==0:
                    tv1["column"] = list(df.columns)
                    tv1["show"] = "headings"
                    #.to_numpy()
                    for column in tv1["columns"]:
                        tv1.heading(column, text=column) # let the column heading = column name
                        tv1.column(column,width=40)


                df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
                tv1.tag_configure('attack',foreground="white",background="blue")
                tv1.tag_configure('goldeneye',foreground="white",background="purple")
                tv1.tag_configure('hulk',foreground="white",background="orange")
                tv1.tag_configure('httptest',foreground="white",background="red")
                tv1.tag_configure('slowloris',foreground="white",background="brown")  
                tv1.tag_configure('portscan',foreground="white",background="black")         
                tv1.tag_configure('normal',foreground="white",background="grey")
               
                #df_rows=df_rows.style.apply(highlight_sentiment, axis=1)
                for row in df_rows:
                    
                    if row[0] ==1.0 :
                    	#pass
                    	#attack+=1
                        tv1.insert("", 0, values=(row),tags=('attack'))
                        attack+=1
                    	
                    elif row[1] ==6.0:
                    	#attack+=1
                        tv1.insert("", 0, values=(row),tags=('goldeneye'))
                        attack+=1
                    elif row[1] ==5.0:
                    	#attack+=1
                        tv1.insert("", 0, values=(row),tags=('hulk'))
                        attack+=1
                    elif row[1] ==4.0:
                    	#attack+=1
                        tv1.insert("", 0, values=(row),tags=('httptest'))
                        attack+=1
                    elif row[1] ==3.0:
                    	#attack+=1
                        tv1.insert("", 0, values=(row),tags=('slowloris'))
                        attack+=1
                    
                    else:
                    	#normal+=1
                        tv1.insert("", 0, values=(row),tags=('normal'))
                        normal+=1
                        
                    	
                    
                    
                    
                    # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
                #tv1.tag_configure('attack',foreground="white",background="red")
                #tv1.configure(treescrolly=treescrolly.set) 
            #root2.update()
            #
                count=1
       
                os.remove(file_csv)
                os.remove(file_pcap)
                flag+=1
                count1+=1
            except ValueError:
               pass
        except FileNotFoundError:
            pass
        #ij=ij-1
        #print(ij)
        #count=0
        root2.update()
        normal1=normal
        print("Normal=",normal)
        print("Attack=",attack)
        print("Total=",total)
        total=normal+attack
        
        try:
               #percentage=(attack*100/total)
               #if count1==0:
               #  root3= tk.Tk() 	
               percent=(attack*100/total)
               percent=round(percent,2)
               percentage=(str(percent)+"%")
               print("Percent=",percentage)
        except ZeroDivisionError:
        	pass
        #attack=0
        #normal=0
 
        print(flag)
        Button_start.configure(text="Stop!",command=terminate,font=('calibre',12,'bold'))
        root.update_idletasks()
        root.update()
        

# In[5]:


root=tk.Tk()

root.title("PSO+TC")
root.geometry("500x500")
root.configure(background="Green")
root.pack_propagate(False) 
root.resizable(0, 0) 
#initialize
l=tk.StringVar()
m=tk.StringVar()

#Label & Entry
label1=tk.Label(root,text="Realtime-Prediction",font=('calibre',12,'bold'),bg="yellow",fg='red').place(x=160,y=50)
#label2=tk.Label(root,text="Input Time Limit (in seconds): ",font=('calibre',12,'bold'),bg="yellow").place(x=10,y=100)
#box2=tk.Entry(root,textvariable=k,font=('calibre',10,'normal')).place(x=320,y=100)
label3=tk.Label(root,text="Enter location of CICFlowMeter: ",font=('calibre',12,'bold'),bg="yellow").place(x=10,y=150)
box3=tk.Entry(root,textvariable=l,font=('calibre',10,'normal')).place(x=320,y=150)
label4=tk.Label(root,text="Enter password: ",font=('calibre',12,'bold'),bg="yellow").place(x=80,y=180)
box4=tk.Entry(root,textvariable=m,font=('calibre',10,'normal'),show="*").place(x=250,y=180)
label5=tk.Label(root,font=('calibre',12,'bold'),fg="green",bg="green")
label5.place(x=130,y=260)
#=tk.Label(root,text="",font=('calibre',12,'bold'),fg="green")
#t.place(x=330,y=260)

#Button
Button_start=tk.Button(root,text="Start!",command=submit,font=('calibre',12,'bold'))
Button_start.place(x=220,y=220)

root.mainloop()
root2.mainloop()
root3.mainloop()

# In[ ]:




