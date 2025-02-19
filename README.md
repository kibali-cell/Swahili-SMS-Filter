# SMS Gateway Spam Filter

A Flask-based application that filters and processes incoming SMS messages using machine learning to detect spam.

## Features

- Real-time SMS spam detection using a pre-trained machine learning model
- Web dashboard to view message history and spam detection results
- Integration with Africa's Talking SMS API
- Environment-based configuration
- Detailed logging for troubleshooting

## Setup and Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Africa's Talking account with API credentials

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/sms-gateway-filter.git
   cd sms-gateway-filter
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Africa's Talking credentials:
   ```
   AT_USERNAME=your_africastalking_username
   AT_API_KEY=your_africastalking_api_key
   ```

5. Ensure you have the required ML model files:
   - `spam_model.pkl`
   - `vectorizer.pkl`

## Usage

### Starting the Server

Run the application:
```bash
python app.py
```

The server will start on http://127.0.0.1:5000/ by default.

### Available Endpoints

- **GET /** - Web dashboard for viewing filtered messages
- **POST /incoming-messages** - Endpoint for receiving SMS messages
- **GET /test** - Simple endpoint to verify server status

### Sending Test Messages

You can test the API by sending a POST request to the `/incoming-messages` endpoint:

```bash
curl -X POST http://localhost:5000/incoming-messages \
  -H "Content-Type: application/json" \
  -d '{"from": "+1234567890", "text": "Hello, this is a test message", "to": "+0987654321"}'
```

## Message Processing

When a message is received:
1. The system extracts the sender, message content, and recipient
2. The machine learning model analyzes the message to determine if it's spam
3. Results are stored with confidence scores and timestamps
4. All processed messages appear in the web dashboard

## Development

### Logging

The application uses Python's built-in logging module. Debug logs can be found in the console output when running in debug mode.

### Extending the Filtering Model

To update or improve the spam detection model:

1. Train a new model using scikit-learn
2. Export the model and vectorizer:
   ```python
   import pickle
   with open('spam_model.pkl', 'wb') as f:
      pickle.dump(model, f)
   with open('vectorizer.pkl', 'wb') as f:
      pickle.dump(vectorizer, f)
   ```
3. Replace the existing files in the project directory

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.