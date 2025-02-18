# Swahili SMS Filter

Swahili SMS Filter is a Flask-based application that filters incoming SMS messages for spam using a machine learning model. The project integrates with Africa's Talking API to forward legitimate messages and send warnings for suspected spam. Includes a web dashboard for monitoring.

## Features

- **SMS Spam Detection**
  - Logistic Regression model with TF-IDF vectorization
  - Classifies messages as spam/ham with confidence scores
  
- **Africa's Talking Integration**
  - Forwards legitimate messages
  - Sends spam warnings via SMS

- **API Endpoints**
  - `POST /incoming-messages` - Process incoming SMS
  - `GET /` - View message dashboard

- **Dashboard**
  - Bootstrap-powered interface
  - Displays sender, recipient, timestamp, spam status, and confidence

## Technologies Used

- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas, numpy
- **SMS Gateway:** Africa's Talking API
- **Utilities:** python-dotenv, pickle

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/swahili_sms_filter.git
   cd swahili_sms_filter
