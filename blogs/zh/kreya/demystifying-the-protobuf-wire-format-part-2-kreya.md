---
title: '解密 Protobuf 线格式（二）'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/protocolbuffers-wire-format-part-2/'
original_language: en
published: 2025-05-15
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b55c27dc88702ec9'
translated: true
---

> 原文：[Demystifying the protobuf wire format - Part 2 | Kreya](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)　·　Kreya Blog

在[上一篇文章](https://kreya.app/blog/protocolbuffers-wire-format/)中，我们探索了 protocol buffers（protobuf）线格式的基础知识。现在，让我们进一步了解一些高级特性：**packed repeated 字段**、**映射（map）** 和**负数**。

## Repeated 字段

Repeated 字段允许你在单个字段中存储同一类型的多个值。例如：

```protobuf
message FruitBasket {  repeated string fruits = 1;}
```

默认情况下，repeated 字段中的每个值在线格式中都会编码为单独的标签-值对。例如，编码 `fruits: ["Apple", "Banana"]` 会产生两个标签-值对，二者字段号相同但值不同：

```
0a 05 41 70 70 6c 65 0a 06 42 61 6e 61 6e 61│  │  │              │  │  └─ UTF-8 encoded string payload (Banana)│  │  │              │  └──── Length of the string (6)│  │  │              └─────── Tag of the field "fruits" (field number 1, wire type 2)│  │  ││  │  └────────────────────── UTF-8 encoded string payload (Apple)│  └───────────────────────── Length of the string (5)└──────────────────────────── Tag of the field "fruits" (field number 1, wire type 2)
```

这是理解 packed repeated 字段和映射如何编码的基础，因为它们都建立在 repeated 字段的基础之上。

## Packed repeated 字段

默认情况下，repeated 字段被编码为多个标签-值对。但对于数值类型，你可以使用 `packed` 选项将所有值存储在一个长度分隔字段中：

```protobuf
message FruitCounts {  repeated int32 values = 1 [packed = true];}
```

Packed repeated 字段的编码方式为：

- 标签（字段号 + 表示长度分隔的 wire type 2）
- 一个指示 packed 数据总字节长度的 varint
- 拼接在一起的 varint 编码值

例如，将 `[3, 270, 86942]` 编码为 packed 后的结果是：

```
0a 06 03 8e 02 9e a7 05│  │  │  │     └──── The varint encoded value of 86942 → 0x9e 0xa7 0x05│  │  │  └────────── The varint encoded value of 270 → 0x8e 0x02│  │  └───────────── The varint encoded value of 3 → 0x03│  ││  └──────────────── Byte length of the packed data└─────────────────── Tag of the field "values" (field number 1, wire type 2 length delimited)
```

如果该字段不是 packed 的，同样的值则会是这样：

```
08 03 08 8e 02 08 9e a7 05 │  │  │  │     │  └──── The varint encoded value of 86942 → 0x9e 0xa7 0x05│  │  │  │     └─────── Tag of the field "values" (field number 1 and wire type 0 varint)│  │  │  ││  │  │  └───────────── The varint encoded value of 270 → 0x8e 0x02│  │  └──────────────── Tag of the field "values" (field number 1 and wire type 0 varint)│  ││  └─────────────────── The varint encoded value of 3 → 0x03└────────────────────── Tag of the field "values" (field number 1 and wire type 0 varint)
```

## 映射（Maps）

Protobuf 中的映射是 repeated 键值消息对的语法糖。例如：

```protobuf
message FruitBasket {  map<string, int32> fruit_counts = 1;}
```

这在内部被表示为：

```protobuf
message FruitBasket {  repeated FruitCountsEntry fruit_counts = 1;}message FruitCountsEntry {  string key = 1;  int32 value = 2;}
```

每个映射条目都被编码为一个长度分隔的内嵌消息。例如，编码 `{ "Apple": 3, "Banana": 5 }` 会产生两个长度分隔字段，每个字段包含编码后的键和值。

```
0a 09 0a 05 41 70 70 6C 65 10 03 0a 0a 0a 06 42 61 6E 61 6E 61 10 05│  │  │                          │  │  └ The second map entry Banana: 5│  │  │                          │  └─── The length of the second map entry: 10 bytes│  │  │                          └────── Tag of the field "fruit_counts" (field number 1, wire type 2 length delimited)│  │  ││  │  └───────────────────────────────── The first map entry Apple: 3│  └──────────────────────────────────── The length of the first map entry: 9 bytes└─────────────────────────────────────── Tag of the field "fruit_counts" (field number 1, wire type 2 length delimited)
```

## 负数：ZigZag 编码

Protobuf 对有符号整数（`sint32`、`sint64`）使用 ZigZag 编码，以便高效编码负数。常规的 `int32` 和 `int64` 使用标准 varint 编码，这对负值来说效率很低。ZigZag 编码将有符号整数映射为无符号整数，使得绝对值较小的数（包括负数）拥有更小的 varint 编码值。ZigZag 编码的公式是：

```text
(n << 1) ^ (n >> 31)
```

例如：

```text
 0 → 0-1 → 1 1 → 2-2 → 3
```

这使得负数在线格式中变得紧凑。

用以下定义对 `temperature = -2` 进行编码：

```protobuf
message Weather {  sint32 temperature = 1;}
```

结果如下：

```text
ZigZag(-2) = (-2 << 1) ^ (-2 >> 31)           = 0b11111100 ^ 0b11111111           = 0b00000011           = 3
```

```
08 03│  └─ ZigZag encoded value of -2 is 3 as varint is 03└──── Tag of the field "temperature" (field number 1, wire type 0 for varint)
```

如果该字段是 `int32` 而非 `sint32`，编码结果会大不相同。当使用 `int32` 时，负数是基于标准 varint 来编码的，而后者针对较小的正数进行了优化。负值以二进制补码形式表示，任何 32 位负整数都会产生一个 10 字节的 varint。对于负数而言，这比 ZigZag 编码的效率低得多。

```text
00000010 2 in binary, displayed as 8-bit11111101 one's complement11111110 add 1 → -2 in two's complement
```

对 `11111110` 进行 varint 编码：

```text
         11111111 11111111 11111111 11111110 # original value -2 in two's complement    1111  1111111  1111111  1111111  1111110 # split into 7-bit chunks 1111110  1111111  1111111  1111111     1111 # change to little endian11111111 11111111 11111111 11111111 00001111 # add continuation bits
```

如你所见，数字 -2 作为 int32 的 varint 编码，在二进制中是 `11111111 11111111 11111111 11111111 00001111`，在十六进制中则是 `FE FF FF FF 0F`。

在消息中：

```
08 FE FF FF FF 0F│  └─ The varint encoded value of -2 as int32 (two's complement of 2)└──── Tag of the field "temperature" (field number 1, wire type 0 for varint)
```

总而言之，对负数使用 `sint32`（采用 ZigZag 编码）比使用 `int32` 节省了大量空间，这就是 protobuf 推荐对可能包含负值的字段使用 `sint32` 的原因。

## 结语

理解这些高级 protobuf 线格式特性能够帮助你调试和优化数据交换。更多详细信息，请参阅官方 [protobuf 编码指南](https://protobuf.dev/programming-guides/encoding)。

好奇这些消息是如何在服务之间传输的？接着阅读我们的 [gRPC 深度探索](https://kreya.app/blog/grpc-deep-dive/)吧。
