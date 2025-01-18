
# Crop Yield Prediction Web Application

This project aims to predict the most suitable crops for cultivation based on various factors like soil nutrients, pH, temperature, and other environmental variables. The application uses machine learning models to help farmers make informed decisions.

## Contributors

### [Gautham Nair](https://github.com/Gauthamnair-Ronin)
- Co-conceived the project idea and assisted with dataset hunting and exploratory data analysis (EDA).
- Contributed to feature engineering and preprocessing for the classification dataset.
- Developed the machine learning classifier model and integrated it into the Flask web application.
- Designed and implemented the web application using Flask, HTML, and CSS.
- Managed the deployment process using Waitress for local hosting and Render for production deployment.

### [Afidh S Muhammed](https://github.com/)
- Co-conceived the project idea and assisted with dataset hunting and exploratory data analysis (EDA).
- Contributed to feature engineering and preprocessing for the regression dataset.
- Developed the regressor model for predicting crop yield based on environmental factors.
- Collaborated in fine-tuning the machine learning models and ensured their proper integration.

## About the Models

- **Classification Model**: This model predicts the crop type based on various soil and environmental features.
- **Regression Model**: This model predicts the crop yield based on environmental conditions such as temperature, soil pH, and more.

## Technologies Used
- Python
- Flask
- HTML, CSS, JavaScript
- Waitress
- Machine Learning (Random Forest Classifier, Regressor)
- GitHub, Render for deployment

## How to Run the Application
1. Clone the repository: `git clone https://github.com/yourusername/repository-name.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask app locally: `python app.py`
4. The application should be accessible at `http://127.0.0.1:5000/`.

## Deployment
The application is deployed and available at [Mitti Sathi](https://mitti-sathi.onrender.com). You can access the web application through this URL.


## Acknowledgments
- This project was developed through collaborative efforts between [Gautham Nair](https://github.com/Gauthamnair-Rnonin) and [Afidh S Muhammed](https://github.com/).
- Thanks to the tools and libraries used in this project: Flask, Waitress, scikit-learn, pandas, numpy, and matplotlib.
