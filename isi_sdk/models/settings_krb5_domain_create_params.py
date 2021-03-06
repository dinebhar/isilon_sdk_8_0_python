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


class SettingsKrb5DomainCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SettingsKrb5DomainCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'realm': 'str',
            'domain': 'str'
        }

        self.attribute_map = {
            'realm': 'realm',
            'domain': 'domain'
        }

        self._realm = None
        self._domain = None

    @property
    def realm(self):
        """
        Gets the realm of this SettingsKrb5DomainCreateParams.
        Specifies the name of the realm.

        :return: The realm of this SettingsKrb5DomainCreateParams.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """
        Sets the realm of this SettingsKrb5DomainCreateParams.
        Specifies the name of the realm.

        :param realm: The realm of this SettingsKrb5DomainCreateParams.
        :type: str
        """
        
        self._realm = realm

    @property
    def domain(self):
        """
        Gets the domain of this SettingsKrb5DomainCreateParams.
        Specifies the name of the domain.

        :return: The domain of this SettingsKrb5DomainCreateParams.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this SettingsKrb5DomainCreateParams.
        Specifies the name of the domain.

        :param domain: The domain of this SettingsKrb5DomainCreateParams.
        :type: str
        """
        
        self._domain = domain

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

