# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_stats.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import gym_badge_type_pb2 as pogoprotos_dot_enums_dot_gym__badge__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_stats.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/data/player/player_stats.proto\x12\x16pogoprotos.data.player\x1a%pogoprotos/enums/gym_badge_type.proto\"\xc3\x07\n\x0bPlayerStats\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x12\n\nexperience\x18\x02 \x01(\x03\x12\x16\n\x0eprev_level_exp\x18\x03 \x01(\x03\x12\x16\n\x0enext_level_exp\x18\x04 \x01(\x03\x12\x11\n\tkm_walked\x18\x05 \x01(\x02\x12\x1f\n\x17num_pokemon_encountered\x18\x06 \x01(\x05\x12\"\n\x1anum_unique_pokedex_entries\x18\x07 \x01(\x05\x12\x1c\n\x14num_pokemon_captured\x18\x08 \x01(\x05\x12\x16\n\x0enum_evolutions\x18\t \x01(\x05\x12\x18\n\x10poke_stop_visits\x18\n \x01(\x05\x12!\n\x19number_of_pokeball_thrown\x18\x0b \x01(\x05\x12\x18\n\x10num_eggs_hatched\x18\x0c \x01(\x05\x12\x1b\n\x13\x62ig_magikarp_caught\x18\r \x01(\x05\x12\x1d\n\x15num_battle_attack_won\x18\x0e \x01(\x05\x12\x1f\n\x17num_battle_attack_total\x18\x0f \x01(\x05\x12\x1f\n\x17num_battle_defended_won\x18\x10 \x01(\x05\x12\x1f\n\x17num_battle_training_won\x18\x11 \x01(\x05\x12!\n\x19num_battle_training_total\x18\x12 \x01(\x05\x12\x1d\n\x15prestige_raised_total\x18\x13 \x01(\x05\x12\x1e\n\x16prestige_dropped_total\x18\x14 \x01(\x05\x12\x1c\n\x14num_pokemon_deployed\x18\x15 \x01(\x05\x12\"\n\x1anum_pokemon_caught_by_type\x18\x16 \x03(\x05\x12\x1c\n\x14small_rattata_caught\x18\x17 \x01(\x05\x12\x14\n\x0cused_km_pool\x18\x18 \x01(\x01\x12\x19\n\x11last_km_refill_ms\x18\x19 \x01(\x03\x12\x1b\n\x13num_raid_battle_won\x18\x1a \x01(\x05\x12\x1d\n\x15num_raid_battle_total\x18\x1b \x01(\x05\x12 \n\x18num_legendary_battle_won\x18\x1c \x01(\x05\x12\"\n\x1anum_legendary_battle_total\x18\x1d \x01(\x05\x12\x17\n\x0fnum_berries_fed\x18\x1e \x01(\x05\x12\x19\n\x11total_defended_ms\x18\x1f \x01(\x03\x12\x34\n\x0c\x65vent_badges\x18  \x03(\x0e\x32\x1e.pogoprotos.enums.GymBadgeTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_gym__badge__type__pb2.DESCRIPTOR,])




_PLAYERSTATS = _descriptor.Descriptor(
  name='PlayerStats',
  full_name='pogoprotos.data.player.PlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.player.PlayerStats.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience', full_name='pogoprotos.data.player.PlayerStats.experience', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_level_exp', full_name='pogoprotos.data.player.PlayerStats.prev_level_exp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_level_exp', full_name='pogoprotos.data.player.PlayerStats.next_level_exp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_walked', full_name='pogoprotos.data.player.PlayerStats.km_walked', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_pokemon_encountered', full_name='pogoprotos.data.player.PlayerStats.num_pokemon_encountered', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_unique_pokedex_entries', full_name='pogoprotos.data.player.PlayerStats.num_unique_pokedex_entries', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_pokemon_captured', full_name='pogoprotos.data.player.PlayerStats.num_pokemon_captured', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_evolutions', full_name='pogoprotos.data.player.PlayerStats.num_evolutions', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_stop_visits', full_name='pogoprotos.data.player.PlayerStats.poke_stop_visits', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_pokeball_thrown', full_name='pogoprotos.data.player.PlayerStats.number_of_pokeball_thrown', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_eggs_hatched', full_name='pogoprotos.data.player.PlayerStats.num_eggs_hatched', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='big_magikarp_caught', full_name='pogoprotos.data.player.PlayerStats.big_magikarp_caught', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_battle_attack_won', full_name='pogoprotos.data.player.PlayerStats.num_battle_attack_won', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_battle_attack_total', full_name='pogoprotos.data.player.PlayerStats.num_battle_attack_total', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_battle_defended_won', full_name='pogoprotos.data.player.PlayerStats.num_battle_defended_won', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_battle_training_won', full_name='pogoprotos.data.player.PlayerStats.num_battle_training_won', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_battle_training_total', full_name='pogoprotos.data.player.PlayerStats.num_battle_training_total', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_raised_total', full_name='pogoprotos.data.player.PlayerStats.prestige_raised_total', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_dropped_total', full_name='pogoprotos.data.player.PlayerStats.prestige_dropped_total', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_pokemon_deployed', full_name='pogoprotos.data.player.PlayerStats.num_pokemon_deployed', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_pokemon_caught_by_type', full_name='pogoprotos.data.player.PlayerStats.num_pokemon_caught_by_type', index=21,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_rattata_caught', full_name='pogoprotos.data.player.PlayerStats.small_rattata_caught', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used_km_pool', full_name='pogoprotos.data.player.PlayerStats.used_km_pool', index=23,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_km_refill_ms', full_name='pogoprotos.data.player.PlayerStats.last_km_refill_ms', index=24,
      number=25, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_raid_battle_won', full_name='pogoprotos.data.player.PlayerStats.num_raid_battle_won', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_raid_battle_total', full_name='pogoprotos.data.player.PlayerStats.num_raid_battle_total', index=26,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_legendary_battle_won', full_name='pogoprotos.data.player.PlayerStats.num_legendary_battle_won', index=27,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_legendary_battle_total', full_name='pogoprotos.data.player.PlayerStats.num_legendary_battle_total', index=28,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_berries_fed', full_name='pogoprotos.data.player.PlayerStats.num_berries_fed', index=29,
      number=30, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_defended_ms', full_name='pogoprotos.data.player.PlayerStats.total_defended_ms', index=30,
      number=31, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_badges', full_name='pogoprotos.data.player.PlayerStats.event_badges', index=31,
      number=32, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=109,
  serialized_end=1072,
)

_PLAYERSTATS.fields_by_name['event_badges'].enum_type = pogoprotos_dot_enums_dot_gym__badge__type__pb2._GYMBADGETYPE
DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERSTATS,
  __module__ = 'pogoprotos.data.player.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerStats)
  ))
_sym_db.RegisterMessage(PlayerStats)


# @@protoc_insertion_point(module_scope)
