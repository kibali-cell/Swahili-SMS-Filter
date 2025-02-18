from flask import Flask, request, jsonify, render_template
import africastalking
import pickle
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Changed to DEBUG for more info
logger = logging.getLogger(__name__)

class SMSGatewayFilter:
    def __init__(self):
        # Initialize Africa's Talking
        self.username = os.getenv('AT_USERNAME')
        self.api_key = os.getenv('AT_API_KEY')
        
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS
        
        # Load the spam detection model
        with open('spam_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open('vectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f)
        
        # Initialize message store
        self.filtered_messages = []
    
    def check_spam(self, message):
        features = self.vectorizer.transform([message])
        prediction = self.model.predict(features)[0]
        confidence = max(self.model.predict_proba(features)[0])
        return prediction == 0, confidence
    
    def process_incoming_message(self, sender, message, recipient):
        is_spam, confidence = self.check_spam(message)
        
        timestamp = datetime.now().isoformat()
        
        message_log = {
            'timestamp': timestamp,
            'sender': sender,
            'recipient': recipient,
            'message': message,
            'is_spam': is_spam,
            'confidence': round(confidence * 100, 2)
        }
        
        self.filtered_messages.insert(0, message_log)
        return message_log

# Initialize the filter
sms_filter = SMSGatewayFilter()

@app.route('/')
def dashboard():
    return render_template('dashboard.html', messages=sms_filter.filtered_messages)

@app.route('/incoming-messages', methods=['POST'])
def handle_incoming_message():
    # Add debugging logs
    logger.debug(f"Received request with headers: {dict(request.headers)}")
    logger.debug(f"Received request with data: {request.get_data()}")
    
    try:
        data = request.get_json()
        logger.debug(f"Parsed JSON data: {data}")
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        required_fields = ['from', 'text', 'to']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        result = sms_filter.process_incoming_message(
            sender=data['from'],
            message=data['text'],
            recipient=data['to']
        )
        
        logger.debug(f"Processed message with result: {result}")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Add a test endpoint
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'status': 'OK', 'message': 'Server is running'}), 200

if __name__ == '__main__':
    # Print startup message
    print("Server starting...")
    print("Available endpoints:")
    print("  - GET  /           (Dashboard)")
    print("  - POST /incoming-messages (SMS Processing)")
    print("  - GET  /test       (Server Status)")
    app.run(debug=True)