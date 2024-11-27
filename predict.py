import pickle
from flask import Flask

input_file='model_1.bin'
f_in= open(input_file,'rb')
dv,model=pickle.load(f_in)
f_in.close()

user={'customerid': '5575_gnvde'}

# from here start **/**/**/**/
from flask import request
from flask import jsonify
app=Flask('predict')
@app.route('/predict',methods=['POST'])
def predict():
   customer=request.get_json()
   x_user= dv.transform([customer])
   x_pred=model.predict_proba(x_user)[0,1]
   churn=x_pred>=0.5
   result={
       'converted_proba':x_pred,
       'converted': bool(churn)
   }
   return jsonify(result)
if __name__=="__main__":
   app.run(debug=True,host='0.0.0.0',port=9696)
