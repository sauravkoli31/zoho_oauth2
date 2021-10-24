import json
import os
import pickle
import time
import urllib

import requests

__author__ = 'Saurav Koli'
__version__ = '1.0'


class ZohoAPITokens:

    def __init__(self, **kwargs):
        self.url = 'https://accounts.zoho.com/oauth/v2/token?'
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.redirect_uri = kwargs.get('redirect_uri')
        self.scope = kwargs.get('scope')
        self.confirmation_code = None
        self.token = None
        self.tokenPickleFile = 'token.pickle'

    def generate_access_and_refresh(self):
        '''
        Generate access and refresh token using the confirmation code from the api portal.

        Args:
            confirmation_code:

        Returns:
            token dict: Dict with following data -
                access_token string:
                refresh_token string:
                api_domain string:
                token_type string:
                expires_in int:
                valid_until epoch:
        '''
        params = {
            'code'         : self.confirmation_code,
            'grant_type'   : 'authorization_code',
            'client_id'    : self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri' : self.redirect_uri,
            'scope'        : self.scope
        }
        response = requests.request("POST", self.url + urllib.parse.urlencode(params))
        self.token = json.loads(response.text)
        if self.token.get('expires_in'):
            valid_until = time.time() + self.token.get('expires_in')
            self.token.update({'valid_until': valid_until})
            self.writePickle()
        else:
            raise Exception(f'Error occured while requesting token : {self.token}')
            return None

    def refreshToken(self):
        '''
        Generate access_token using refresh_token after the validity of the access_token has expired.
        Args:
            refresh_token: refresh token to generate new access token.

        Returns:
            new_token dict: dict with new access_token and validity.
        '''
        params = {
            'refresh_token': self.token.get('refresh_token'),
            'grant_type'   : 'refresh_token',
            'client_id'    : self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri' : self.redirect_uri,
            'scope'        : self.scope
        }
        response = requests.request("POST", self.url + urllib.parse.urlencode(params))
        refreshed_token = json.loads(response.text)
        access_token = refreshed_token.get('access_token')

        valid_until = time.time() + refreshed_token.get('expires_in')
        self.token.update({
            'access_token': access_token,
            'valid_until' : valid_until
        })
        self.writePickle()

    def writePickle(self):
        outfile = open(self.tokenPickleFile, 'wb')
        pickle.dump(self.token, outfile)
        outfile.close()

    def readPickle(self):
        infile = open(self.tokenPickleFile, 'rb')
        self.token = pickle.load(infile)
        infile.close()

    def auth_token(self):
        '''
        Uses OAuth2.0 to generate and refresh access_token for servicedesk.

        Returns:
            access_token string: Bearer access_token to access servicedesk apis.
        '''
        if not self.client_id or not self.client_secret:
            print("No Client ID and Client Secret present. Please read the documentation.")
            return f'ERROR: APPLICATION NOT CONFIGURED.'
        if not os.path.isfile(self.tokenPickleFile):
            print(
                f'ERROR: {self.tokenPickleFile} does not exist. No access and refresh token has been generated or missing.\n'
                f'Visit https://api-console.zoho.com/client/{self.client_id}, add Scope, Description and Generate the code.')
            self.confirmation_code = input("Enter the Generated Code : ")
            self.generate_access_and_refresh()
        else:
            self.readPickle()
            validity = self.token.get('valid_until')
            if not validity > time.time():
                self.refreshToken()
        return self.token.get('access_token')
