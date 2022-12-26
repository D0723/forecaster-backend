# from crypt import methods
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
from symbol import simil,coins
from mod import Predictions
from pipeline import Crypto
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from extract import postgres    
app = Flask(__name__)
CORS(app)
from Functions import Predict
import pandas as pd
##################################_______________________________________________________Crone Function_____________________________________________________________###############################################
df=postgres()
def ditrubition():
    c= Crypto()
    c.CoinCaP(simil)
    c.Polygon(coins)
    data=postgres()
    Predictions(data)

##################################_______________________________________________________Recommendation Prediction Page_____________________________________________________________###############################################
@app.route("/predict1", methods=['GET', 'POST'])
def predict():
    # if request.method == 'GET':
    data=request.json
    if data:
            t=list(data.values())
            s,m,c,e=Predict(t)
            return jsonify(s,m,c,e)
##################################_______________________________________________________Forecasting Page_____________________________________________________________###############################################



@app.route('/forecast',methods=['GET','POST'])
def Forcast():
    pred=pd.read_csv('prediction.csv')
    # ln=len(pred['Day'])
    # return render_template('forecast.html',l=ln,
    # data1=list(simil.values()),
    data1=[elem for elem in pred['Coins']]
    # data2=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}],coins=pred['Coins'],
    data3= [ '%.2f' % elem for elem in pred['Day']],
    data4=[ '%.2f' % elem for elem in pred['Week']],
    data5=[ '%.2f' % elem for elem in pred['2Weeks']]
    data={
        'Symbol':data1,
        'Day':data3,
        'Week':data4,
        '2Weeks':data5
    }
    return jsonify(data)



##################################_______________________________________________________Forecasting Prediction Page_____________________________________________________________###################################################
@app.route('/predict2',methods=['GET','POST'])
def predict2():
    data = request.json
    t=data['Coin']
    cn=t
    pred=pd.read_csv('prediction.csv')
    c=[elem for elem in pred['Coins']]
    if cn in c:
                coin=cn
                p=df['open'].loc[df['symbol']== coin]  
                m=df['marketcap'].loc[df['symbol']== coin]
                v=df['volume'].loc[df['symbol']== coin]
                day=pred['Day'].loc[pred['Coins']== coin]
                week=pred['Week'].loc[pred['Coins']== coin]
                weeks=pred['2Weeks'].loc[pred['Coins']== coin]
                market=['%.2f' % float(m1) for m1 in m][0],
                price=['%.2f' % float(p1) for p1 in p][0],
                volume=['%.2f' % float(v1) for v1 in v][0]
                day='%.3f' % float(day)
                week='%.3f' % float(week)
                weeks='%.3f' % float(weeks)
                dt={'Symbol':coin,
                    'Price':price[0],
                    'MarketCap':market[0],
                    'Volume':volume,
                    'Day':day,
                    'Week':week,
                    '2Weeks':weeks
                    }
                return jsonify(dt)
    else:
                data1=[elem for elem in pred['Coins']]
                data3= [ '%.2f' % elem for elem in pred['Day']],
                data4=[ '%.2f' % elem for elem in pred['Week']],
                data5=[ '%.2f' % elem for elem in pred['2Weeks']]
                data={
                    'Symbol':data1,
                    'Day':data3,
                    'Week':data4,
                    '2Weeks':data5
                }
                return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False,host='https://forecast-endpoint.herokuapp.com',port=5000)
    # app.run(debug=True) 
