from flask import Flask, jsonify, request, render_template
from http import HTTPStatus
import pdb

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verification endpoint to confirm ownership of the webhook
        verification_token = "D8V0dfGXsa"
    
        if request.args.get('hub.verify_token') == verification_token:
            # return '<meta property="og:image" content="https://png.pngtree.com/element_pic/16/12/07/921c6d12350e366ee4af07eb9055ab40.jpg"/>'
            # return {"og.image": "https://png.pngtree.com/element_pic/16/12/07/921c6d12350e366ee4af07eb9055ab40.jpg"}
            return render_template("index.html")
            # return request.args.get('hub.challenge'), HTTPStatus.OK
        else:
            return 'Invalid verification token1' 

    elif request.method == 'POST':
        # Handle incoming webhook events
        data = request.json
        pdb.set_trace()
        if data['object'] == 'page':
            for entry in data['entry']:
                for messaging_event in entry['messaging']:
                    if messaging_event.get('message'):
                        sender_id = messaging_event['sender']['id']
                        message_text = messaging_event['message']['text']
                        # Process the message or store verification token'the sender_id as needed
        return jsonify({'status': 'success'}), HTTPStatus.OK

    # params = request.args
    # verify_token = params.get("hub.verify_token")
    # chalenge = params.get('hub.challenge')
    # if verify_token == "meta-dev":    
    #     return chalenge
    # return False

@app.route('/policy', methods=['GET'])
def policy():
    return {"success": True}

if __name__ == '__main__':
    app.run()






# callback URL 
# https://8821-49-248-66-146.ngrok-free.app/webhook
# meta-dev - token
# D8V0dfGXsa