# pH-data-prediction
Colorimetry is the technique used to determine the concentration of colored
compounds in a solution. The aim of the project includes developing machine learning models
and algorithms, to predict colorimetric property such as pH of an analyte using primary
colors(RGB) values. Using the ML model which predicts pH value, we can obtain real pH
predicted value using a web application.

### Report
Project presentation is available at https://github.com/bahl24/pH-data-prediction/blob/master/Poster%20-%20pH%20predictor.pdf

### Data
The dataset is in CSV(comma separated values) format obtained
from ​ https://www.kaggle.com/robjan/ph-recognition​ . The data
consists of 4 columns having RGB color values. Three columns have
the features - blue, green, red and the fourth column has the label
which is the pH(0-14).
There are 653 distinct data points(rows) covering all the pH range
from 0-14 with almost equal distribution.

### Using Machine Learning for prediction
I compared the performance of 6 common ML algorithms:- Linear Regression, Logistic Regression, KNN, SVM, Decision Trees & Random Forest Classifier, RFC gave the least MSE (0.51) and highest accuracy (72%).
Thus, I trained and built an RFC based ML model and saved it, to use it in the web app.

### Saving model using Pickle
Pickle is the standard way of serializing objects in Python. Pickle operation
can be used to serialize ML algorithms and save the serialized format to a
file. Pickle can save this as a binary file, which can be loaded in another
program to deserialize and make predictions with the model.

### Developing a web app
Next step after saving the ML model, is to develop a web application to
enable users to actually use the model and make the predictions. I've used VueJS (a JS framework) to build the frontend part of the web app.

As the pickle model is Python-based, we need to develop a Flask based
REST API backend to fetch and post data via HTTP to the web page.
