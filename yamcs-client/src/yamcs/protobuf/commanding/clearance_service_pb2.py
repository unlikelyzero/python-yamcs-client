# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/commanding/clearance_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.protobuf.mdb import mdb_pb2 as yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/commanding/clearance_service.proto',
  package='yamcs.protobuf.commanding',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\025ClearanceServiceProtoP\001'),
  serialized_pb=_b('\n1yamcs/protobuf/commanding/clearance_service.proto\x12\x19yamcs.protobuf.commanding\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a\x1cyamcs/protobuf/mdb/mdb.proto\"V\n\x16ListClearancesResponse\x12<\n\nclearances\x18\x01 \x03(\x0b\x32(.yamcs.protobuf.commanding.ClearanceInfo\"\xcb\x01\n\rClearanceInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12I\n\x05level\x18\x02 \x01(\x0e\x32:.yamcs.protobuf.mdb.SignificanceInfo.SignificanceLevelType\x12\x10\n\x08issuedBy\x18\x03 \x01(\t\x12-\n\tissueTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x14hasCommandPrivileges\x18\x05 \x01(\x08\"u\n\x16UpdateClearanceRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12I\n\x05level\x18\x02 \x01(\x0e\x32:.yamcs.protobuf.mdb.SignificanceInfo.SignificanceLevelType\"*\n\x16\x44\x65leteClearanceRequest\x12\x10\n\x08username\x18\x01 \x01(\t2\xdc\x04\n\x0c\x43learanceApi\x12r\n\x0eListClearances\x12\x16.google.protobuf.Empty\x1a\x31.yamcs.protobuf.commanding.ListClearancesResponse\"\x15\x8a\x92\x03\x11\n\x0f/api/clearances\x12\xc1\x01\n\x0fUpdateClearance\x12\x31.yamcs.protobuf.commanding.UpdateClearanceRequest\x1a(.yamcs.protobuf.commanding.ClearanceInfo\"Q\x8a\x92\x03M*\x1a/api/clearances/{username}:\x01*b,Clearance of \'{username}\' changed to {level}\x12\xa8\x01\n\x0f\x44\x65leteClearance\x12\x31.yamcs.protobuf.commanding.DeleteClearanceRequest\x1a\x16.google.protobuf.Empty\"J\x8a\x92\x03\x46\"\x1a/api/clearances/{username}b(Clearance revoked from user \'{username}\'\x12i\n\x12SubscribeClearance\x12\x16.google.protobuf.Empty\x1a(.yamcs.protobuf.commanding.ClearanceInfo\"\x0f\xda\x92\x03\x0b\n\tclearance0\x01\x42-\n\x12org.yamcs.protobufB\x15\x43learanceServiceProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2.DESCRIPTOR,])




_LISTCLEARANCESRESPONSE = _descriptor.Descriptor(
  name='ListClearancesResponse',
  full_name='yamcs.protobuf.commanding.ListClearancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clearances', full_name='yamcs.protobuf.commanding.ListClearancesResponse.clearances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=287,
)


_CLEARANCEINFO = _descriptor.Descriptor(
  name='ClearanceInfo',
  full_name='yamcs.protobuf.commanding.ClearanceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='yamcs.protobuf.commanding.ClearanceInfo.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='yamcs.protobuf.commanding.ClearanceInfo.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issuedBy', full_name='yamcs.protobuf.commanding.ClearanceInfo.issuedBy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueTime', full_name='yamcs.protobuf.commanding.ClearanceInfo.issueTime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasCommandPrivileges', full_name='yamcs.protobuf.commanding.ClearanceInfo.hasCommandPrivileges', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=493,
)


_UPDATECLEARANCEREQUEST = _descriptor.Descriptor(
  name='UpdateClearanceRequest',
  full_name='yamcs.protobuf.commanding.UpdateClearanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='yamcs.protobuf.commanding.UpdateClearanceRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='yamcs.protobuf.commanding.UpdateClearanceRequest.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=612,
)


_DELETECLEARANCEREQUEST = _descriptor.Descriptor(
  name='DeleteClearanceRequest',
  full_name='yamcs.protobuf.commanding.DeleteClearanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='yamcs.protobuf.commanding.DeleteClearanceRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=656,
)

_LISTCLEARANCESRESPONSE.fields_by_name['clearances'].message_type = _CLEARANCEINFO
_CLEARANCEINFO.fields_by_name['level'].enum_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._SIGNIFICANCEINFO_SIGNIFICANCELEVELTYPE
_CLEARANCEINFO.fields_by_name['issueTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATECLEARANCEREQUEST.fields_by_name['level'].enum_type = yamcs_dot_protobuf_dot_mdb_dot_mdb__pb2._SIGNIFICANCEINFO_SIGNIFICANCELEVELTYPE
DESCRIPTOR.message_types_by_name['ListClearancesResponse'] = _LISTCLEARANCESRESPONSE
DESCRIPTOR.message_types_by_name['ClearanceInfo'] = _CLEARANCEINFO
DESCRIPTOR.message_types_by_name['UpdateClearanceRequest'] = _UPDATECLEARANCEREQUEST
DESCRIPTOR.message_types_by_name['DeleteClearanceRequest'] = _DELETECLEARANCEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListClearancesResponse = _reflection.GeneratedProtocolMessageType('ListClearancesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLEARANCESRESPONSE,
  __module__ = 'yamcs.protobuf.commanding.clearance_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.commanding.ListClearancesResponse)
  ))
_sym_db.RegisterMessage(ListClearancesResponse)

ClearanceInfo = _reflection.GeneratedProtocolMessageType('ClearanceInfo', (_message.Message,), dict(
  DESCRIPTOR = _CLEARANCEINFO,
  __module__ = 'yamcs.protobuf.commanding.clearance_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.commanding.ClearanceInfo)
  ))
_sym_db.RegisterMessage(ClearanceInfo)

UpdateClearanceRequest = _reflection.GeneratedProtocolMessageType('UpdateClearanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECLEARANCEREQUEST,
  __module__ = 'yamcs.protobuf.commanding.clearance_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.commanding.UpdateClearanceRequest)
  ))
