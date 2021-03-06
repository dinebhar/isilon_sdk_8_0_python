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


class EventChannel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventChannel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allowed_nodes': 'list[int]',
            'enabled': 'bool',
            'excluded_nodes': 'list[int]',
            'parameters': 'EventChannelParameters',
            'system': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'allowed_nodes': 'allowed_nodes',
            'enabled': 'enabled',
            'excluded_nodes': 'excluded_nodes',
            'parameters': 'parameters',
            'system': 'system',
            'type': 'type'
        }

        self._allowed_nodes = None
        self._enabled = None
        self._excluded_nodes = None
        self._parameters = None
        self._system = None
        self._type = None

    @property
    def allowed_nodes(self):
        """
        Gets the allowed_nodes of this EventChannel.
        Nodes that can be masters for this channel

        :return: The allowed_nodes of this EventChannel.
        :rtype: list[int]
        """
        return self._allowed_nodes

    @allowed_nodes.setter
    def allowed_nodes(self, allowed_nodes):
        """
        Sets the allowed_nodes of this EventChannel.
        Nodes that can be masters for this channel

        :param allowed_nodes: The allowed_nodes of this EventChannel.
        :type: list[int]
        """
        
        self._allowed_nodes = allowed_nodes

    @property
    def enabled(self):
        """
        Gets the enabled of this EventChannel.
        Channel is to be used or not

        :return: The enabled of this EventChannel.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this EventChannel.
        Channel is to be used or not

        :param enabled: The enabled of this EventChannel.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def excluded_nodes(self):
        """
        Gets the excluded_nodes of this EventChannel.
        Nodes that can be masters for this channel

        :return: The excluded_nodes of this EventChannel.
        :rtype: list[int]
        """
        return self._excluded_nodes

    @excluded_nodes.setter
    def excluded_nodes(self, excluded_nodes):
        """
        Sets the excluded_nodes of this EventChannel.
        Nodes that can be masters for this channel

        :param excluded_nodes: The excluded_nodes of this EventChannel.
        :type: list[int]
        """
        
        self._excluded_nodes = excluded_nodes

    @property
    def parameters(self):
        """
        Gets the parameters of this EventChannel.
        Parameters to be used for an smtp channel

        :return: The parameters of this EventChannel.
        :rtype: EventChannelParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this EventChannel.
        Parameters to be used for an smtp channel

        :param parameters: The parameters of this EventChannel.
        :type: EventChannelParameters
        """
        
        self._parameters = parameters

    @property
    def system(self):
        """
        Gets the system of this EventChannel.
        Channel is a pre-defined system channel

        :return: The system of this EventChannel.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this EventChannel.
        Channel is a pre-defined system channel

        :param system: The system of this EventChannel.
        :type: bool
        """
        
        self._system = system

    @property
    def type(self):
        """
        Gets the type of this EventChannel.
        The mechanism used by the channel

        :return: The type of this EventChannel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EventChannel.
        The mechanism used by the channel

        :param type: The type of this EventChannel.
        :type: str
        """
        allowed_values = ["connectemc", "smtp", "snmp"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )

        self._type = type

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

