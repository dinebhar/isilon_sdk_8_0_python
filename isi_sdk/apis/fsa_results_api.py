# coding: utf-8

"""
FsaResultsApi.py
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


class FsaResultsApi(object):
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

    def get_result_histogram(self, id, **kwargs):
        """
        
        This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_histogram(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: ResultHistogram
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_histogram" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_histogram`")


        resource_path = '/platform/3/fsa/results/{Id}/histogram'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']

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
                                            response_type='ResultHistogram',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_result_histogram_stat(self, result_histogram_stat, id, **kwargs):
        """
        
        This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_histogram_stat(result_histogram_stat, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str result_histogram_stat: This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID. (required)
        :param str id:  (required)
        :param str directory_filter: Filter according to a specific directory, which includes all of its subdirectories.
        :param str attribute_filter: Filter according to the name of a file user attribute.
        :param str node_pool_filter: Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class.
        :param str disk_pool_filter: Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain.
        :param str tier_filter: Filter according to the name of a storage tier, which is a user-created set of node pools.
        :param int comp_report: Result set identifier for comparison of database results.
        :param int log_size_filter: Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values.
        :param int phys_size_filter: Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values.
        :param str path_ext_filter: Filter according to the name of a single file extension.
        :param int ctime_filter: Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values.
        :param int atime_filter: Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values.
        :return: ResultHistogram
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['result_histogram_stat', 'id', 'directory_filter', 'attribute_filter', 'node_pool_filter', 'disk_pool_filter', 'tier_filter', 'comp_report', 'log_size_filter', 'phys_size_filter', 'path_ext_filter', 'ctime_filter', 'atime_filter']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_histogram_stat" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'result_histogram_stat' is set
        if ('result_histogram_stat' not in params) or (params['result_histogram_stat'] is None):
            raise ValueError("Missing the required parameter `result_histogram_stat` when calling `get_result_histogram_stat`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_histogram_stat`")


        resource_path = '/platform/3/fsa/results/{Id}/histogram/{ResultHistogramStat}'.replace('{format}', 'json')
        path_params = {}
        if 'result_histogram_stat' in params:
            path_params['ResultHistogramStat'] = params['result_histogram_stat']
        if 'id' in params:
            path_params['Id'] = params['id']

        query_params = {}
        if 'directory_filter' in params:
            query_params['directory_filter'] = params['directory_filter']
        if 'attribute_filter' in params:
            query_params['attribute_filter'] = params['attribute_filter']
        if 'node_pool_filter' in params:
            query_params['node_pool_filter'] = params['node_pool_filter']
        if 'disk_pool_filter' in params:
            query_params['disk_pool_filter'] = params['disk_pool_filter']
        if 'tier_filter' in params:
            query_params['tier_filter'] = params['tier_filter']
        if 'comp_report' in params:
            query_params['comp_report'] = params['comp_report']
        if 'log_size_filter' in params:
            query_params['log_size_filter'] = params['log_size_filter']
        if 'phys_size_filter' in params:
            query_params['phys_size_filter'] = params['phys_size_filter']
        if 'path_ext_filter' in params:
            query_params['path_ext_filter'] = params['path_ext_filter']
        if 'ctime_filter' in params:
            query_params['ctime_filter'] = params['ctime_filter']
        if 'atime_filter' in params:
            query_params['atime_filter'] = params['atime_filter']

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
                                            response_type='ResultHistogram',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_result_top_dir(self, result_top_dir_id, id, **kwargs):
        """
        
        This resource retrieves the top directories. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_top_dir(result_top_dir_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str result_top_dir_id: This resource retrieves the top directories. ID in the resource path is the result set ID. (required)
        :param str id:  (required)
        :param str sort: The field that will be used for sorting.
        :param int start: Starting index for results. Default value of 0.
        :param int limit: Number of results from start index. Default value of 1000.
        :param int comp_report: Result set identifier for comparison of database results.
        :param str dir: The direction of the sort.
        :return: ResultTopDirs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['result_top_dir_id', 'id', 'sort', 'start', 'limit', 'comp_report', 'dir']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_top_dir" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'result_top_dir_id' is set
        if ('result_top_dir_id' not in params) or (params['result_top_dir_id'] is None):
            raise ValueError("Missing the required parameter `result_top_dir_id` when calling `get_result_top_dir`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_top_dir`")


        resource_path = '/platform/3/fsa/results/{Id}/top-dirs/{ResultTopDirId}'.replace('{format}', 'json')
        path_params = {}
        if 'result_top_dir_id' in params:
            path_params['ResultTopDirId'] = params['result_top_dir_id']
        if 'id' in params:
            path_params['Id'] = params['id']

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'comp_report' in params:
            query_params['comp_report'] = params['comp_report']
        if 'dir' in params:
            query_params['dir'] = params['dir']

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
                                            response_type='ResultTopDirs',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_result_top_dirs(self, id, **kwargs):
        """
        
        This resource retrieves the top directories. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_top_dirs(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: ResultTopDirs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_top_dirs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_top_dirs`")


        resource_path = '/platform/3/fsa/results/{Id}/top-dirs'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']

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
                                            response_type='ResultTopDirs',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_result_top_file(self, result_top_file_id, id, **kwargs):
        """
        
        This resource retrieves the top files. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_top_file(result_top_file_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str result_top_file_id: This resource retrieves the top files. ID in the resource path is the result set ID. (required)
        :param str id:  (required)
        :param str sort: The field that will be used for sorting.
        :param int start: Starting index for results. Default value of 0.
        :param int limit: Number of results from start index. Default value of 1000.
        :param int comp_report: Result set identifier for comparison of database results.
        :param str dir: The direction of the sort.
        :return: ResultTopFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['result_top_file_id', 'id', 'sort', 'start', 'limit', 'comp_report', 'dir']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_top_file" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'result_top_file_id' is set
        if ('result_top_file_id' not in params) or (params['result_top_file_id'] is None):
            raise ValueError("Missing the required parameter `result_top_file_id` when calling `get_result_top_file`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_top_file`")


        resource_path = '/platform/3/fsa/results/{Id}/top-files/{ResultTopFileId}'.replace('{format}', 'json')
        path_params = {}
        if 'result_top_file_id' in params:
            path_params['ResultTopFileId'] = params['result_top_file_id']
        if 'id' in params:
            path_params['Id'] = params['id']

        query_params = {}
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'comp_report' in params:
            query_params['comp_report'] = params['comp_report']
        if 'dir' in params:
            query_params['dir'] = params['dir']

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
                                            response_type='ResultTopFiles',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_result_top_files(self, id, **kwargs):
        """
        
        This resource retrieves the top files. ID in the resource path is the result set ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_result_top_files(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: ResultTopFiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_result_top_files" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_result_top_files`")


        resource_path = '/platform/3/fsa/results/{Id}/top-files'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']

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
                                            response_type='ResultTopFiles',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
