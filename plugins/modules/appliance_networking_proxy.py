#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: appliance_networking_proxy
short_description: Tests a proxy configuration by testing the connection to the proxy
  server and test host.
description: Tests a proxy configuration by testing the connection to the proxy server
  and test host.
options:
  config:
    description:
    - Proxy configuration for the specific protocol. Required with I(state=['test'])
    - 'Valid attributes are:'
    - ' - C(server) (str): URL of the proxy server'
    - ' - C(port) (int): Port to connect to the proxy server. In a ''get'' call, indicates
      the port connected to the proxy server. In a ''set'' call, specifies the port
      to connect to the proxy server. A value of -1 indicates the default port.'
    - ' - C(username) (str): Username for proxy server.'
    - ' - C(password) (str): Password for proxy server.'
    - ' - C(enabled) (bool): In the result of the {@name #get} and {@name #list} {@term
      operations} this field indicates whether proxying is enabled for a particular
      protocol. In the input to the {@name test} and {@name set} {@term operations}
      this field specifies whether proxying should be enabled for a particular protocol.'
    type: dict
  enabled:
    description:
    - 'In the result of the {@name #get} and {@name #list} {@term operations} this
      field indicates whether proxying is enabled for a particular protocol. In the
      input to the {@name test} and {@name set} {@term operations} this field specifies
      whether proxying should be enabled for a particular protocol. Required with
      I(state=[''set''])'
    type: bool
  host:
    description:
    - A hostname, IPv4 or Ipv6 address. Required with I(state=['test'])
    type: str
  password:
    description:
    - Password for proxy server.
    type: str
  port:
    description:
    - Port to connect to the proxy server. In a 'get' call, indicates the port connected
      to the proxy server. In a 'set' call, specifies the port to connect to the proxy
      server. A value of -1 indicates the default port. Required with I(state=['set'])
    type: int
  protocol:
    description:
    - The protocol for which proxy should be set. This parameter is mandatory.
    required: true
    type: str
  server:
    description:
    - URL of the proxy server Required with I(state=['set'])
    type: str
  state:
    choices:
    - absent
    - set
    - test
    default: set
    description: []
    type: str
  username:
    description:
    - Username for proxy server.
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = r"""
- name: Delete the HTTP proxy configuration
  vmware.vmware_rest.appliance_networking_proxy:
    config: {}
    protocol: http
    state: absent
  register: result
- name: Set the HTTP proxy configuration
  vmware.vmware_rest.appliance_networking_proxy:
    config:
      enabled: true
      server: https://www.google.com
      port: 443
    protocol: http
  register: result
- name: Set the HTTP proxy configuration (again)
  vmware.vmware_rest.appliance_networking_proxy:
    config:
      enabled: true
      server: https://www.google.com
      port: 443
    protocol: http
  register: result
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Set the HTTP proxy configuration (again)
value:
  description: Set the HTTP proxy configuration (again)
  returned: On success
  sample:
    enabled: 0
    port: -1
    server: ''
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {"query": {}, "body": {}, "path": {}},
    "set": {
        "query": {},
        "body": {
            "enabled": "enabled",
            "password": "password",
            "port": "port",
            "server": "server",
            "username": "username",
        },
        "path": {"protocol": "protocol"},
    },
    "get": {"query": {}, "body": {}, "path": {"protocol": "protocol"}},
    "delete": {"query": {}, "body": {}, "path": {"protocol": "protocol"}},
    "test": {
        "query": {},
        "body": {"config": "config", "host": "host"},
        "path": {"protocol": "protocol"},
    },
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
    }

    argument_spec["config"] = {"type": "dict"}
    argument_spec["enabled"] = {"type": "bool"}
    argument_spec["host"] = {"type": "str"}
    argument_spec["password"] = {"no_log": True, "type": "str"}
    argument_spec["port"] = {"type": "int"}
    argument_spec["protocol"] = {"required": True, "type": "str"}
    argument_spec["server"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "set", "test"],
        "default": "set",
    }
    argument_spec["username"] = {"no_log": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/appliance/networking/proxy").format(
        **params
    )


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/api/appliance/networking/proxy/{protocol}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/api/appliance/networking/proxy/{protocol}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _set(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["set"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["set"])
    subdevice_type = get_subdevice_type("/api/appliance/networking/proxy/{protocol}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/api/appliance/networking/proxy/{protocol}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.get(_url, json=payload) as resp:
        before = await resp.json()

    async with session.put(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        # The PUT answer does not let us know if the resource has actually been
        # modified
        async with session.get(_url, json=payload) as resp_get:
            after = await resp_get.json()
            if before == after:
                return await update_changed_flag(after, resp_get.status, "get")
        return await update_changed_flag(_json, resp.status, "set")


async def _test(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["test"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["test"])
    subdevice_type = get_subdevice_type(
        "/api/appliance/networking/proxy/{protocol}?action=test"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/appliance/networking/proxy/{protocol}?action=test"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "test")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
