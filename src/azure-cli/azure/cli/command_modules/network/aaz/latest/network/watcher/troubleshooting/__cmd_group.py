# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network watcher troubleshooting",
)
class __CMDGroup(AAZCommandGroup):
    """Manage Network Watcher troubleshooting sessions.

    For more information on configuring troubleshooting visit https://docs.microsoft.com/azure/network-watcher/network-watcher-troubleshoot-manage-cli.
    """
    pass


__all__ = ["__CMDGroup"]