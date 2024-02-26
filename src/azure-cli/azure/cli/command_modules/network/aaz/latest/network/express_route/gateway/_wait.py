# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route gateway wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutegateways/{}", "2023-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="ExpressRoute gateway name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteGatewaysGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class ExpressRouteGatewaysGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "expressRouteGatewayName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.allow_non_virtual_wan_traffic = AAZBoolType(
                serialized_name="allowNonVirtualWanTraffic",
            )
            properties.auto_scale_configuration = AAZObjectType(
                serialized_name="autoScaleConfiguration",
            )
            properties.express_route_connections = AAZListType(
                serialized_name="expressRouteConnections",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.virtual_hub = AAZObjectType(
                serialized_name="virtualHub",
                flags={"required": True},
            )

            auto_scale_configuration = cls._schema_on_200.properties.auto_scale_configuration
            auto_scale_configuration.bounds = AAZObjectType()

            bounds = cls._schema_on_200.properties.auto_scale_configuration.bounds
            bounds.max = AAZIntType()
            bounds.min = AAZIntType()

            express_route_connections = cls._schema_on_200.properties.express_route_connections
            express_route_connections.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.express_route_connections.Element
            _element.id = AAZStrType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.properties.express_route_connections.Element.properties
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.enable_internet_security = AAZBoolType(
                serialized_name="enableInternetSecurity",
            )
            properties.enable_private_link_fast_path = AAZBoolType(
                serialized_name="enablePrivateLinkFastPath",
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
                flags={"required": True},
            )
            properties.express_route_gateway_bypass = AAZBoolType(
                serialized_name="expressRouteGatewayBypass",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.routing_configuration = AAZObjectType(
                serialized_name="routingConfiguration",
            )
            properties.routing_weight = AAZIntType(
                serialized_name="routingWeight",
            )

            express_route_circuit_peering = cls._schema_on_200.properties.express_route_connections.Element.properties.express_route_circuit_peering
            express_route_circuit_peering.id = AAZStrType()

            routing_configuration = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration
            routing_configuration.associated_route_table = AAZObjectType(
                serialized_name="associatedRouteTable",
            )
            _WaitHelper._build_schema_sub_resource_read(routing_configuration.associated_route_table)
            routing_configuration.inbound_route_map = AAZObjectType(
                serialized_name="inboundRouteMap",
            )
            _WaitHelper._build_schema_sub_resource_read(routing_configuration.inbound_route_map)
            routing_configuration.outbound_route_map = AAZObjectType(
                serialized_name="outboundRouteMap",
            )
            _WaitHelper._build_schema_sub_resource_read(routing_configuration.outbound_route_map)
            routing_configuration.propagated_route_tables = AAZObjectType(
                serialized_name="propagatedRouteTables",
            )
            routing_configuration.vnet_routes = AAZObjectType(
                serialized_name="vnetRoutes",
            )

            propagated_route_tables = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables
            propagated_route_tables.ids = AAZListType()
            propagated_route_tables.labels = AAZListType()

            ids = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables.ids
            ids.Element = AAZObjectType()
            _WaitHelper._build_schema_sub_resource_read(ids.Element)

            labels = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.propagated_route_tables.labels
            labels.Element = AAZStrType()

            vnet_routes = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes
            vnet_routes.bgp_connections = AAZListType(
                serialized_name="bgpConnections",
                flags={"read_only": True},
            )
            vnet_routes.static_routes = AAZListType(
                serialized_name="staticRoutes",
            )
            vnet_routes.static_routes_config = AAZObjectType(
                serialized_name="staticRoutesConfig",
            )

            bgp_connections = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.bgp_connections
            bgp_connections.Element = AAZObjectType()
            _WaitHelper._build_schema_sub_resource_read(bgp_connections.Element)

            static_routes = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes
            static_routes.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes.Element
            _element.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )
            _element.name = AAZStrType()
            _element.next_hop_ip_address = AAZStrType(
                serialized_name="nextHopIpAddress",
            )

            address_prefixes = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes.Element.address_prefixes
            address_prefixes.Element = AAZStrType()

            static_routes_config = cls._schema_on_200.properties.express_route_connections.Element.properties.routing_configuration.vnet_routes.static_routes_config
            static_routes_config.propagate_static_routes = AAZBoolType(
                serialized_name="propagateStaticRoutes",
                flags={"read_only": True},
            )
            static_routes_config.vnet_local_route_override_criteria = AAZStrType(
                serialized_name="vnetLocalRouteOverrideCriteria",
            )

            virtual_hub = cls._schema_on_200.properties.virtual_hub
            virtual_hub.id = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Wait"]
