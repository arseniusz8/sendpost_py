# coding: utf-8

"""
    SendPost API

    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@sendpost.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sendpost_py import schemas  # noqa: F401


class QEmailMessage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            accountID = schemas.Int64Schema
            ampBody = schemas.StrSchema
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Attachment']:
                        return Attachment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Attachment'], typing.List['Attachment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Attachment':
                    return super().__getitem__(i)
            attempt = schemas.Int64Schema
            customFields = schemas.DictSchema
            emailType = schemas.StrSchema
        
            @staticmethod
            def _from() -> typing.Type['ModelFrom']:
                return ModelFrom
            
            
            class groups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'groups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class headerBcc(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CopyTo']:
                        return CopyTo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CopyTo'], typing.List['CopyTo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'headerBcc':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CopyTo':
                    return super().__getitem__(i)
            
            
            class headerCc(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CopyTo']:
                        return CopyTo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CopyTo'], typing.List['CopyTo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'headerCc':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CopyTo':
                    return super().__getitem__(i)
        
            @staticmethod
            def headerTo() -> typing.Type['To']:
                return To
            headers = schemas.DictSchema
            htmlBody = schemas.StrSchema
            ipID = schemas.Int64Schema
            ipPool = schemas.StrSchema
            localIP = schemas.StrSchema
            messageID = schemas.StrSchema
            preText = schemas.StrSchema
            publicIP = schemas.StrSchema
        
            @staticmethod
            def replyTo() -> typing.Type['ReplyTo']:
                return ReplyTo
            subAccountID = schemas.Int64Schema
            subject = schemas.StrSchema
            submittedAt = schemas.Int64Schema
            textBody = schemas.StrSchema
        
            @staticmethod
            def to() -> typing.Type['To']:
                return To
            trackClicks = schemas.BoolSchema
            trackOpens = schemas.BoolSchema
            __annotations__ = {
                "accountID": accountID,
                "ampBody": ampBody,
                "attachments": attachments,
                "attempt": attempt,
                "customFields": customFields,
                "emailType": emailType,
                "from": _from,
                "groups": groups,
                "headerBcc": headerBcc,
                "headerCc": headerCc,
                "headerTo": headerTo,
                "headers": headers,
                "htmlBody": htmlBody,
                "ipID": ipID,
                "ipPool": ipPool,
                "localIP": localIP,
                "messageID": messageID,
                "preText": preText,
                "publicIP": publicIP,
                "replyTo": replyTo,
                "subAccountID": subAccountID,
                "subject": subject,
                "submittedAt": submittedAt,
                "textBody": textBody,
                "to": to,
                "trackClicks": trackClicks,
                "trackOpens": trackOpens,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountID"]) -> MetaOapg.properties.accountID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ampBody"]) -> MetaOapg.properties.ampBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attempt"]) -> MetaOapg.properties.attempt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFields"]) -> MetaOapg.properties.customFields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailType"]) -> MetaOapg.properties.emailType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> 'ModelFrom': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groups"]) -> MetaOapg.properties.groups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headerBcc"]) -> MetaOapg.properties.headerBcc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headerCc"]) -> MetaOapg.properties.headerCc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headerTo"]) -> 'To': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["headers"]) -> MetaOapg.properties.headers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlBody"]) -> MetaOapg.properties.htmlBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipID"]) -> MetaOapg.properties.ipID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipPool"]) -> MetaOapg.properties.ipPool: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localIP"]) -> MetaOapg.properties.localIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageID"]) -> MetaOapg.properties.messageID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preText"]) -> MetaOapg.properties.preText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicIP"]) -> MetaOapg.properties.publicIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replyTo"]) -> 'ReplyTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subAccountID"]) -> MetaOapg.properties.subAccountID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subject"]) -> MetaOapg.properties.subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submittedAt"]) -> MetaOapg.properties.submittedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["textBody"]) -> MetaOapg.properties.textBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> 'To': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackClicks"]) -> MetaOapg.properties.trackClicks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackOpens"]) -> MetaOapg.properties.trackOpens: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountID", "ampBody", "attachments", "attempt", "customFields", "emailType", "from", "groups", "headerBcc", "headerCc", "headerTo", "headers", "htmlBody", "ipID", "ipPool", "localIP", "messageID", "preText", "publicIP", "replyTo", "subAccountID", "subject", "submittedAt", "textBody", "to", "trackClicks", "trackOpens", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountID"]) -> typing.Union[MetaOapg.properties.accountID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ampBody"]) -> typing.Union[MetaOapg.properties.ampBody, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attempt"]) -> typing.Union[MetaOapg.properties.attempt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFields"]) -> typing.Union[MetaOapg.properties.customFields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailType"]) -> typing.Union[MetaOapg.properties.emailType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union['ModelFrom', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union[MetaOapg.properties.groups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headerBcc"]) -> typing.Union[MetaOapg.properties.headerBcc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headerCc"]) -> typing.Union[MetaOapg.properties.headerCc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headerTo"]) -> typing.Union['To', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["headers"]) -> typing.Union[MetaOapg.properties.headers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlBody"]) -> typing.Union[MetaOapg.properties.htmlBody, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipID"]) -> typing.Union[MetaOapg.properties.ipID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipPool"]) -> typing.Union[MetaOapg.properties.ipPool, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localIP"]) -> typing.Union[MetaOapg.properties.localIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageID"]) -> typing.Union[MetaOapg.properties.messageID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preText"]) -> typing.Union[MetaOapg.properties.preText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicIP"]) -> typing.Union[MetaOapg.properties.publicIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replyTo"]) -> typing.Union['ReplyTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subAccountID"]) -> typing.Union[MetaOapg.properties.subAccountID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subject"]) -> typing.Union[MetaOapg.properties.subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submittedAt"]) -> typing.Union[MetaOapg.properties.submittedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["textBody"]) -> typing.Union[MetaOapg.properties.textBody, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union['To', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackClicks"]) -> typing.Union[MetaOapg.properties.trackClicks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackOpens"]) -> typing.Union[MetaOapg.properties.trackOpens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountID", "ampBody", "attachments", "attempt", "customFields", "emailType", "from", "groups", "headerBcc", "headerCc", "headerTo", "headers", "htmlBody", "ipID", "ipPool", "localIP", "messageID", "preText", "publicIP", "replyTo", "subAccountID", "subject", "submittedAt", "textBody", "to", "trackClicks", "trackOpens", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountID: typing.Union[MetaOapg.properties.accountID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ampBody: typing.Union[MetaOapg.properties.ampBody, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        attempt: typing.Union[MetaOapg.properties.attempt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customFields: typing.Union[MetaOapg.properties.customFields, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        emailType: typing.Union[MetaOapg.properties.emailType, str, schemas.Unset] = schemas.unset,
        groups: typing.Union[MetaOapg.properties.groups, list, tuple, schemas.Unset] = schemas.unset,
        headerBcc: typing.Union[MetaOapg.properties.headerBcc, list, tuple, schemas.Unset] = schemas.unset,
        headerCc: typing.Union[MetaOapg.properties.headerCc, list, tuple, schemas.Unset] = schemas.unset,
        headerTo: typing.Union['To', schemas.Unset] = schemas.unset,
        headers: typing.Union[MetaOapg.properties.headers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        htmlBody: typing.Union[MetaOapg.properties.htmlBody, str, schemas.Unset] = schemas.unset,
        ipID: typing.Union[MetaOapg.properties.ipID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ipPool: typing.Union[MetaOapg.properties.ipPool, str, schemas.Unset] = schemas.unset,
        localIP: typing.Union[MetaOapg.properties.localIP, str, schemas.Unset] = schemas.unset,
        messageID: typing.Union[MetaOapg.properties.messageID, str, schemas.Unset] = schemas.unset,
        preText: typing.Union[MetaOapg.properties.preText, str, schemas.Unset] = schemas.unset,
        publicIP: typing.Union[MetaOapg.properties.publicIP, str, schemas.Unset] = schemas.unset,
        replyTo: typing.Union['ReplyTo', schemas.Unset] = schemas.unset,
        subAccountID: typing.Union[MetaOapg.properties.subAccountID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        subject: typing.Union[MetaOapg.properties.subject, str, schemas.Unset] = schemas.unset,
        submittedAt: typing.Union[MetaOapg.properties.submittedAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        textBody: typing.Union[MetaOapg.properties.textBody, str, schemas.Unset] = schemas.unset,
        to: typing.Union['To', schemas.Unset] = schemas.unset,
        trackClicks: typing.Union[MetaOapg.properties.trackClicks, bool, schemas.Unset] = schemas.unset,
        trackOpens: typing.Union[MetaOapg.properties.trackOpens, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QEmailMessage':
        return super().__new__(
            cls,
            *_args,
            accountID=accountID,
            ampBody=ampBody,
            attachments=attachments,
            attempt=attempt,
            customFields=customFields,
            emailType=emailType,
            groups=groups,
            headerBcc=headerBcc,
            headerCc=headerCc,
            headerTo=headerTo,
            headers=headers,
            htmlBody=htmlBody,
            ipID=ipID,
            ipPool=ipPool,
            localIP=localIP,
            messageID=messageID,
            preText=preText,
            publicIP=publicIP,
            replyTo=replyTo,
            subAccountID=subAccountID,
            subject=subject,
            submittedAt=submittedAt,
            textBody=textBody,
            to=to,
            trackClicks=trackClicks,
            trackOpens=trackOpens,
            _configuration=_configuration,
            **kwargs,
        )

from sendpost_py.model.attachment import Attachment
from sendpost_py.model.copy_to import CopyTo
from sendpost_py.model.model_from import ModelFrom
from sendpost_py.model.reply_to import ReplyTo
from sendpost_py.model.to import To
