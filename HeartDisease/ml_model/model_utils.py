from sklearn.linear_model import LogisticRegression
import pickle

def get_result(age,	gender,	cp,	trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    filename = 'ml_model/cardiology_pickle'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    # Make predictions
    return  model.predict([[age,	gender,	cp,	trestbps,	chol,	fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    