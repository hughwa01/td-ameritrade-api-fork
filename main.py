from pprint import pprint
from configparser import ConfigParser
import td
from td.credentials import TdCredentials
from td.client import TdAmeritradeClient


# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('td/config/config.ini')

# Get the specified credentials.
client_id = config.get('main', 'client_id')
redirect_uri = config.get('main', 'redirect_uri')

# Intialize our `Credentials` object.
td_credentials = TdCredentials(
    client_id=client_id,
    redirect_uri=redirect_uri,
    credential_file='td/config/td_credentials.json'
)

# Initalize the `TdAmeritradeClient`
td_client = TdAmeritradeClient(
    credentials=td_credentials
)

# Grab a single quote.
pprint(td_client.quote_service.get_quote(instrument='AAPL'))