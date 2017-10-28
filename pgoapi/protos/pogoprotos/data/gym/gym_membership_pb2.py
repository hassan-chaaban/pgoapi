# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gym/gym_membership.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/gym/gym_membership.proto',
  package='pogoprotos.data.gym',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/data/gym/gym_membership.proto\x12\x13pogoprotos.data.gym\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x32pogoprotos/data/player/player_public_profile.proto\"\xc3\x01\n\rGymMembership\x12-\n\x07pokemon\x18\x01 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12\x36\n\x10training_pokemon\x18\x03 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonDatab\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,])




_GYMMEMBERSHIP = _descriptor.Descriptor(
  name='GymMembership',
  full_name='pogoprotos.data.gym.GymMembership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.gym.GymMembership.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='pogoprotos.data.gym.GymMembership.trainer_public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='training_pokemon', full_name='pogoprotos.data.gym.GymMembership.training_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=154,
  serialized_end=349,
)

_GYMMEMBERSHIP.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_GYMMEMBERSHIP.fields_by_name['trainer_public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_GYMMEMBERSHIP.fields_by_name['training_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
DESCRIPTOR.message_types_by_name['GymMembership'] = _GYMMEMBERSHIP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymMembership = _reflection.GeneratedProtocolMessageType('GymMembership', (_message.Message,), dict(
  DESCRIPTOR = _GYMMEMBERSHIP,
  __module__ = 'pogoprotos.data.gym.gym_membership_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.gym.GymMembership)
  ))
_sym_db.RegisterMessage(GymMembership)


# @@protoc_insertion_point(module_scope)
