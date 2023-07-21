<a id="__pageTop"></a>
# sendpost_py.apis.tags.email_api.EmailApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](#send_email) | **post** /subaccount/email/ | 
[**send_email_with_template**](#send_email_with_template) | **post** /subaccount/email/template | 

# **send_email**
<a id="send_email"></a>
> [EmailResponse] send_email(x_sub_account_api_key)



Send Email To Contacts

### Example

```python
import sendpost_py
from sendpost_py.apis.tags import email_api
from sendpost_py.model.email_message import EmailMessage
from sendpost_py.model.email_response import EmailResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_py.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.send_email(
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_py.ApiException as e:
        print("Exception when calling EmailApi->send_email: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    body = EmailMessage(
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
    )
    try:
        api_response = api_instance.send_email(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except sendpost_py.ApiException as e:
        print("Exception when calling EmailApi->send_email: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailMessage**](../../models/EmailMessage.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_email.ApiResponseFor200) | \&quot;Email Message Processed Successfully\&quot;
401 | [ApiResponseFor401](#send_email.ApiResponseFor401) | Not Authorized
422 | [ApiResponseFor422](#send_email.ApiResponseFor422) | Request body is not in proper format
500 | [ApiResponseFor500](#send_email.ApiResponseFor500) | Internal Server Error

#### send_email.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) | [**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) | [**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) |  | 

#### send_email.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_email.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_email.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **send_email_with_template**
<a id="send_email_with_template"></a>
> [EmailResponse] send_email_with_template(x_sub_account_api_key)



Send Email To Contacts With Template

### Example

```python
import sendpost_py
from sendpost_py.apis.tags import email_api
from sendpost_py.model.email_message import EmailMessage
from sendpost_py.model.email_response import EmailResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_py.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.send_email_with_template(
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_py.ApiException as e:
        print("Exception when calling EmailApi->send_email_with_template: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    body = EmailMessage(
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
    )
    try:
        api_response = api_instance.send_email_with_template(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except sendpost_py.ApiException as e:
        print("Exception when calling EmailApi->send_email_with_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailMessage**](../../models/EmailMessage.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#send_email_with_template.ApiResponseFor200) | \&quot;Email Message Processed Successfully\&quot;
401 | [ApiResponseFor401](#send_email_with_template.ApiResponseFor401) | Not Authorized
422 | [ApiResponseFor422](#send_email_with_template.ApiResponseFor422) | Request body is not in proper format
500 | [ApiResponseFor500](#send_email_with_template.ApiResponseFor500) | Internal Server Error

#### send_email_with_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) | [**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) | [**EmailResponse**]({{complexTypePrefix}}EmailResponse.md) |  | 

#### send_email_with_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_email_with_template.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### send_email_with_template.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

