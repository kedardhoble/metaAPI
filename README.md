# Facebook Messenger Webhook with Flask

This is a Flask application that acts as a webhook for receiving and handling messages from the Facebook Messenger platform.

## Overview

This Flask application serves as a webhook to interact with the Facebook Messenger platform. It handles incoming messages, verifies the webhook, and processes user messages.

## Getting Started

1. **Clone the Repository:**

2. **Install Dependencies:**
Install the required packages using `pip`:

3. **Configuration:**
Replace the following placeholders in the `app.py` file:
- `page_id`: Your Facebook page ID
- `page_access_token`: Your Facebook page access token
- `user_access_token`: Your user access token

4. **Run the Application:**
Run the Flask application using:

5. **Expose Locally with ngrok:**
To test the webhook locally, you can use [ngrok](https://ngrok.com/):
Copy the generated ngrok URL and update your Facebook App's webhook settings.

## Usage

- Verify Webhook:
- Access `http://localhost:5000/webhook` to verify the webhook using your browser.

- Handle Incoming Messages:
- The webhook listens for incoming messages from the Facebook Messenger platform.
- Messages are processed in the `webhook` function in the `app.py` file.
- Customize the message processing logic as needed.

- Policy Endpoint:
- Access `http://localhost:5000/policy` to retrieve a policy JSON response.

## Important Notes

- This application is intended for educational and demonstration purposes.
- Keep sensitive information (tokens, secrets) secure and do not share them in public repositories.
- Adapt the code to your use case and ensure proper error handling and security practices.
