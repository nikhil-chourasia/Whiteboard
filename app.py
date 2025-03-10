import os

from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token')
def generate_token():
    # Fetching Credentials from Environment Variables
    accountSid = os.getenv('TWILIO_ACCOUNT_SID')
    apiKey = os.getenv('TWILIO_API_KEY')
    apiSecret = os.getenv('TWILIO_API_SECRET')
    syncServiceSid = os.getenv('TWILIO_SYNC_SERVICE_SID')
    username = request.args.get('username', fake.user_name())

    # Creating Accesss Token with Credentials
    token = AccessToken(accountSid, apiKey, apiSecret, identity=username)

    # Creating a  Sync grant and add to a token
    sync_grant = SyncGrant(syncServiceSid)
    token.add_grant(sync_grant)
    return jsonify(identity=username, token=token.to_jwt())
