from flask import Flask, render_template, request
from flask_cors import cross_origin
import logging
from datetime import datetime
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    logger.debug("Redirecting to Index.html")
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
@cross_origin()
def pred_output():
    try:
        ZN = float(request.form['zn'])
        INDUS = float(request.form['indus'])
        CHAS = float(request.form['chas'])
        NOX = float(request.form['nox'])
        RM = float(request.form['rm'])
        AGE = float(request.form['age'])
        DIS = float(request.form['dis'])
        PTRATIO = float(request.form['ptratio'])
        B = float(request.form['b'])
        LSTAT = float(request.form['lstat'])
        filename = 'modelForPrediction.pickle'
        scalar_filename = 'sandardScalar.sav'
        logger.debug("ZN :"+str(ZN))
        logger.debug("INDUS :" + str(INDUS))
        logger.debug("CHAS :" + str(CHAS))
        logger.debug("NOX :" + str(NOX))
        logger.debug("RM :" + str(RM))
        logger.debug("AGE :" + str(AGE))
        logger.debug("DIS :" + str(DIS))
        logger.debug("PTRATIO :" + str(PTRATIO))
        logger.debug("B :" + str(B))
        logger.debug("LSTAT :"+str(LSTAT))
        logger.debug("model filename :" + str(filename))
        logger.debug("scalar_filename :" + str(scalar_filename))
        loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
        logger.debug("model loaded successfully " )
        with open(scalar_filename, 'rb') as f:
            scalar = pickle.load(f)
        scaled_data = scalar.transform([[ZN, INDUS, CHAS, NOX, RM, AGE, DIS, PTRATIO, B, LSTAT]])
        predict = loaded_model.predict(scaled_data)
        logger.debug("prediction result :"+str(predict))
        return render_template('index.html', prediction_result=predict)
    except Exception as e:
        logger.error("Exception occured :"+str(e))
        return "something went wrong"


if __name__ == "__main__":
    logging.basicConfig(filename="logs/applog" + datetime.now().strftime('%d%m%Y') + ".log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    app.run(host='127.0.0.1', port=8001, debug=True)
# app.run(debug=True) # running the app
