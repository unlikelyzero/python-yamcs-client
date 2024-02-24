# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/config/config.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/config/config.proto',
  package='yamcs.protobuf.config',
  syntax='proto2',
  serialized_options=b'\n\031org.yamcs.protobuf.configB\013ConfigProtoP\001',
  serialized_pb=b'\n\"yamcs/protobuf/config/config.proto\x12\x15yamcs.protobuf.config\x1a\x1cgoogle/protobuf/struct.proto\"\x9a\x02\n\x08SpecInfo\x12\x32\n\x07options\x18\x01 \x03(\x0b\x32!.yamcs.protobuf.config.OptionInfo\x12\x18\n\x10\x61llowUnknownKeys\x18\x02 \x01(\x08\x12=\n\rrequiredOneOf\x18\x03 \x03(\x0b\x32&.yamcs.protobuf.config.OptionGroupInfo\x12?\n\x0frequireTogether\x18\x04 \x03(\x0b\x32&.yamcs.protobuf.config.OptionGroupInfo\x12@\n\x0ewhenConditions\x18\x05 \x03(\x0b\x32(.yamcs.protobuf.config.WhenConditionInfo\"\x1f\n\x0fOptionGroupInfo\x12\x0c\n\x04keys\x18\x01 \x03(\t\"]\n\x11WhenConditionInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x14\n\x0crequiredKeys\x18\x03 \x03(\t\"\xb8\x03\n\nOptionInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.yamcs.protobuf.config.OptionType\x12\r\n\x05title\x18\x03 \x01(\t\x12\'\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x10\n\x08required\x18\x05 \x01(\x08\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\x12\x0e\n\x06secret\x18\x07 \x01(\x08\x12\x14\n\x0cversionAdded\x18\x08 \x01(\t\x12\x1a\n\x12\x64\x65precationMessage\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x03(\t\x12\x36\n\x0b\x65lementType\x18\x0b \x01(\x0e\x32!.yamcs.protobuf.config.OptionType\x12-\n\x04spec\x18\x0c \x01(\x0b\x32\x1f.yamcs.protobuf.config.SpecInfo\x12\'\n\x07\x63hoices\x18\r \x03(\x0b\x32\x16.google.protobuf.Value\x12\x19\n\x11\x61pplySpecDefaults\x18\x0e \x01(\x08\x12\x0f\n\x07\x61liases\x18\x0f \x03(\t*n\n\nOptionType\x12\x07\n\x03\x41NY\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\t\n\x05\x46LOAT\x10\x04\x12\x08\n\x04LIST\x10\x05\x12\x13\n\x0fLIST_OR_ELEMENT\x10\x06\x12\x07\n\x03MAP\x10\x07\x12\n\n\x06STRING\x10\x08\x42*\n\x19org.yamcs.protobuf.configB\x0b\x43onfigProtoP\x01'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])

_OPTIONTYPE = _descriptor.EnumDescriptor(
  name='OptionType',
  full_name='yamcs.protobuf.config.OptionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_OR_ELEMENT', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=7, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=947,
  serialized_end=1057,
)
_sym_db.RegisterEnumDescriptor(_OPTIONTYPE)

OptionType = enum_type_wrapper.EnumTypeWrapper(_OPTIONTYPE)
ANY = 1
BOOLEAN = 2
INTEGER = 3
FLOAT = 4
LIST = 5
LIST_OR_ELEMENT = 6
MAP = 7
STRING = 8



_SPECINFO = _descriptor.Descriptor(
  name='SpecInfo',
  full_name='yamcs.protobuf.config.SpecInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='yamcs.protobuf.config.SpecInfo.options', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowUnknownKeys', full_name='yamcs.protobuf.config.SpecInfo.allowUnknownKeys', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requiredOneOf', full_name='yamcs.protobuf.config.SpecInfo.requiredOneOf', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requireTogether', full_name='yamcs.protobuf.config.SpecInfo.requireTogether', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='whenConditions', full_name='yamcs.protobuf.config.SpecInfo.whenConditions', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=92,
  serialized_end=374,
)


