# coding: utf-8

"""
HardeningApi.py
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


class HardeningApi(object):
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

    def create_hardening_apply_item(self, hardening_apply_item, **kwargs):
        """
        
        Apply hardening on the cluster.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_hardening_apply_item(hardening_apply_item, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HardeningApplyItem hardening_apply_item:  (required)
        :return: CreateHardeningApplyItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_apply_item']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_apply_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardening_apply_item' is set
        if ('hardening_apply_item' not in params) or (params['hardening_apply_item'] is None):
            raise ValueError("Missing the required parameter `hardening_apply_item` when calling `create_hardening_apply_item`")


        resource_path = '/platform/3/hardening/apply'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_apply_item' in params:
            body_params = params['hardening_apply_item']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateHardeningApplyItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_hardening_resolve_item(self, hardening_resolve_item, **kwargs):
        """
        
        Resolve issues related to hardening, found in current cluster configuration.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_hardening_resolve_item(hardening_resolve_item, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HardeningResolveItem hardening_resolve_item:  (required)
        :param bool accept: If true, execution proceeds to resolve all issues. If false, executrion aborts. This is a required argument.
        :return: CreateHardeningResolveItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_resolve_item', 'accept']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_resolve_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardening_resolve_item' is set
        if ('hardening_resolve_item' not in params) or (params['hardening_resolve_item'] is None):
            raise ValueError("Missing the required parameter `hardening_resolve_item` when calling `create_hardening_resolve_item`")


        resource_path = '/platform/3/hardening/resolve'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'accept' in params:
            query_params['accept'] = params['accept']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_resolve_item' in params:
            body_params = params['hardening_resolve_item']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateHardeningResolveItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_hardening_revert_item(self, hardening_revert_item, **kwargs):
        """
        
        Revert hardening on the cluster.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_hardening_revert_item(hardening_revert_item, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Empty hardening_revert_item:  (required)
        :param bool force: If specified, revert operation continues even in case of a failure. Default is false in which case revert stops at the first failure.
        :return: CreateHardeningRevertItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardening_revert_item', 'force']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardening_revert_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardening_revert_item' is set
        if ('hardening_revert_item' not in params) or (params['hardening_revert_item'] is None):
            raise ValueError("Missing the required parameter `hardening_revert_item` when calling `create_hardening_revert_item`")


        resource_path = '/platform/3/hardening/revert'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'force' in params:
            query_params['force'] = params['force']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hardening_revert_item' in params:
            body_params = params['hardening_revert_item']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateHardeningRevertItemResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_hardening_state(self, **kwargs):
        """
        
        Get the state of the current hardening operation, if one is happening.  Note that this is different from the /status resource, which returns the overall hardening status of the cluster.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hardening_state(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HardeningState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardening_state" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/platform/3/hardening/state'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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
                                            response_type='HardeningState',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_hardening_status(self, **kwargs):
        """
        
        Get a message indicating whether or not the cluster is hardened. Note that this is different from the /state resource, which returns the state of a specific hardening operation (apply or revert).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hardening_status(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HardeningStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardening_status" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/platform/3/hardening/status'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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
                                            response_type='HardeningStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
