# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_participant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_pokemon_info_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2
from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.map.pokemon import lobby_pokemon_pb2 as pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_participant.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_pb=_b('\n/pogoprotos/data/battle/battle_participant.proto\x12\x16pogoprotos.data.battle\x1a\x30pogoprotos/data/battle/battle_pokemon_info.proto\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a*pogoprotos/map/pokemon/lobby_pokemon.proto\"\xff\x02\n\x11\x42\x61ttleParticipant\x12\x41\n\x0e\x61\x63tive_pokemon\x18\x01 \x01(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12\x42\n\x0freserve_pokemon\x18\x03 \x03(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12\x43\n\x10\x64\x65\x66\x65\x61ted_pokemon\x18\x04 \x03(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12;\n\rlobby_pokemon\x18\x05 \x03(\x0b\x32$.pogoprotos.map.pokemon.LobbyPokemon\x12\x14\n\x0c\x64\x61mage_dealt\x18\x06 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2.DESCRIPTOR,])




_BATTLEPARTICIPANT = _descriptor.Descriptor(
  name='BattleParticipant',
  full_name='pogoprotos.data.battle.BattleParticipant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.active_pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='pogoprotos.data.battle.BattleParticipant.trainer_public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reserve_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.reserve_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defeated_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.defeated_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lobby_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.lobby_pokemon', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage_dealt', full_name='pogoprotos.data.battle.BattleParticipant.damage_dealt', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=222,
  serialized_end=605,
)

_BATTLEPARTICIPANT.fields_by_name['active_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['trainer_public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_BATTLEPARTICIPANT.fields_by_name['reserve_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['defeated_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['lobby_pokemon'].message_type = pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2._LOBBYPOKEMON
DESCRIPTOR.message_types_by_name['BattleParticipant'] = _BATTLEPARTICIPANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BattleParticipant = _reflection.GeneratedProtocolMessageType('BattleParticipant', (_message.Message,), dict(
  DESCRIPTOR = _BATTLEPARTICIPANT,
  __module__ = 'pogoprotos.data.battle.battle_participant_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattleParticipant)
  ))
_sym_db.RegisterMessage(BattleParticipant)


# @@protoc_insertion_point(module_scope)
