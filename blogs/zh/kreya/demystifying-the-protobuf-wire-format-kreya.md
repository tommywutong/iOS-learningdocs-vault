---
title: '解密 Protobuf 线格式'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/protocolbuffers-wire-format/'
original_language: en
published: 2024-05-03
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d021212303063c5c'
translated: true
---

> 原文：[Demystifying the protobuf wire format | Kreya](https://kreya.app/blog/protocolbuffers-wire-format/)　·　Kreya Blog

Protocol Buffers 会将数据转换成紧凑的二进制流，用于存储或传输。本文将使用一个示例消息的 proto 定义，并将其序列化为二进制数据。

## 示例消息

我们使用以下 `.proto` 文件作为示例：

```protobuf
syntax = "proto3";message Fruit {  int32 weight = 1;  string name = 2;}
```

这定义了一个 `Fruit` 消息，包含两个字段 `name` 和 `weight`。每个字段都有类型、名称和字段编号。

我们将使用以下值序列化一个简单的示例消息：

```yaml
weight: 150name: 'Apple'
```

每个字段值对都被编码为字段编号、wire type 和 payload 的组合。二进制流总是以第一个字段的 tag 开始。tag 是一个 **varint 编码** 的值，由字段编号和 wire type 组成。

## Varint

Varint 是一种使用一个或多个字节来序列化整数的方法。较小的数字占用较少的字节数。这种编码方式用于每个字段的 tag 以及 protobuf 中的几种类型（`int32`、`enum`、`bool` 等）。Varint 使用一组 7 个比特来表示数字的值，并使用第 8 个比特作为 continuation bit，以指示是否需要更多字节。以下是将整数编码为 varint 的步骤：

1. **分组**：从最低有效位到最高有效位，将整数分解为 7 比特为一组。
2. **continuation bit**：在每个 7 比特组前添加一个 continuation bit。除最后一个字节组外，所有字节组的此比特都设置为 1，最后一个字节组设置为 0。此比特告知解码器是否应期待下一个字节。
3. **组合**：然后以 little-endian 格式组合这些组，即最低有效组（最右边的 7 个比特）优先存储。

让我们看看将数字 150 编码为 varint 的过程：

```bash
         10010110 # decimal 150 in binary       1  0010110 # split into 7bit group 0010110        1 # change to little endian10010110 00000001 # add continuation bits
```

如你所见，数字 150 在 varint 中二进制表示为 `10010110 00000001`，十六进制表示为 `96 01`。

Varint 编码的主要优点是对于小数字的空间效率。小于 128 的数字只需一个字节存储。随着数字增大，会使用额外的字节。这对于那些通常很小但偶尔会很大的数据非常高效（实际应用中，大多数数字通常都是如此）。

对于几乎总是包含大数字的字段，varint 编码由于额外的 continuation bit 而效率低下。在这种情况下，应优先使用固定大小的数字，例如 `fixed32`。

## wire type

Protobuf 定义了五种不同的 wire type。wire type 描述了 payload 的编码格式。

| 值 | 名称 | Proto 类型 |
|---|---|---|
| 0 | varint | int32, int64, uint32, uint64, sint32, sint64, bool, enum |
| 1 | i64 | fixed64, sfixed64, double |
| 2 | len | 字符串、字节、嵌入式消息、打包的重复字段 |
| 3 | SGROUP | group start (已废弃) |
| 4 | EGROUP | group end (已废弃) |
| 5 | i32 | fixed32, sfixed32, float |

## 标签

tag 是一个 varint 编码的值，由字段编号和 wire type 组成。我们第一个字段的字段编号是 `1`，由于它是 `int32`，编码为 varint，因此 wire type 是 `0`。低 3 位表示 wire type，其他位表示字段编号。这可以表示为：

```text
wire_type | (field_number << 3)
```

由于我们的字段编号小于可序列化到可用四个比特的最大数字，因此我们不需要为字段编号增加额外的字节。对于 wire type `0` 和字段编号 `1`，这将得到 `08`，其二进制表示如下：

```
0000 1000│  │   └─── Wire type (0)│  └─────── Field number (1)└────────── Varint continuation bit
```

## 值

在 tag 之后，紧接着根据 wire type 编码字段的值。对于 `weight` 字段，我们想要将 `150` 编码为 int32，wire type 为 varint。如 [varint](#the-varint) 部分的示例所示，这将得到 `96 01`。

到目前为止，我们有以下数据：

```
08 96 01│    └──── Payload of the field "weight", varint encoded└───────── Tag of the field "weight" (field number and wire type)
```

## 长度分隔字段

接下来是 `name` 字段。根据我们的 wire type 表，字符串是一个长度分隔字段，因此使用 wire type 2 进行编码。结合字段编号 2，得到 tag `12`：

```
0001 0010│  │   └─── Wire type (2)│  └─────── Field number (2)└────────── Varint continuation bit
```

长度分隔字段的 tag 后面紧跟着一个 varint，用于指定 payload 的长度。`Apple` 的 UTF-8 表示是 `41 70 70 6c 65`。这是 5 个字节，因此长度为 `5`。

```
12 05 41 70 70 6c 65│  │        └──────── UTF-8 encoded string payload (Apple)│  └───────────────── Count of UTF-8 bytes of the payload (5)└──────────────────── Tag of the field "name" (field number and wire type)
```

## 编码后的示例消息

将我们编码后的两个字段连接起来，得到以下字节：

```
08 96 01 12 05 41 70 70 6c 65│        └────────── Length delimited field "name" with field number 2└─────────────────── Varint encoded field "weight" with field number 1
```

我们可以使用 `protoc` 验证我们的编码：

```bash
echo '08960112054170706c65' | xxd -r -p | protoc --decode=Fruit ./fruit.protoweight: 150name: "Apple"
```

结果完全符合我们的示例值 🥳🎉

该命令的工作原理如下：

1. 输出我们的十六进制编码字节
2. 通过 `xxd` 将十六进制转换为二进制
3. 将二进制流通过 `decode` 标志传递给 `protoc`

    - 为了让 `protoc` 访问我们的示例 proto，我们将其存储在工作目录中，文件名为 `fruit.proto`

即使我们无法访问 proto 文件，也可以使用 `decode_raw` 标志从编码后的 protobuf 中提取一些信息：

```bash
echo '08960112054170706c65' | xxd -r -p | protoc --decode_raw1: 1502: "Apple"
```

这告诉我们有两个字段，一个字段编号为 1，解码后的值为 150；另一个字段编号为 2，解码后的字符串为 "Apple"。

## 其他 wire type

- 字节（bytes）和嵌套消息（nested messages）的编码方式与字符串完全相同，采用长度分隔编码。
- 布尔值编码为 varint，`true` 得到 `01`，`false` 得到 `00`。
- 枚举（Enum）也编码为 varint。
- 重复字段（repeated fields，非 packed）在字节流中最终会变成多个 tag-value 对，同一 tag 会多次出现。
- Packed 重复字段编码为长度分隔字段。

## 结语

在本篇博客文章中，我们编码了一个示例 protobuf 消息，并使用 `protoc` 验证了编码后的字节。有关更多详细信息，请参阅官方的 [protobuf 编码指南](https://protobuf.dev/programming-guides/encoding)，或继续阅读[本系列的第 2 部分](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)，深入了解 map、负数和 packed 重复字段。

要了解这些编码后的消息是如何通过网络传输的，请查看我们的 [gRPC 深入解读](https://kreya.app/blog/grpc-deep-dive/)。
