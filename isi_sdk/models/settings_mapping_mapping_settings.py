# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class SettingsMappingMappingSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SettingsMappingMappingSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cache_entry_expiry': 'int',
            'gid_range_enabled': 'bool',
            'gid_range_max': 'int',
            'gid_range_min': 'int',
            'gid_range_next': 'int',
            'uid_range_enabled': 'bool',
            'uid_range_max': 'int',
            'uid_range_min': 'int',
            'uid_range_next': 'int'
        }

        self.attribute_map = {
            'cache_entry_expiry': 'cache_entry_expiry',
            'gid_range_enabled': 'gid_range_enabled',
            'gid_range_max': 'gid_range_max',
            'gid_range_min': 'gid_range_min',
            'gid_range_next': 'gid_range_next',
            'uid_range_enabled': 'uid_range_enabled',
            'uid_range_max': 'uid_range_max',
            'uid_range_min': 'uid_range_min',
            'uid_range_next': 'uid_range_next'
        }

        self._cache_entry_expiry = None
        self._gid_range_enabled = None
        self._gid_range_max = None
        self._gid_range_min = None
        self._gid_range_next = None
        self._uid_range_enabled = None
        self._uid_range_max = None
        self._uid_range_min = None
        self._uid_range_next = None

    @property
    def cache_entry_expiry(self):
        """
        Gets the cache_entry_expiry of this SettingsMappingMappingSettings.
        Specifies the cache expiry in seconds of the idmapper.

        :return: The cache_entry_expiry of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._cache_entry_expiry

    @cache_entry_expiry.setter
    def cache_entry_expiry(self, cache_entry_expiry):
        """
        Sets the cache_entry_expiry of this SettingsMappingMappingSettings.
        Specifies the cache expiry in seconds of the idmapper.

        :param cache_entry_expiry: The cache_entry_expiry of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._cache_entry_expiry = cache_entry_expiry

    @property
    def gid_range_enabled(self):
        """
        Gets the gid_range_enabled of this SettingsMappingMappingSettings.
        If true, allocates GIDs from a fixed range.

        :return: The gid_range_enabled of this SettingsMappingMappingSettings.
        :rtype: bool
        """
        return self._gid_range_enabled

    @gid_range_enabled.setter
    def gid_range_enabled(self, gid_range_enabled):
        """
        Sets the gid_range_enabled of this SettingsMappingMappingSettings.
        If true, allocates GIDs from a fixed range.

        :param gid_range_enabled: The gid_range_enabled of this SettingsMappingMappingSettings.
        :type: bool
        """
        
        self._gid_range_enabled = gid_range_enabled

    @property
    def gid_range_max(self):
        """
        Gets the gid_range_max of this SettingsMappingMappingSettings.
        Specifies the ending number for a fixed range from which GIDs are allocated.

        :return: The gid_range_max of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._gid_range_max

    @gid_range_max.setter
    def gid_range_max(self, gid_range_max):
        """
        Sets the gid_range_max of this SettingsMappingMappingSettings.
        Specifies the ending number for a fixed range from which GIDs are allocated.

        :param gid_range_max: The gid_range_max of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._gid_range_max = gid_range_max

    @property
    def gid_range_min(self):
        """
        Gets the gid_range_min of this SettingsMappingMappingSettings.
        Specifies the starting number for a fixed range from which GIDs are allocated.

        :return: The gid_range_min of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._gid_range_min

    @gid_range_min.setter
    def gid_range_min(self, gid_range_min):
        """
        Sets the gid_range_min of this SettingsMappingMappingSettings.
        Specifies the starting number for a fixed range from which GIDs are allocated.

        :param gid_range_min: The gid_range_min of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._gid_range_min = gid_range_min

    @property
    def gid_range_next(self):
        """
        Gets the gid_range_next of this SettingsMappingMappingSettings.
        Specifies the next GID to allocate.

        :return: The gid_range_next of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._gid_range_next

    @gid_range_next.setter
    def gid_range_next(self, gid_range_next):
        """
        Sets the gid_range_next of this SettingsMappingMappingSettings.
        Specifies the next GID to allocate.

        :param gid_range_next: The gid_range_next of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._gid_range_next = gid_range_next

    @property
    def uid_range_enabled(self):
        """
        Gets the uid_range_enabled of this SettingsMappingMappingSettings.
        If true, allocates UIDs from a fixed range.

        :return: The uid_range_enabled of this SettingsMappingMappingSettings.
        :rtype: bool
        """
        return self._uid_range_enabled

    @uid_range_enabled.setter
    def uid_range_enabled(self, uid_range_enabled):
        """
        Sets the uid_range_enabled of this SettingsMappingMappingSettings.
        If true, allocates UIDs from a fixed range.

        :param uid_range_enabled: The uid_range_enabled of this SettingsMappingMappingSettings.
        :type: bool
        """
        
        self._uid_range_enabled = uid_range_enabled

    @property
    def uid_range_max(self):
        """
        Gets the uid_range_max of this SettingsMappingMappingSettings.
        Specifies the ending number for a fixed range from which UIDs are allocated.

        :return: The uid_range_max of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._uid_range_max

    @uid_range_max.setter
    def uid_range_max(self, uid_range_max):
        """
        Sets the uid_range_max of this SettingsMappingMappingSettings.
        Specifies the ending number for a fixed range from which UIDs are allocated.

        :param uid_range_max: The uid_range_max of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._uid_range_max = uid_range_max

    @property
    def uid_range_min(self):
        """
        Gets the uid_range_min of this SettingsMappingMappingSettings.
        Specifies the starting number for a fixed range from which UIDs are allocated.

        :return: The uid_range_min of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._uid_range_min

    @uid_range_min.setter
    def uid_range_min(self, uid_range_min):
        """
        Sets the uid_range_min of this SettingsMappingMappingSettings.
        Specifies the starting number for a fixed range from which UIDs are allocated.

        :param uid_range_min: The uid_range_min of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._uid_range_min = uid_range_min

    @property
    def uid_range_next(self):
        """
        Gets the uid_range_next of this SettingsMappingMappingSettings.
        Specifies the next UID to allocate.

        :return: The uid_range_next of this SettingsMappingMappingSettings.
        :rtype: int
        """
        return self._uid_range_next

    @uid_range_next.setter
    def uid_range_next(self, uid_range_next):
        """
        Sets the uid_range_next of this SettingsMappingMappingSettings.
        Specifies the next UID to allocate.

        :param uid_range_next: The uid_range_next of this SettingsMappingMappingSettings.
        :type: int
        """
        
        self._uid_range_next = uid_range_next

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

