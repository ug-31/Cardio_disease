
import pandas as pd




dataset=pd.read_csv("cardio_train.csv",sep=';')


correlation=dataset.corr()

y=dataset.iloc[:,12].values

dataset=dataset.drop(['id','gender','height','weight'],axis=1)

x=dataset.iloc[:,:].values

x[:,0]=x[:,0]/365     #CONVERTING DAYS TO YEARS
x=x[:,0:-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.10,random_state=0)





#TO PREDICT WHETHER THE PERSON HAS ANY CARDIOVASCULAR DISEASE



from sklearn.tree import DecisionTreeClassifier
classifier =DecisionTreeClassifier(max_depth=10,random_state=101,max_features=None,min_samples_leaf=15)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cmC=confusion_matrix(y_test,y_pred)

import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title('Cardiology Pridiction')

#Column 1 
Age=ttk.Label(win,text="Age (In Days)")
Age.grid(row=0,column=0,sticky=tk.W)
Age_var=tk.StringVar()
Age_entrybox=ttk.Entry(win,width=16,textvariable=Age_var)
Age_entrybox.grid(row=0,column=1)
#Column 2
Sbp=ttk.Label(win,text="Systolic Blood pressure(High) ")
Sbp.grid(row=1,column=0,sticky=tk.W)
Sbp_var=tk.StringVar()
Sbp_entrybox=ttk.Entry(win,width=16,textvariable=Sbp_var)
Sbp_entrybox.grid(row=1,column=1)
#Column 3
Dbp=ttk.Label(win,text="Diastolic Blood Pressure(Low)")
Dbp.grid(row=2,column=0,sticky=tk.W)
Dbp_var=tk.StringVar()
Dbp_entrybox=ttk.Entry(win,width=16,textvariable=Dbp_var)
Dbp_entrybox.grid(row=2,column=1)
#Column 4
Cholesterol=ttk.Label(win,text="Cholesterol(1:Bad,2:normal,3:Good)")
Cholesterol.grid(row=3,column=0,sticky=tk.W)
Cholesterol_var=tk.StringVar()
Cholesterol_entrybox=ttk.Entry(win,width=16,textvariable=Cholesterol_var)
Cholesterol_entrybox.grid(row=3,column=1)
#Column 5
Glucose=ttk.Label(win,text="Glucose(1:Bad,2: normal,3:Good)")
Glucose.grid(row=4,column=0,sticky=tk.W)
Glucose_var=tk.StringVar()
Glucose_entrybox=ttk.Entry(win,width=16,textvariable=Glucose_var)
Glucose_entrybox.grid(row=4,column=1)
#Column 6
Smoking=ttk.Label(win,text="Smoking 1 for yes else 0")
Smoking.grid(row=5,column=0,sticky=tk.W)
Smoking_var=tk.StringVar()
Smoking_entrybox=ttk.Entry(win,width=16,textvariable=Smoking_var)
Smoking_entrybox.grid(row=5,column=1)
#Column 7
Alcohol=ttk.Label(win,text="Alcohol 1 for yes else 0")
Alcohol.grid(row=6,column=0,sticky=tk.W)
Alcohol_var=tk.StringVar()
Alcohol_entrybox=ttk.Entry(win,width=16,textvariable=Alcohol_var)
Alcohol_entrybox.grid(row=6,column=1)
#Column 8
Physical=ttk.Label(win,text="Physical Activity 1 for yes else 0")
Physical.grid(row=7,column=0,sticky=tk.W)
Physical_var=tk.StringVar()
Physical_entrybox=ttk.Entry(win,width=16,textvariable=Physical_var)
Physical_entrybox.grid(row=7,column=1)


##############################################################
result = ''
empty=''

import pandas as pd
DF = pd.DataFrame()
def action():
    global DB
    import pandas as pd
    DF = pd.DataFrame(columns=['Age','Sbp','Dbp','Cholesterol','Glucose','Smoking','Alcohol','Physical'])
    AGE=Age_var.get()
    DF.loc[0,'Age']=AGE
    SBP=Sbp_var.get()
    DF.loc[0,'Sbp']=SBP
    DBP=Dbp_var.get()
    DF.loc[0,'Dbp']=DBP
    CHOL=Cholesterol_var.get()
    DF.loc[0,'Cholesterol']=CHOL
    GLU=Glucose_var.get()
    DF.loc[0,'Glucose']=GLU
    SMOK=Smoking_var.get()
    DF.loc[0,'Smoking']=SMOK
    ALC=Alcohol_var.get()
    DF.loc[0,'Alcohol']=ALC
    PHY=Physical_var.get()
    DF.loc[0,'Physical']=PHY

    DB=DF
    DB["Age"] = pd.to_numeric(DB["Age"])
    DB["Sbp"] = pd.to_numeric(DB["Sbp"]) 
    DB["Dbp"] = pd.to_numeric(DB["Dbp"])
    DB["Cholesterol"] = pd.to_numeric(DB["Cholesterol"])
    DB["Glucose"] = pd.to_numeric(DB["Glucose"])
    DB["Smoking"] = pd.to_numeric(DB["Smoking"])
    DB["Alcohol"] = pd.to_numeric(DB["Alcohol"])
    DB["Physical"] = pd.to_numeric(DB["Physical"])


    output=classifier.predict(DB)
    print(output[0])
    if output[0]==1:
            result='Patient Might Have some cardiovascular Disease :('
    elif output[0]==0:
            result='Patient is Alright :)'
    Predict_entrybox.insert(1,str(empty))        
    Predict_entrybox.insert(1,str(result))

###################################################################

Predict_entrybox=ttk.Entry(win,width=60)
Predict_entrybox.grid(row=21,column=1)
Predict_entrybox.insert(1,str(result))



Predict_button=ttk.Button(win,text="Predict",command=action)
Predict_button.grid(row=21,column=0)
win.geometry("800x600")
win.mainloop()











    

