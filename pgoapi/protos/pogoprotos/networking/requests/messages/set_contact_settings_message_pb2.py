# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/set_contact_settings_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import contact_settings_pb2 as pogoprotos_dot_data_dot_player_dot_contact__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/set_contact_settings_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nJpogoprotos/networking/requests/messages/set_contact_settings_message.proto\x12\'pogoprotos.networking.requests.messages\x1a-pogoprotos/data/player/contact_settings.proto\"d\n\x19SetContactSettingsMessage\x12G\n\x16\x63ontact_settings_proto\x18\x01 \x01(\x0b\x32\'.pogoprotos.data.player.ContactSettingsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_contact__settings__pb2.DESCRIPTOR,])




_SETCONTACTSETTINGSMESSAGE = _descriptor.Descriptor(
  name='SetContactSettingsMessage',
  full_name='pogoprotos.networking.requests.messages.SetContactSettingsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contact_settings_proto', full_name='pogoprotos.networking.requests.messages.SetContactSettingsMessage.contact_settings_proto', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=166,
  serialized_end=266,
)

_SETCONTACTSETTINGSMESSAGE.fields_by_name['contact_settings_proto'].message_type = pogoprotos_dot_data_dot_player_dot_contact__settings__pb2._CONTACTSETTINGS
DESCRIPTOR.message_types_by_name['SetContactSettingsMessage'] = _SETCONTACTSETTINGSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetContactSettingsMessage = _reflection.GeneratedProtocolMessageType('SetContactSettingsMessage', (_message.Message,), dict(
  DESCRIPTOR = _SETCONTACTSETTINGSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.set_contact_settings_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SetContactSettingsMessage)
  ))
_sym_db.RegisterMessage(SetContactSettingsMessage)


# @@protoc_insertion_point(module_scope)
