"""Routes for logged-in application."""
from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
#from .assets import compile_auth_assets
from flask_login import login_required
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
import pandas as pd
import io
import csv
from flask import json
from flask import Response
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
from keras.models import load_model

#from sklearn.metrics import mean_absolute_error
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure
import random
#from matplotlib import pyplot as plt
import io
#import seaborn as sns
from flask import Flask, render_template, request
from werkzeug import secure_filename
from flask import send_from_directory
import os
from flask import make_response
from functools import wraps, update_wrapper
import datetime
from datetime import timedelta
"""Routes for user authentication."""
from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash
#from .assets import compile_auth_assets
from .forms import LoginForm, SignupForm
from .models import db, User,Score 
from .import login_manager



# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
#compile_auth_assets(app)




@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""
    return render_template('csv.html',
                           title='Flask-Login Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")



def features(segment_1):
    for i in range(len(segment_1)):
        for j in range(len(segment_1[i])):
            x = segment_1[i][j]
            segment_1[i][j]=x
        segment_1[i]=segment_1[i]+[0]*(129-len(segment_1[i]))
    return segment_1


@main_bp.route('/home', methods=['GET','POST'])
#@app.route('/home',methods= ['GET','POST'])
def read_csv():
    if request.method=="POST":
        if request.files.get("txt",None) is not None: 
            f=request.files["txt"]
            f.save(secure_filename('hello.txt'))
            data=pd.read_csv('hello.txt')
            data = data[data.S != 'T001']   
            data = data[data.S != 'T002']
            data = data[data.S != 'T003']
            data = data[data.S != 'T004']
            data = data[data.S != 'T005']
            data = data[data.S != 'M020']  
            data = data[data.S != 'M007']
            data = data[data.S != 'M019']
            data = data[data.S != 'M027']
            ep_seg = data.copy()
            ep_seg = ep_seg[ep_seg.S != 'D001']
            ep_seg = ep_seg[ep_seg.S != 'D002']
            ep_seg = ep_seg[ep_seg.S != 'D004']
            ep_seg = ep_seg[ep_seg.S != 'LEAVEHOME']
            ep_seg = ep_seg[ep_seg.S != 'ENTERHOME']
            ep_seg = ep_seg[ep_seg.S != 'c']
            ep_seg = ep_seg[ep_seg.M != 'OFFc']
            ep_seg = ep_seg[ep_seg.M != 'ONc']
            ep_seg = ep_seg[ep_seg.M != 'ON5']
            ep_seg = ep_seg[ep_seg.M != 'OFF5']
            ep_seg = ep_seg[ep_seg.M != 'ONcc']
            ep_seg = ep_seg[ep_seg.M != 'OFF5c']
            ep_seg = ep_seg[ep_seg.M != 'ON5c']
            ep_seg = ep_seg[ep_seg.M != 'OFFcc']
            ep_seg = ep_seg[ep_seg.M != 'OFFc5']
            ep_seg = ep_seg[ep_seg.M != 'ONc5']
            ep_seg = ep_seg[ep_seg.M != 'OFcF']
            ep_seg = ep_seg[ep_seg.M != 'ONc5c']
            ep_seg = ep_seg[ep_seg.M != 'ONM024']
            ep_seg = ep_seg[ep_seg.M != 'ON55']
            ep_seg = ep_seg[ep_seg.M != 'OFF5cc']
            ep_seg = ep_seg[ep_seg.M != 'ONM026']
            ep_seg = ep_seg[ep_seg.M != 'OFFccc5']
            ep_seg = ep_seg[ep_seg.M != 'ONM009']
            ep_seg = ep_seg[ep_seg.M != 'O']
            ep_seg1 = ep_seg.copy()
            ep_seg1 = ep_seg[ep_seg1.M != 'OFF']
            ep_segt=list(ep_seg1.Time)
            ep_segs=list(ep_seg1.S)
            num1={}
            num1[0]=0
            num1['M001']=1
            num1['M002']=2
            num1['M003']=3
            num1['M004']=4
            num1['M005']=5
            num1['M006']=6
            num1['M007']=7
            num1['M008']=8
            num1['M009']=9
            num1['M010']=10
            num1['M011']=11
            num1['M012']=12
            num1['M013']=13
            num1['M014']=14
            num1['M015']=15
            num1['M016']=16
            num1['M017']=17
            num1['M018']=18
            num1['M019']=19
            num1['M020']=20
            num1['M021']=21
            num1['M022']=22
            num1['M023']=23
            num1['M024']=24
            num1['M025']=25
            num1['M026']=26
            num1['M027']=27
            num1['M028']=28
            num1['M029']=29
            num1['M030']=30
            num1['M031']=31 
            for i in range(len(ep_segt)):
                data_pre = ep_segt[i].strip().split(',')
                stDate = data_pre[0].replace("\"", "")
                #print ("stDate before: ", stDate)
                try:
                    dat_time = datetime.datetime.strptime(stDate,
                               '%H:%M:%S.%f')                                  
                except:
                    stDate = stDate + ".4"
                    dat_time = datetime.datetime.strptime(stDate,'%H:%M:%S.%f')
                    ep_segt[i] = stDate
            
            segment = []
            new = []
            new.append(ep_segs[0])
            f=0
            prev_time =  '00:03:50.209589'
            datetimeFormat = '%H:%M:%S.%f'

            for i in range(1,len(ep_seg1)):
                diff = datetime.datetime.strptime(ep_segt[i], datetimeFormat) - datetime.datetime.strptime(prev_time, datetimeFormat)
                prev_time = ep_segt[i]
                if diff.seconds > 10 or (ep_segs[i-1]==ep_segs[i]):
                    if(len(new)>0):
                        segment.append(new)
                        E = []
                        E.append(ep_segs[i])
                        new = E
                else:
                    new.append(ep_segs[i])    
            if(len(new)>0):
                segment.append(new)    
            l=[segment[i] for i in range(len(segment)) if len(segment[i])<=32 and len(segment[i])>3]
            l=features(l)
            h=[]
            for i in range(len(l)):
                k=[]
                for j in range(len(l[i])):
                    k.append(num1[l[i][j]])
                h.append(k)
            l=h 
            l=np.asarray(l)
            l=np.reshape(l,(l.shape[0],l.shape[1],1))
            #l=[[num1[i] for i in x] for x in l]
            model = load_model('model.hdf5')
            t=model.predict(l)
            h=t.argmax(axis=-1)
            c=0
            for i in h:
                if i==0:
                    c+=1
            g=(c*1.0/len(h))*100.0
            email=current_user.email
            score= Score(email=email,result=g)
            db.session.add(score)
            db.session.commit()
            #email=current_user.email
            #score= Score.query.filter_by(email=email).first()
            #score.objects().all()
            return flask.render_template('result.html',listt=g)


@main_bp.route('/history', methods=['GET','POST'])
def history():
    if request.method=="GET":
            email=current_user.email
            score= Score.query.filter_by(email=email)
            y=list()
            for x in score:
                y.append(x.result)
            return flask.render_template('history.html',history=y)
