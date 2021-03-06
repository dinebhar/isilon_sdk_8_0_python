# coding: utf-8

"""
UpgradeClusterApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UpgradeClusterApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_nodes_node_firmware_status(self, lnn, **kwargs):
        """
        
        The firmware status for the node.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_nodes_node_firmware_status(lnn, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int lnn:  (required)
        :param bool devices: Show devices. If false, this returns an empty list. Default is false.
        :param bool package: Show package. If false, this returns an empty list.Default is false.
        :return: NodesNodeFirmwareStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lnn', 'devices', 'package']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_nodes_node_firmware_status" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'lnn' is set
        if ('lnn' not in params) or (params['lnn'] is None):
            raise ValueError("Missing the required parameter `lnn` when calling `get_nodes_node_firmware_status`")


        resource_path = '/platform/3/upgrade/cluster/nodes/{Lnn}/firmware/status'.replace('{format}', 'json')
        path_params = {}
        if 'lnn' in params:
            path_params['Lnn'] = params['lnn']

        query_params = {}
        if 'devices' in params:
            query_params['devices'] = params['devices']
        if 'package' in params:
            query_params['package'] = params['package']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='NodesNodeFirmwareStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
