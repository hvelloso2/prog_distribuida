# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from grpc_services import alerta_pb2 as alerta__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in alerta_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AlertaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VerificarTemperatura = channel.unary_unary(
                '/alerta.AlertaService/VerificarTemperatura',
                request_serializer=alerta__pb2.DadoSensor.SerializeToString,
                response_deserializer=alerta__pb2.RespostaAlerta.FromString,
                _registered_method=True)


class AlertaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VerificarTemperatura(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AlertaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VerificarTemperatura': grpc.unary_unary_rpc_method_handler(
                    servicer.VerificarTemperatura,
                    request_deserializer=alerta__pb2.DadoSensor.FromString,
                    response_serializer=alerta__pb2.RespostaAlerta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'alerta.AlertaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('alerta.AlertaService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AlertaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VerificarTemperatura(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/alerta.AlertaService/VerificarTemperatura',
            alerta__pb2.DadoSensor.SerializeToString,
            alerta__pb2.RespostaAlerta.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
