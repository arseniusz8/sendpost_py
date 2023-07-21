# sendpost_py.model.q_email_message.QEmailMessage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ampBody** | str,  | str,  |  | [optional] 
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**attempt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[customFields](#customFields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**emailType** | str,  | str,  |  | [optional] 
**from** | [**ModelFrom**](ModelFrom.md) | [**ModelFrom**](ModelFrom.md) |  | [optional] 
**[groups](#groups)** | list, tuple,  | tuple,  |  | [optional] 
**[headerBcc](#headerBcc)** | list, tuple,  | tuple,  |  | [optional] 
**[headerCc](#headerCc)** | list, tuple,  | tuple,  |  | [optional] 
**headerTo** | [**To**](To.md) | [**To**](To.md) |  | [optional] 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**htmlBody** | str,  | str,  |  | [optional] 
**ipID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**ipPool** | str,  | str,  |  | [optional] 
**localIP** | str,  | str,  |  | [optional] 
**messageID** | str,  | str,  |  | [optional] 
**preText** | str,  | str,  |  | [optional] 
**publicIP** | str,  | str,  |  | [optional] 
**replyTo** | [**ReplyTo**](ReplyTo.md) | [**ReplyTo**](ReplyTo.md) |  | [optional] 
**subAccountID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**subject** | str,  | str,  |  | [optional] 
**submittedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**textBody** | str,  | str,  |  | [optional] 
**to** | [**To**](To.md) | [**To**](To.md) |  | [optional] 
**trackClicks** | bool,  | BoolClass,  |  | [optional] 
**trackOpens** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attachments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Attachment**](Attachment.md) | [**Attachment**](Attachment.md) | [**Attachment**](Attachment.md) |  | 

# customFields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# headerBcc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CopyTo**](CopyTo.md) | [**CopyTo**](CopyTo.md) | [**CopyTo**](CopyTo.md) |  | 

# headerCc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CopyTo**](CopyTo.md) | [**CopyTo**](CopyTo.md) | [**CopyTo**](CopyTo.md) |  | 

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

