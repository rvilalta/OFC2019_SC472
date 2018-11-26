# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import connectionServiceWithNotif_pb2 as connectionServiceWithNotif__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ConnectionServiceWithNotifStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateConnection = channel.unary_unary(
        '/connection.ConnectionServiceWithNotif/CreateConnection',
        request_serializer=connectionServiceWithNotif__pb2.Connection.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListConnection = channel.unary_unary(
        '/connection.ConnectionServiceWithNotif/ListConnection',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=connectionServiceWithNotif__pb2.ConnectionList.FromString,
        )
    self.GetBer = channel.unary_stream(
        '/connection.ConnectionServiceWithNotif/GetBer',
        request_serializer=connectionServiceWithNotif__pb2.Connection.SerializeToString,
        response_deserializer=connectionServiceWithNotif__pb2.Ber.FromString,
        )


class ConnectionServiceWithNotifServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateConnection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListConnection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConnectionServiceWithNotifServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateConnection': grpc.unary_unary_rpc_method_handler(
          servicer.CreateConnection,
          request_deserializer=connectionServiceWithNotif__pb2.Connection.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListConnection': grpc.unary_unary_rpc_method_handler(
          servicer.ListConnection,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=connectionServiceWithNotif__pb2.ConnectionList.SerializeToString,
      ),
      'GetBer': grpc.unary_stream_rpc_method_handler(
          servicer.GetBer,
          request_deserializer=connectionServiceWithNotif__pb2.Connection.FromString,
          response_serializer=connectionServiceWithNotif__pb2.Ber.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'connection.ConnectionServiceWithNotif', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
