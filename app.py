from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            # 1. Capture inputs from the form
            gender = request.form.get('gender')
            ethnicity = request.form.get('ethnicity')
            parental_level = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_prep = request.form.get('test_preparation_course')
            reading_raw = request.form.get('reading_score')
            writing_raw = request.form.get('writing_score')

            # 2. Validate that scores are provided and are within range
            if not reading_raw or not writing_raw:
                return render_template('home.html', results="Error: Please enter both scores.")

            reading_score = float(reading_raw)
            writing_score = float(writing_raw)

            if not (0 <= reading_score <= 100 and 0 <= writing_score <= 100):
                return render_template('home.html', results="Error: Scores must be between 0 and 100.")

            # 3. Create CustomData object
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level,
                lunch=lunch,
                test_preparation_course=test_prep,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("after Prediction")

            return render_template('home.html', results=results[0])

        except ValueError:
            # This catches cases where the input is not a valid number
            return render_template('home.html', results="Error: Please enter valid numeric scores.")
        except Exception as e:
            # General error handling
            return render_template('home.html', results=f"Error: {str(e)}")
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)        


