# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0eresponse.proto\"\x1b\n\nPrediction\x12\r\n\x05label\x18\x01 \x01(\tb\x06proto3'
)




_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Prediction.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=45,
)

DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'response_pb2'
  # @@protoc_insertion_point(class_scope:Prediction)
  })
_sym_db.RegisterMessage(Prediction)


# @@protoc_insertion_point(module_scope)
