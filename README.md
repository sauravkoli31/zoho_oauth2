# Manage Engine - Service Desk OAuth 2.0

Uses OAuth 2.0 for generating access_tokens for using Zoho APIs.


## Generate required credentials

- **CLIENT_ID | CLIENT_SECRET** - Generate the two values from [https://api-console.zoho.com/](https://api-console.zoho.com/).
Add a self client, and copy the CLIENT_ID and CLIENT_SECRET as seen in the example below.

## API Documentation

The access tokens have only been tested with Manage Engine Service Desk although it should work with most Zoho products. 

Learn more about the APIs from the link below.

- [ManageEngine ServiceDesk Plus Cloud API Documentation](https://www.manageengine.com/products/service-desk/sdpod-v3-api/index.html)

- [ZOHO People API Documentation](https://www.manageengine.com/products/service-desk/sdpod-v3-api/SDPOD-V3-API.html#add-request)


## Example Usage


    from zoho_oauth2 import ZohoAPITokens
    
    if __name__ == '__main__':
        test = ZohoAPITokens(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPES(as string, each scope separated by comma)
        )
        print(test.auth_token())