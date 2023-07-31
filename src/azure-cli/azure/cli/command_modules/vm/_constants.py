# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#
# Generation mode: Incremental
# --------------------------------------------------------------------------

UPGRADE_SECURITY_HINT = 'Consider upgrading security for your workloads using Azure Trusted Launch VMs. ' \
                        'To know more about Trusted Launch, please visit ' \
                        'https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch.'

TLAD_DEFAULT_CHANGE_MSG = 'Ignite (November) 2023 onwards "{}" command will deploy Gen2-Trusted ' \
                          'Launch VM by default. To know more about the default change and Trusted Launch, ' \
                          'please visit https://aka.ms/TLaD'

# The `Standard` is used for backward compatibility to allow customers to keep their current behavior
# after changing the default values of `security_type` to Trusted Launch VMs in the future.
COMPATIBLE_SECURITY_TYPE_VALUE = 'Standard'