# IrisFlowerPredictor

Yes, I know this dataset has been analysed in its entirety over the years but as someone who is new to ML, everyone should get familiar with this dataset. Also, I wanted to create a simple web-app using flask to predict the iris species as a beginner's project. This dataset is particularly handy for newbies because there are very few features present. It is good to explore and play with the data using pandas. It is also good for learning basic visualization techniques such as barplots, histograms, boxplots and many more using matplotlib and seaborn.

## Table of Contents
* Overview/Problem Statement
* Dataset
* File Structure
* Major Packages/Libraries Used
* Installation/Working Environment
* Building the Web App
* Model Deployment on Heroku Platform
* App Implementation

### 1. Overview/Problem Statement
The Iris dataset was used in R.A. Fisher's classic 1936 paper, 'The Use of Multiple Measurements in Taxonomic Problems', and can also be found on the UCI Machine Learning Repository. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

### 2. Dataset
* The dataset was taken from UCI Machine Learning Repository and is available on Kaggle. 
* The dataset contains the following features: **Id**, **SepalLength(Cm)**, **SepalWidth(Cm)**, **PetalLength(Cm)**, **PetalWidth(Cm)** and **Species**.
* [Dateset Link](https://www.kaggle.com/uciml/iris)

### 3. File Structure
```
├── static 
│   ├── iris.jpg
├── templates
│   ├── home.html
├── Iris.csv
├── Notebook.ipynb
├── Procfile
├── README.md
├── app.py
├── iris.pkl
├── requirements.txt
```

### 4. Major Packages/Libraries Used
* pandas 
* numpy
* sci-kit learn
* matplotlib
* seaborn
* Flask
* gunicorn

### 5. Installation/Working Environment
Follow the instructions if you want to run the app from your local computer.
* The app is written using **Python 3.8.5**. You can download it from [here](https://www.python.org/downloads/).You can also download **Anaconda** which is a distribution of python from [here](https://www.anaconda.com/products/individual). I would recommend downloading anaconda since it is very useful as it comes with a lot of python libraries, Jupyter and Spyder IDE.
* Once you are done with the installation, you can clone this repository to your computer and install the required packages and libraries using the following line of code through the command prompt where your local environment is setup.
```
pip install -r requirements.txt
```
### 6. Building the Web App
* The web was developed using flask micro web framework which is written in python suitable for small scale projects such as this one. For more information you can check the offical flask website by clicking [here](https://flask.palletsprojects.com/en/2.0.x/)
* Basic HTML was needed for designing the webpage and to make sure it was responsive to user inputs. 

### 7. Model Deployment on Heroku Platoform
* You will have to create a account in order to deploy the model. Login to your account and go to the deploy section.
* Connect to your github repository and deploy the model manually or through Heroku CLI.

![3](https://user-images.githubusercontent.com/83957848/119222443-06092480-bb12-11eb-8102-086761ded15b.JPG)

### 8. App Implementation  
* Link: [IrisFlowerClassifier](https://irisflowerpredictor99.herokuapp.com/)  
* The app asks for user to enter the petal length and petalwidth of the flower. Based on these input the flower is classified as setosa, versicolor or virginica. From the data analysis it was found out that sepal characteristics are not good at classifying the flowers. 

![1](https://user-images.githubusercontent.com/83957848/120065868-32342080-c091-11eb-8fd2-62c865986d0f.JPG)

