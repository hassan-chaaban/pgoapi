# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/use_item_egg_incubator_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/use_item_egg_incubator_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/use_item_egg_incubator_message.proto\x12\'pogoprotos.networking.requests.messages\"B\n\x1aUseItemEggIncubatorMessage\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x13\n\x0bpokemond_id\x18\x02 \x01(\x03\x62\x06proto3')
)




_USEITEMEGGINCUBATORMESSAGE = _descriptor.Descriptor(
  name='UseItemEggIncubatorMessage',
  full_name='pogoprotos.networking.requests.messages.UseItemEggIncubatorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='pogoprotos.networking.requests.messages.UseItemEggIncubatorMessage.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemond_id', full_name='pogoprotos.networking.requests.messages.UseItemEggIncubatorMessage.pokemond_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['UseItemEggIncubatorMessage'] = _USEITEMEGGINCUBATORMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemEggIncubatorMessage = _reflection.GeneratedProtocolMessageType('UseItemEggIncubatorMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMEGGINCUBATORMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.use_item_egg_incubator_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.UseItemEggIncubatorMessage)
  ))
_sym_db.RegisterMessage(UseItemEggIncubatorMessage)


# @@protoc_insertion_point(module_scope)
