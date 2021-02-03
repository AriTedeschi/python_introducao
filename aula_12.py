# pip --version
# pip --help
# pip freeze
# pip list : 
# pip install requests
# pip freeze

import requests
response = requests.get()
print(response.status_code)
print(response.json())
