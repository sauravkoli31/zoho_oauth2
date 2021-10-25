# Zoho API - OAuth 2.0

Uses OAuth 2.0 for generating access_tokens for using Zoho APIs.

## Installation

Install the package using pip.

    pip install zoho-oauth2

## Generate required credentials

- **CLIENT_ID**
- **CLIENT_SECRET** 
>Generate the two values from [https://api-console.zoho.com/](https://api-console.zoho.com/).
Add a self client, and copy the CLIENT_ID and CLIENT_SECRET as seen in the example below.

- **redirect_uri** 
>Add the redirect uri of your instance.

- **scope**
>You can find the list of scopes in the api documentation of the products you wish to use the API for.

- **region** 

>Select the region if required. Chooses https://accounts.zoho.com by default. Following regions are supported as per Zoho Documentation.
>>EU : https://accounts.zoho.eu

>>CN : https://accounts.zoho.com.cn

>>IN : https://accounts.zoho.in

## API Documentation

The access tokens have only been tested with Manage Engine Service Desk instance in a demo environment, although it should work with most Zoho products. 

Learn more about the APIs from the link below.

- [ZOHO People API Documentation](https://www.zoho.com/people/api/overview.html)

- [ManageEngine ServiceDesk Plus Cloud API Documentation](https://www.manageengine.com/products/service-desk/sdpod-v3-api/index.html)

## Available methods to use.

- To generate the access token for making the API Requests.
```Python
    ZohoAPITokens(
        client_id=CLIENT_ID, #Required
        client_secret=CLIENT_SECRET, #Required
        redirect_uri=REDIRECT_URI, #Required
        scope=SCOPES(as string, each scope separated by comma), #Required
        region=REGION #Optional
    )
```

- To revoke the refresh token. The method will revoke the access token and proceed with deleting the token.pickle file.
```Python
    revokeRefreshToken()
```

## Example Usage


    from zoho_oauth2 import ZohoAPITokens
    
    if __name__ == '__main__':
        test = ZohoAPITokens(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPES(as string, each scope separated by comma)
        )
