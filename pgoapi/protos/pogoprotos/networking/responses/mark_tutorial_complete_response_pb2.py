# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/mark_tutorial_complete_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import player_data_pb2 as pogoprotos_dot_data_dot_player__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/mark_tutorial_complete_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nEpogoprotos/networking/responses/mark_tutorial_complete_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/data/player_data.proto\"\\\n\x1cMarkTutorialCompleteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12+\n\x06player\x18\x02 \x01(\x0b\x32\x1b.pogoprotos.data.PlayerDatab\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player__data__pb2.DESCRIPTOR,])




_MARKTUTORIALCOMPLETERESPONSE = _descriptor.Descriptor(
  name='MarkTutorialCompleteResponse',
  full_name='pogoprotos.networking.responses.MarkTutorialCompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.MarkTutorialCompleteResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.networking.responses.MarkTutorialCompleteResponse.player', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=141,
  serialized_end=233,
)

_MARKTUTORIALCOMPLETERESPONSE.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_player__data__pb2._PLAYERDATA
DESCRIPTOR.message_types_by_name['MarkTutorialCompleteResponse'] = _MARKTUTORIALCOMPLETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkTutorialCompleteResponse = _reflection.GeneratedProtocolMessageType('MarkTutorialCompleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _MARKTUTORIALCOMPLETERESPONSE,
  __module__ = 'pogoprotos.networking.responses.mark_tutorial_complete_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.MarkTutorialCompleteResponse)
  ))
_sym_db.RegisterMessage(MarkTutorialCompleteResponse)


# @@protoc_insertion_point(module_scope)