_OPTIONGROUPINFO = _descriptor.Descriptor(
  name='OptionGroupInfo',
  full_name='yamcs.protobuf.config.OptionGroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='yamcs.protobuf.config.OptionGroupInfo.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=376,
  serialized_end=407,
)


_WHENCONDITIONINFO = _descriptor.Descriptor(
  name='WhenConditionInfo',
  full_name='yamcs.protobuf.config.WhenConditionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yamcs.protobuf.config.WhenConditionInfo.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yamcs.protobuf.config.WhenConditionInfo.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requiredKeys', full_name='yamcs.protobuf.config.WhenConditionInfo.requiredKeys', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=409,
  serialized_end=502,
)


_OPTIONINFO = _descriptor.Descriptor(
  name='OptionInfo',
  full_name='yamcs.protobuf.config.OptionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.config.OptionInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='yamcs.protobuf.config.OptionInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='yamcs.protobuf.config.OptionInfo.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='yamcs.protobuf.config.OptionInfo.default', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='yamcs.protobuf.config.OptionInfo.required', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='yamcs.protobuf.config.OptionInfo.hidden', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret', full_name='yamcs.protobuf.config.OptionInfo.secret', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionAdded', full_name='yamcs.protobuf.config.OptionInfo.versionAdded', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deprecationMessage', full_name='yamcs.protobuf.config.OptionInfo.deprecationMessage', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yamcs.protobuf.config.OptionInfo.description', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elementType', full_name='yamcs.protobuf.config.OptionInfo.elementType', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='yamcs.protobuf.config.OptionInfo.spec', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choices', full_name='yamcs.protobuf.config.OptionInfo.choices', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applySpecDefaults', full_name='yamcs.protobuf.config.OptionInfo.applySpecDefaults', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='yamcs.protobuf.config.OptionInfo.aliases', index=14,
      number=15, type=9, cpp_type=9, label=3,
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
  serialized_start=505,
  serialized_end=945,
)

_SPECINFO.fields_by_name['options'].message_type = _OPTIONINFO
_SPECINFO.fields_by_name['requiredOneOf'].message_type = _OPTIONGROUPINFO
_SPECINFO.fields_by_name['requireTogether'].message_type = _OPTIONGROUPINFO
_SPECINFO.fields_by_name['whenConditions'].message_type = _WHENCONDITIONINFO
_WHENCONDITIONINFO.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_OPTIONINFO.fields_by_name['type'].enum_type = _OPTIONTYPE
_OPTIONINFO.fields_by_name['default'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_OPTIONINFO.fields_by_name['elementType'].enum_type = _OPTIONTYPE
_OPTIONINFO.fields_by_name['spec'].message_type = _SPECINFO
_OPTIONINFO.fields_by_name['choices'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['SpecInfo'] = _SPECINFO
DESCRIPTOR.message_types_by_name['OptionGroupInfo'] = _OPTIONGROUPINFO
DESCRIPTOR.message_types_by_name['WhenConditionInfo'] = _WHENCONDITIONINFO
DESCRIPTOR.message_types_by_name['OptionInfo'] = _OPTIONINFO
DESCRIPTOR.enum_types_by_name['OptionType'] = _OPTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpecInfo = _reflection.GeneratedProtocolMessageType('SpecInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPECINFO,
  '__module__' : 'yamcs.protobuf.config.config_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.config.SpecInfo)
  })
_sym_db.RegisterMessage(SpecInfo)

OptionGroupInfo = _reflection.GeneratedProtocolMessageType('OptionGroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONGROUPINFO,
  '__module__' : 'yamcs.protobuf.config.config_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.config.OptionGroupInfo)
  })
_sym_db.RegisterMessage(OptionGroupInfo)

WhenConditionInfo = _reflection.GeneratedProtocolMessageType('WhenConditionInfo', (_message.Message,), {
  'DESCRIPTOR' : _WHENCONDITIONINFO,
  '__module__' : 'yamcs.protobuf.config.config_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.config.WhenConditionInfo)
  })
_sym_db.RegisterMessage(WhenConditionInfo)

OptionInfo = _reflection.GeneratedProtocolMessageType('OptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONINFO,
  '__module__' : 'yamcs.protobuf.config.config_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.config.OptionInfo)
  })
_sym_db.RegisterMessage(OptionInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
