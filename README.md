# sendpost
Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.

## Requirements.

Python &gt;&#x3D;3.7


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/arseniusz8/sendpost_py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/arseniusz8/sendpost_py.git`)

Then import the package:
```python
import sendpost_py
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sendpost_py
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import sendpost_py
from pprint import pprint
from sendpost_py.apis.tags import email_api
from sendpost_py.model.email_message import EmailMessage
from sendpost_py.model.email_response import EmailResponse
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_py.Configuration(
    host = "https://api.sendpost.io/api/v1"
)


# Enter a context with an instance of the API client
with sendpost_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)
    x_sub_account_api_key = "X-SubAccount-ApiKey_example" # str | Sub-Account API Key
email_message = EmailMessage(
        attachments=[
            Attachment(
                content="V2VsY29tZSB0byBTZW5kUG9zdCEgOikK",
                filename="file0.txt",
            )
        ],
        _from=ModelFrom(
            email="gavin@hooli.com",
            name="Gavin Belson",
        ),
        groups=["promotion","techcrunch-launch"],
        html_body="<html><body>Thanks for your trust in Hooli {{.Name}}. We are trying launching Nucleus at TechCrunch Disrupt - our cloud based compression platform. That you could easily integrate it into {{.Company}}.</html></body>",
        ippool="promotional-hooli",
        pre_text="Follow the steps to integrate our video compression API",
        reply_to=ReplyTo(
            email="welcome@hooli.vom",
            name="Team @ Hooli",
        ),
        subject="Welcome to Nucles {{.Name}}:) Let's get started",
        template="welcome-onboarding",
        text_body="Thanks for your trust in Hooli {{.Name}}. We are trying launching Nucleus at TechCrunch Disrupt - our cloud based compression platform. That you could easily integrate it into {{.Company}}",
        to=[
            To(
                name="Elrich Bachman",
                email="elrich@bachmanity.com",
                cc=[
                    CopyTo(
                        name="Nelson Bighetti",
                        email="bighead@bachmanity.com",
                        custom_fields=dict(),
                    )
                ],
,
                custom_fields=dict(),
            )
        ],
        track_clicks=True,
        track_opens=True,
        headers=dict(),
        amp_body="amp_body_example",
    ) # EmailMessage | Email message (optional)

    try:
        api_response = api_instance.send_email(x_sub_account_api_keyemail_message=email_message)
        pprint(api_response)
    except sendpost_py.ApiException as e:
        print("Exception when calling EmailApi->send_email: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.sendpost.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EmailApi* | [**send_email**](docs/apis/tags/EmailApi.md#send_email) | **post** /subaccount/email/ | 
*EmailApi* | [**send_email_with_template**](docs/apis/tags/EmailApi.md#send_email_with_template) | **post** /subaccount/email/template | 

## Documentation For Models

 - [Attachment](docs/models/Attachment.md)
 - [City](docs/models/City.md)
 - [CopyTo](docs/models/CopyTo.md)
 - [Device](docs/models/Device.md)
 - [EmailMessage](docs/models/EmailMessage.md)
 - [EmailResponse](docs/models/EmailResponse.md)
 - [EventMetadata](docs/models/EventMetadata.md)
 - [ModelFrom](docs/models/ModelFrom.md)
 - [Os](docs/models/Os.md)
 - [QEmailMessage](docs/models/QEmailMessage.md)
 - [QEvent](docs/models/QEvent.md)
 - [ReplyTo](docs/models/ReplyTo.md)
 - [To](docs/models/To.md)
 - [UserAgent](docs/models/UserAgent.md)
 - [WebhookEvent](docs/models/WebhookEvent.md)

## Documentation For Authorization

 Endpoints do not require authorization.


## Author

hello@sendpost.io

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in sendpost_py.apis and sendpost_py.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from sendpost_py.apis.default_api import DefaultApi`
- `from sendpost_py.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import sendpost_py
from sendpost_py.apis import *
from sendpost_py.models import *
```