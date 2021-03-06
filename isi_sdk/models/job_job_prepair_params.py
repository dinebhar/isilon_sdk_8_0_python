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


class JobJobPrepairParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobJobPrepairParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mapping_type': 'str',
            'mode': 'str',
            'template': 'str',
            'zone': 'str'
        }

        self.attribute_map = {
            'mapping_type': 'mapping_type',
            'mode': 'mode',
            'template': 'template',
            'zone': 'zone'
        }

        self._mapping_type = None
        self._mode = None
        self._template = None
        self._zone = None

    @property
    def mapping_type(self):
        """
        Gets the mapping_type of this JobJobPrepairParams.
        Type of permissions; not accepted with mode=clone or mode=inherit.

        :return: The mapping_type of this JobJobPrepairParams.
        :rtype: str
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, mapping_type):
        """
        Sets the mapping_type of this JobJobPrepairParams.
        Type of permissions; not accepted with mode=clone or mode=inherit.

        :param mapping_type: The mapping_type of this JobJobPrepairParams.
        :type: str
        """
        allowed_values = ["global", "sid", "unix", "native"]
        if mapping_type is not None and mapping_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mapping_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._mapping_type = mapping_type

    @property
    def mode(self):
        """
        Gets the mode of this JobJobPrepairParams.
        Type of PermissionRepair operation.

        :return: The mode of this JobJobPrepairParams.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this JobJobPrepairParams.
        Type of PermissionRepair operation.

        :param mode: The mode of this JobJobPrepairParams.
        :type: str
        """
        allowed_values = ["clone", "inherit", "convert"]
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._mode = mode

    @property
    def template(self):
        """
        Gets the template of this JobJobPrepairParams.
        IFS file or directory to use as a template; required with mode=clone and mode=inherit, not accepted with mode=convert.

        :return: The template of this JobJobPrepairParams.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this JobJobPrepairParams.
        IFS file or directory to use as a template; required with mode=clone and mode=inherit, not accepted with mode=convert.

        :param template: The template of this JobJobPrepairParams.
        :type: str
        """
        
        self._template = template

    @property
    def zone(self):
        """
        Gets the zone of this JobJobPrepairParams.
        Authentication zone; not accepted with mode=clone or mode=inherit.

        :return: The zone of this JobJobPrepairParams.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this JobJobPrepairParams.
        Authentication zone; not accepted with mode=clone or mode=inherit.

        :param zone: The zone of this JobJobPrepairParams.
        :type: str
        """
        
        self._zone = zone

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

