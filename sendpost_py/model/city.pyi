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


class City(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            cityID = schemas.Int32Schema
            continentCode = schemas.StrSchema
            countryCode = schemas.StrSchema
            postalCode = schemas.StrSchema
            timeZone = schemas.StrSchema
            __annotations__ = {
                "cityID": cityID,
                "continentCode": continentCode,
                "countryCode": countryCode,
                "postalCode": postalCode,
                "timeZone": timeZone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cityID"]) -> MetaOapg.properties.cityID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["continentCode"]) -> MetaOapg.properties.continentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeZone"]) -> MetaOapg.properties.timeZone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cityID", "continentCode", "countryCode", "postalCode", "timeZone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cityID"]) -> typing.Union[MetaOapg.properties.cityID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["continentCode"]) -> typing.Union[MetaOapg.properties.continentCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> typing.Union[MetaOapg.properties.countryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeZone"]) -> typing.Union[MetaOapg.properties.timeZone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cityID", "continentCode", "countryCode", "postalCode", "timeZone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cityID: typing.Union[MetaOapg.properties.cityID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        continentCode: typing.Union[MetaOapg.properties.continentCode, str, schemas.Unset] = schemas.unset,
        countryCode: typing.Union[MetaOapg.properties.countryCode, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        timeZone: typing.Union[MetaOapg.properties.timeZone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'City':
        return super().__new__(
            cls,
            *_args,
            cityID=cityID,
            continentCode=continentCode,
            countryCode=countryCode,
            postalCode=postalCode,
            timeZone=timeZone,
            _configuration=_configuration,
            **kwargs,
        )
