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


class StatisticsKey(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatisticsKey - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aggregation_type': 'str',
            'base_name': 'str',
            'default_cache_time': 'int',
            'description': 'str',
            'key': 'str',
            'policies': 'list[StatisticsKeyPolicy]',
            'policy_cache_time': 'int',
            'real_name': 'str',
            'scope': 'str',
            'type': 'str',
            'units': 'str'
        }

        self.attribute_map = {
            'aggregation_type': 'aggregation_type',
            'base_name': 'base_name',
            'default_cache_time': 'default_cache_time',
            'description': 'description',
            'key': 'key',
            'policies': 'policies',
            'policy_cache_time': 'policy_cache_time',
            'real_name': 'real_name',
            'scope': 'scope',
            'type': 'type',
            'units': 'units'
        }

        self._aggregation_type = None
        self._base_name = None
        self._default_cache_time = None
        self._description = None
        self._key = None
        self._policies = None
        self._policy_cache_time = None
        self._real_name = None
        self._scope = None
        self._type = None
        self._units = None

    @property
    def aggregation_type(self):
        """
        Gets the aggregation_type of this StatisticsKey.
        Type of aggregation used in down-sampling.

        :return: The aggregation_type of this StatisticsKey.
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """
        Sets the aggregation_type of this StatisticsKey.
        Type of aggregation used in down-sampling.

        :param aggregation_type: The aggregation_type of this StatisticsKey.
        :type: str
        """
        allowed_values = ["last", "min", "max", "avg", "sum", "custom"]
        if aggregation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def base_name(self):
        """
        Gets the base_name of this StatisticsKey.
        Name of key this keys is derived from, if any.

        :return: The base_name of this StatisticsKey.
        :rtype: str
        """
        return self._base_name

    @base_name.setter
    def base_name(self, base_name):
        """
        Sets the base_name of this StatisticsKey.
        Name of key this keys is derived from, if any.

        :param base_name: The base_name of this StatisticsKey.
        :type: str
        """
        
        self._base_name = base_name

    @property
    def default_cache_time(self):
        """
        Gets the default_cache_time of this StatisticsKey.
        Default time in seconds system will used cached values.

        :return: The default_cache_time of this StatisticsKey.
        :rtype: int
        """
        return self._default_cache_time

    @default_cache_time.setter
    def default_cache_time(self, default_cache_time):
        """
        Sets the default_cache_time of this StatisticsKey.
        Default time in seconds system will used cached values.

        :param default_cache_time: The default_cache_time of this StatisticsKey.
        :type: int
        """
        
        self._default_cache_time = default_cache_time

    @property
    def description(self):
        """
        Gets the description of this StatisticsKey.
        Description of statistics key.

        :return: The description of this StatisticsKey.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StatisticsKey.
        Description of statistics key.

        :param description: The description of this StatisticsKey.
        :type: str
        """
        
        self._description = description

    @property
    def key(self):
        """
        Gets the key of this StatisticsKey.
        Key name.

        :return: The key of this StatisticsKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this StatisticsKey.
        Key name.

        :param key: The key of this StatisticsKey.
        :type: str
        """
        
        self._key = key

    @property
    def policies(self):
        """
        Gets the policies of this StatisticsKey.
        List of effective history policies for key.

        :return: The policies of this StatisticsKey.
        :rtype: list[StatisticsKeyPolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this StatisticsKey.
        List of effective history policies for key.

        :param policies: The policies of this StatisticsKey.
        :type: list[StatisticsKeyPolicy]
        """
        
        self._policies = policies

    @property
    def policy_cache_time(self):
        """
        Gets the policy_cache_time of this StatisticsKey.
        Configured time in seconds system will used cached values.

        :return: The policy_cache_time of this StatisticsKey.
        :rtype: int
        """
        return self._policy_cache_time

    @policy_cache_time.setter
    def policy_cache_time(self, policy_cache_time):
        """
        Sets the policy_cache_time of this StatisticsKey.
        Configured time in seconds system will used cached values.

        :param policy_cache_time: The policy_cache_time of this StatisticsKey.
        :type: int
        """
        
        self._policy_cache_time = policy_cache_time

    @property
    def real_name(self):
        """
        Gets the real_name of this StatisticsKey.
        Name of real key if this is an alias.

        :return: The real_name of this StatisticsKey.
        :rtype: str
        """
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        """
        Sets the real_name of this StatisticsKey.
        Name of real key if this is an alias.

        :param real_name: The real_name of this StatisticsKey.
        :type: str
        """
        
        self._real_name = real_name

    @property
    def scope(self):
        """
        Gets the scope of this StatisticsKey.
        Scope of key.

        :return: The scope of this StatisticsKey.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this StatisticsKey.
        Scope of key.

        :param scope: The scope of this StatisticsKey.
        :type: str
        """
        allowed_values = ["cluster", "node"]
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope`, must be one of {0}"
                .format(allowed_values)
            )

        self._scope = scope

    @property
    def type(self):
        """
        Gets the type of this StatisticsKey.
        Data type of key values.

        :return: The type of this StatisticsKey.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StatisticsKey.
        Data type of key values.

        :param type: The type of this StatisticsKey.
        :type: str
        """
        
        self._type = type

    @property
    def units(self):
        """
        Gets the units of this StatisticsKey.
        Units of key values.

        :return: The units of this StatisticsKey.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this StatisticsKey.
        Units of key values.

        :param units: The units of this StatisticsKey.
        :type: str
        """
        
        self._units = units

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