_sym_db.RegisterMessage(UpdateClearanceRequest)

DeleteClearanceRequest = _reflection.GeneratedProtocolMessageType('DeleteClearanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETECLEARANCEREQUEST,
  __module__ = 'yamcs.protobuf.commanding.clearance_service_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.commanding.DeleteClearanceRequest)
  ))
_sym_db.RegisterMessage(DeleteClearanceRequest)


DESCRIPTOR._options = None

_CLEARANCEAPI = _descriptor.ServiceDescriptor(
  name='ClearanceApi',
  full_name='yamcs.protobuf.commanding.ClearanceApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=659,
  serialized_end=1263,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListClearances',
    full_name='yamcs.protobuf.commanding.ClearanceApi.ListClearances',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTCLEARANCESRESPONSE,
    serialized_options=_b('\212\222\003\021\n\017/api/clearances'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateClearance',
    full_name='yamcs.protobuf.commanding.ClearanceApi.UpdateClearance',
    index=1,
    containing_service=None,
    input_type=_UPDATECLEARANCEREQUEST,
    output_type=_CLEARANCEINFO,
    serialized_options=_b('\212\222\003M*\032/api/clearances/{username}:\001*b,Clearance of \'{username}\' changed to {level}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteClearance',
    full_name='yamcs.protobuf.commanding.ClearanceApi.DeleteClearance',
    index=2,
    containing_service=None,
    input_type=_DELETECLEARANCEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003F\"\032/api/clearances/{username}b(Clearance revoked from user \'{username}\''),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeClearance',
    full_name='yamcs.protobuf.commanding.ClearanceApi.SubscribeClearance',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_CLEARANCEINFO,
    serialized_options=_b('\332\222\003\013\n\tclearance'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CLEARANCEAPI)

DESCRIPTOR.services_by_name['ClearanceApi'] = _CLEARANCEAPI

# @@protoc_insertion_point(module_scope)
