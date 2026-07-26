---
title: 'Demystifying the protobuf wire format - Part 2 | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/protocolbuffers-wire-format-part-2/'
original_language: en
published: 2025-05-15
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b55c27dc88702ec9'
translated: false
---

> 原文：[Demystifying the protobuf wire format - Part 2 | Kreya](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)　·　Kreya Blog

In our [previous post](https://kreya.app/blog/protocolbuffers-wire-format/), we explored the basics of the protocol buffers (protobuf) wire format. Now, let's take a closer look at some advanced features: **packed repeated fields**, **maps** and **negative numbers**.

## Repeated fields

Repeated fields allow you to store multiple values of the same type in a single field. For example:

```protobuf
message FruitBasket {  repeated string fruits = 1;}
```

By default, each value in a repeated field is encoded as a separate tag-value pair in the wire format. For example, encoding `fruits: ["Apple", "Banana"]` results in two tag-value pairs, each with the same field number but different values:

```
0a 05 41 70 70 6c 65 0a 06 42 61 6e 61 6e 61│  │  │              │  │  └─ UTF-8 encoded string payload (Banana)│  │  │              │  └──── Length of the string (6)│  │  │              └─────── Tag of the field "fruits" (field number 1, wire type 2)│  │  ││  │  └────────────────────── UTF-8 encoded string payload (Apple)│  └───────────────────────── Length of the string (5)└──────────────────────────── Tag of the field "fruits" (field number 1, wire type 2)
```

This is the foundation for understanding how packed repeated fields and maps are encoded, as both build on the repeated field concept.

## Packed repeated fields

By default, repeated fields are encoded as multiple tag-value pairs. However, for numeric types, you can use the `packed` option to store all values in a single length-delimited field:

```protobuf
message FruitCounts {  repeated int32 values = 1 [packed = true];}
```

A packed repeated field is encoded as:

- The tag (field number + wire type 2 for length-delimited)
- A varint indicating the total byte length of the packed data
- The concatenated varint-encoded values

For example, encoding `[3, 270, 86942]` as packed results in:

```
0a 06 03 8e 02 9e a7 05│  │  │  │     └──── The varint encoded value of 86942 → 0x9e 0xa7 0x05│  │  │  └────────── The varint encoded value of 270 → 0x8e 0x02│  │  └───────────── The varint encoded value of 3 → 0x03│  ││  └──────────────── Byte length of the packed data└─────────────────── Tag of the field "values" (field number 1, wire type 2 length delimited)
```

If the field would not be packed, the same value would look like this:

```
08 03 08 8e 02 08 9e a7 05 │  │  │  │     │  └──── The varint encoded value of 86942 → 0x9e 0xa7 0x05│  │  │  │     └─────── Tag of the field "values" (field number 1 and wire type 0 varint)│  │  │  ││  │  │  └───────────── The varint encoded value of 270 → 0x8e 0x02│  │  └──────────────── Tag of the field "values" (field number 1 and wire type 0 varint)│  ││  └─────────────────── The varint encoded value of 3 → 0x03└────────────────────── Tag of the field "values" (field number 1 and wire type 0 varint)
```

## Maps

Maps in protobuf are syntactic sugar for repeated key-value message pairs. For example:

```protobuf
message FruitBasket {  map<string, int32> fruit_counts = 1;}
```

This is internally represented as:

```protobuf
message FruitBasket {  repeated FruitCountsEntry fruit_counts = 1;}message FruitCountsEntry {  string key = 1;  int32 value = 2;}
```

Each map entry is encoded as a length-delimited embedded message. For example, encoding `{ "Apple": 3, "Banana": 5 }` results in two length-delimited fields, each containing the encoded key and value.

```
0a 09 0a 05 41 70 70 6C 65 10 03 0a 0a 0a 06 42 61 6E 61 6E 61 10 05│  │  │                          │  │  └ The second map entry Banana: 5│  │  │                          │  └─── The length of the second map entry: 10 bytes│  │  │                          └────── Tag of the field "fruit_counts" (field number 1, wire type 2 length delimited)│  │  ││  │  └───────────────────────────────── The first map entry Apple: 3│  └──────────────────────────────────── The length of the first map entry: 9 bytes└─────────────────────────────────────── Tag of the field "fruit_counts" (field number 1, wire type 2 length delimited)
```

## Negative numbers: ZigZag encoding

Protobuf uses ZigZag encoding for signed integers (`sint32`, `sint64`) to efficiently encode negative numbers. Regular `int32` and `int64` use standard varint encoding, which is inefficient for negative values. ZigZag encoding maps signed integers to unsigned so that numbers with small absolute values (including negative ones) have a small varint encoded value. The formula for ZigZag encoding is:

```text
(n << 1) ^ (n >> 31)
```

For example:

```text
 0 → 0-1 → 1 1 → 2-2 → 3
```

This makes negative numbers compact in the wire format.

Encoding `temperature = -2` with

```protobuf
message Weather {  sint32 temperature = 1;}
```

results in

```text
ZigZag(-2) = (-2 << 1) ^ (-2 >> 31)           = 0b11111100 ^ 0b11111111           = 0b00000011           = 3
```

```
08 03│  └─ ZigZag encoded value of -2 is 3 as varint is 03└──── Tag of the field "temperature" (field number 1, wire type 0 for varint)
```

If the field was an `int32` instead of a `sint32`, the encoding would look very different. When using `int32`, negative numbers are encoded using standard varint encoding, which is optimized for small positive numbers. Negative values are represented in two's complement form, which always results in a 10-byte varint for any negative 32-bit integer. This is much less efficient than ZigZag encoding for negative numbers.

```text
00000010 2 in binary, displayed as 8-bit11111101 one's complement11111110 add 1 → -2 in two's complement
```

Varint encoding `11111110`:

```text
         11111111 11111111 11111111 11111110 # original value -2 in two's complement    1111  1111111  1111111  1111111  1111110 # split into 7-bit chunks 1111110  1111111  1111111  1111111     1111 # change to little endian11111111 11111111 11111111 11111111 00001111 # add continuation bits
```

As you can see, the number -2 as int32 in varint is `11111111 11111111 11111111 11111111 00001111` in binary or `FE FF FF FF 0F` in hexadecimal.

In the message:

```
08 FE FF FF FF 0F│  └─ The varint encoded value of -2 as int32 (two's complement of 2)└──── Tag of the field "temperature" (field number 1, wire type 0 for varint)
```

In summary, using `sint32` (with ZigZag encoding) is much more space-efficient for negative numbers than using `int32`, which is why protobuf recommends `sint32` for fields that may contain negative values.

## Closing

Understanding these advanced protobuf wire format features helps you debug and optimize your data interchange. For more details, see the official [protobuf encoding guide](https://protobuf.dev/programming-guides/encoding).

Curious how these messages travel between services? Read our [gRPC deep dive](https://kreya.app/blog/grpc-deep-dive/) next.
