Swahili SMS Filter
Swahili SMS Filter is a Flask-based application that filters incoming SMS messages for spam using a machine learning model. The project integrates with Africa's Talking API to forward legitimate messages and send warnings for suspected spam. It also includes a simple web dashboard to monitor processed messages and their classifications.

Features
SMS Spam Detection: Uses a trained Logistic Regression model with TF-IDF vectorization to classify incoming SMS as spam or ham.
Africa's Talking Integration: Forwards non-spam messages and sends warning messages for detected spam.
API Endpoints:
POST /incoming-messages - Process incoming SMS messages.
GET / or /dashboard - View a dashboard with processed message logs.
Dashboard: A Bootstrap-powered HTML dashboard displays message logs, including sender, recipient, timestamp, spam status, and confidence score.
Technologies Used
Backend: Python, Flask
Machine Learning: scikit-learn (Logistic Regression, TF-IDF Vectorizer)
SMS API: Africa's Talking
Environment Management: python-dotenv
Other: Pickle for saving/loading the model and vectorizer
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/swahili_sms_filter.git
cd swahili_sms_filter
Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install the Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(Make sure your requirements.txt includes: Flask, africastalking, python-dotenv, scikit-learn, pandas, numpy)

Set Up Environment Variables:

Create a .env file in the project root and add your Africa's Talking credentials:

env
Copy
Edit
AT_USERNAME=sandbox
AT_API_KEY=your_api_key
Usage
Ensure you have the model and vectorizer files:

spam_model.pkl
vectorizer.pkl
(If you haven’t created them, train your model using your data and save these files as described in the project documentation.)

Run the Flask App:

bash
Copy
Edit
python app.py
API Endpoints:

Process Incoming Message:
URL: http://127.0.0.1:5000/incoming-messages
Method: POST
Example JSON Body:
json
Copy
Edit
{
  "from": "+254712345678",
  "text": "Pata loan sasa hivi! Bonyeza hapa kujisajili.",
  "to": "+254798765432"
}
Dashboard / Logs:
URL: http://127.0.0.1:5000/ (or /dashboard if configured)
Method: GET
This will display a web dashboard of all processed messages.
Project Structure
bash
Copy
Edit
swahili_sms_filter/
│── app.py                 # Main Flask application
│── spam_model.pkl         # Trained ML model for spam detection
│── vectorizer.pkl         # TF-IDF vectorizer
│── .env                   # Environment variables
│── requirements.txt       # Python dependencies
│── templates/
│   └── dashboard.html     # Dashboard template for viewing logs
│── venv/                  # Virtual environment directory
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Africa's Talking for the SMS API.
Patric Paul for the Model Dataset
Flask for the lightweight web framework.
scikit-learn for the machine learning tools.
