# sendpost_py.model.email_message.EmailMessage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attachments](#attachments)** | list, tuple,  | tuple,  |  | [optional] 
**from** | [**ModelFrom**](ModelFrom.md) | [**ModelFrom**](ModelFrom.md) |  | [optional] 
**[groups](#groups)** | list, tuple,  | tuple,  |  | [optional] 
**htmlBody** | str,  | str,  |  | [optional] 
**ippool** | str,  | str,  |  | [optional] 
**preText** | str,  | str,  |  | [optional] 
**replyTo** | [**ReplyTo**](ReplyTo.md) | [**ReplyTo**](ReplyTo.md) |  | [optional] 
**subject** | str,  | str,  |  | [optional] 
**template** | str,  | str,  |  | [optional] 
**textBody** | str,  | str,  |  | [optional] 
**[to](#to)** | list, tuple,  | tuple,  |  | [optional] 
**trackClicks** | bool,  | BoolClass,  |  | [optional] 
**trackOpens** | bool,  | BoolClass,  |  | [optional] 
**[headers](#headers)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**ampBody** | str,  | str,  |  | [optional] 
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

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**To**](To.md) | [**To**](To.md) | [**To**](To.md) |  | 

# headers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

