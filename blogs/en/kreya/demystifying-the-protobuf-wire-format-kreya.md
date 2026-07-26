---
title: 'Demystifying the protobuf wire format | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/protocolbuffers-wire-format/'
original_language: en
published: 2024-05-03
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d021212303063c5c'
translated: false
---

> 原文：[Demystifying the protobuf wire format | Kreya](https://kreya.app/blog/protocolbuffers-wire-format/)　·　Kreya Blog

Protocol buffers transform data into a compact binary stream for storage or transmission. In this blog post, we will use a proto definition of a sample message and serialize it to binary data.

## The sample message

For our sample we use the following `.proto` file:

```protobuf
syntax = "proto3";message Fruit {  int32 weight = 1;  string name = 2;}
```

This defines a `Fruit` message with two fields `name` and `weight`. Each of these fields has a type, a name and a field number.

We will serialize a simple sample message with the following values:

```yaml
weight: 150name: 'Apple'
```

Each of the field value pairs is encoded as a combination of the field number, the wire type and a payload. The binary stream always starts with the tag of the first field. The tag is a **varint-encoded** value consisting of the field number and the wire type.

## The varint

Varint is a method of serializing integers using one or more bytes. Smaller numbers take a smaller number of bytes. This encoding is used for the tag of each field as well as for several types in protobuf (`int32`, `enum`, `bool`, and others). Varint uses a group of seven bits to represent the value of the number and an eighth bit as a continuation bit to indicate whether more bytes are needed. Here are the steps involved in encoding integers into varints:

1. Grouping: The integer is broken into 7-bit groups from the least significant to the most significant bits.
2. Continuation Bit: Each 7-bit group is prefixed with a continuation bit. This bit is set to 1 for all byte groups except the last, which is set to 0. This bit tells the decoder whether to expect another byte.
3. Combination: These groups are then combined in a little-endian format, where the least significant group (the rightmost 7 bits) is stored first.

Let's look at encoding the number 150 as a varint:

```bash
         10010110 # decimal 150 in binary       1  0010110 # split into 7bit group 0010110        1 # change to little endian10010110 00000001 # add continuation bits
```

As you can see, the number 150 in varint is `10010110 00000001` in binary or `96 01` in hexadecimal.

The main benefits of the varint encoding is the space efficiency for small numbers. Numbers smaller than 128 are stored in just one byte. As numbers get larger, additional bytes are used. This is very efficient for data that is frequently small but can occasionally be large (which in reality is often the case for most numbers).

For fields that almost always contain large numbers, the varint encoding is inefficient due to the additional continuation bit. In this case fixed size numbers, for example `fixed32`, should be preferred.

## The wire types

Protobuf knows five different wire types. A wire type describes the encoding format of a payload.

| Value | Name | Proto types |
|---|---|---|
| 0 | varint | int32, int64, uint32, uint64, sint32, sint64, bool, enum |
| 1 | i64 | fixed64, sfixed64, double |
| 2 | len | string, bytes, embedded messages, packed repeated fields |
| 3 | SGROUP | group start (deprecated) |
| 4 | EGROUP | group end (deprecated) |
| 5 | i32 | fixed32, sfixed32, float |

## The tag

The tag is a varint-encoded value consisting of the field number and the wire type. The field number of our first field is `1` and since it is an `int32` which gets encoded as varint, the wire type is `0`. The low three bits represent the wire type, the other bits represent the field number. This can be expressed as

```text
wire_type | (field_number << 3)
```

As our field number is less than the maximum number we can serialize to the four bits available, we do not need an additional byte for the field number. For the wire type `0` and the field number `1` this will result in `08` with the following binary representation:

```
0000 1000│  │   └─── Wire type (0)│  └─────── Field number (1)└────────── Varint continuation bit
```

## The value

Immediately after the tag the value of the field gets encoded according to the wire type. For the `weight` field we want to encode `150` as int32 with a wire type of varint. As the sample in the [varint](#the-varint) paragraph shows, this results in `96 01`.

So far we have the following data:

```
08 96 01│    └──── Payload of the field "weight", varint encoded└───────── Tag of the field "weight" (field number and wire type)
```

## Length delimited field

On to the field `name`. According to our wire type table, a string is a length delimited field and therefore encoded with wire type 2. Together with the field number 2 this results in the tag `12`:

```
0001 0010│  │   └─── Wire type (2)│  └─────── Field number (2)└────────── Varint continuation bit
```

The tag of a length delimited field is followed by a varint which specifies the length of the payload. The UTF-8 representation of `Apple` is `41 70 70 6c 65`. These are 5 bytes, therefore the length is `5`.

```
12 05 41 70 70 6c 65│  │        └──────── UTF-8 encoded string payload (Apple)│  └───────────────── Count of UTF-8 bytes of the payload (5)└──────────────────── Tag of the field "name" (field number and wire type)
```

## The encoded sample message

Concatenating our two encoded fields leads to the following bytes:

```
08 96 01 12 05 41 70 70 6c 65│        └────────── Length delimited field "name" with field number 2└─────────────────── Varint encoded field "weight" with field number 1
```

We can verify our encoding using `protoc`:

```bash
echo '08960112054170706c65' | xxd -r -p | protoc --decode=Fruit ./fruit.protoweight: 150name: "Apple"
```

which exactly results in our sample values as expected 🥳🎉

The command works like this:

1. Echo our hex encoded bytes
2. Pass them through `xxd` to transform the hex into binary
3. Pass the binary stream to `protoc` with the decode flag

    - For protoc to access our sample proto we stored it in the working directory in a file named `fruit.proto`

Even if we do not have access to the proto file, we can extract some information from the encoded protobuf by using the `decode_raw` flag:

```bash
echo '08960112054170706c65' | xxd -r -p | protoc --decode_raw1: 1502: "Apple"
```

This tells us there are two fields, one with the field number one that decodes to the value of 150, and one with the field number of two which decodes to the string "Apple".

## Other wire types

- Bytes and nested messages are encoded exactly the same way as strings with a length delimited encoding.
- Boolean values are encoded as varints resulting in `01` for `true` and `00` for false.
- Enums are also encoded as varints.
- Repeated fields (as long as they are not packed) end up as multiple tag value pairs in the byte stream with the same tag being present multiple times.
- Packed repeated fields are encoded as length delimited fields.

## Closing

In this blog post we have encoded a sample protobuf message and validated the encoded bytes with `protoc`. For more details, see the official [protobuf encoding guide](https://protobuf.dev/programming-guides/encoding) or continue with [Part 2 of this series](https://kreya.app/blog/protocolbuffers-wire-format-part-2/) for a deep dive into maps, negative numbers, and packed repeated fields.

To learn how these encoded messages are transported over the network, check out our [gRPC deep dive](https://kreya.app/blog/grpc-deep-dive/).
