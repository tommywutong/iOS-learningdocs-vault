---
title: Protobuf 工作原理——数据编码的艺术
source_url: 'https://victoriametrics.com/blog/go-protobuf/'
source_domain: victoriametrics.com
source_group: single-site
original_language: en
published: 2025-02-07
archived_at: 2026-07-27
content_hash: 'sha256:6ae944437844130a'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09）
container: '//div[contains(@class,''post__content'')]'
container_source: map
---

> 原文：[How Protobuf Works—The Art of Data Encoding](https://victoriametrics.com/blog/go-protobuf/)

本文是通信协议系列文章的一部分：

- [From net/rpc to gRPC in Go Applications](https://victoriametrics.com/blog/go-net-rpc/)
- [How HTTP/2 Works and How to Enable It in Go](https://victoriametrics.com/blog/go-http2/)
- [Practical Protobuf - From Basic to Best Practices](https://victoriametrics.com/blog/go-protobuf-basic/)
- How Protobuf Works—The Art of Data Encoding（本文所在位置）
- [gRPC in Go: Streaming RPCs, Interceptors, and Metadata](https://victoriametrics.com/blog/go-grpc-basic-streaming-interceptor/)

Protobuf（Protocol Buffers）是一种将数据序列化（serialize）成紧凑二进制格式的方法。这使得数据体积更小、在网络上的传输速度更快，但代价是降低了人类可读性。

它的工作方式是在一个 `.proto` 文件中定义数据结构——这个蓝图描述了存在哪些字段、字段的类型、服务等。然后，用这个文件生成不同编程语言的代码，让程序能够高效地编码和解码数据。

_“比起 JSON，Protobuf 序列化和反序列化数据需要更长时间吗？”_

有许多不同的编译器和实现，所以这个问题没有唯一的答案。不过，我们可以在 Go 中运行一个简单的基准测试，比较 `google.golang.org/protobuf` 和 `encoding/json`。虽然这算不上一个完全公平的比较，但确实能反映常见的选择。

我们还对另一个兼容 Protobuf 的方案 [easyproto](https://github.com/VictoriaMetrics/easyproto) 进行了基准测试，它专为高性能和低内存占用而设计，但做了一些取舍。

`easyproto` 只是一种使用 protobuf 编码的更简单方式，无需 `protoc` 编译器或代码生成。它遵循与 protobuf（proto3）完全相同的 wire format。

下面的基准测试是在本地机器上使用 Go 1.23.5 和 [libprotoc 29.2](https://github.com/protocolbuffers/protobuf/releases/tag/v29.2) 运行的：

```go
Protocol Buffers serialized size: 99 bytes
JSON serialized size: 214 bytes
easyproto serialized size: 99 bytes
JSON content:
{"name":"John Doe","age":30,"email":"john.doe@example.com","phone_numbers":["+1234567890","+0987654321"],"status":"ACTIVE","address":{"street":"123 Main St","city":"New York","country":"USA","postal_code":"10001"}}

Field by field comparison:
goos: darwin
goarch: arm64
BenchmarkProtobufMarshal-14    9051836  133.0 ns/op  112 B/op  1 allocs/op
BenchmarkJSONMarshal-14        4950854  248.8 ns/op  224 B/op  1 allocs/op
BenchmarkProtobufUnmarshal-14  4461856  258.8 ns/op  384 B/op  12 allocs/op
BenchmarkJSONUnmarshal-14      899058    1318 ns/op  560 B/op  18 allocs/op
easyprotoMarshal-14            16046793 74.21 ns/op    0 B/op   0 allocs/op
easyprotoUnmarshal-14          17370272 70.61 ns/op  112 B/op   3 allocs/op
```

这并不意外——Protocol Buffers 产生的输出要小得多，对于相同的数据结构，只有 99 字节，而 JSON 是 214 字节。随着数据量的增长，这种差异只会更加明显。

看一下序列化：

- `easyproto` 序列化只需要 74.21 纳秒，零内存分配。
- Protobuf（`proto.Marshal`）需要 133.0 纳秒，并产生一次 112 字节的内存分配。
- JSON（`encoding/json`）需要 248.8 纳秒，并产生一次 224 字节的内存分配。

反序列化的差距更大：

- `easyproto` 反序列化需要 70.61 纳秒，产生 3 次分配，共 112 字节。
- Protobuf（`proto.Unmarshal`）需要 293.6 纳秒，产生 13 次分配，共 448 字节。
- JSON（`encoding/json`）需要 1457 纳秒，产生 18 次分配，共 592 字节。

在今天的讨论中，我们将剖析 Proto3 中二进制数据的结构，并检查由 `protoc` 生成的 struct。

## 序列化（Serialization）

### 字段键（Field Key）或标签（Tag）编码

要编码一个字段，我们需要两样东西：字段在消息中的位置以及它的值是什么。我们将结合下面的代码片段来讲解编码过程：

```go
message Person {
  string name = 1;
  int32  id = 2;
  float  height = 3; // in meters
}

p := Person{
  Name:   "Phuong Le",
  Id:     300,
  Height: 1.75,
}
```

首先要弄清楚的是**每个字段如何被识别**。消息中的每个字段都有两个部分：一个唯一的数字和一个类型（字段的实际名称在这里并不重要）：

- 分配给每个字段的**唯一数字**被称为**字段编号（tag number）**。
- 字段的**类型**决定了所谓的**wire type**，它告诉系统值应如何编码（以及之后如何解码）。

Protobuf 有 5 种 wire type：

- **Varint（0）**：用于编码整数（`int32`、`int64`、`uint32`、`uint64`、`sint32`、`sint64`）、布尔值（`bool`）和枚举（`enum`）。
- **64-bit（1）**：用于固定长度的 64 位数据类型，如 `fixed64`、`sfixed64` 和 `double`。
- **Length-delimited（2）**：用于字符串、字节数组、嵌套消息，以及 packed repeated 字段。
- **Groups（3, 4）**：以前用于 group，现已废弃（deprecated）。
- **32-bit（5）**：用于固定长度的 32 位数据类型，如 `fixed32`、`sfixed32` 和 `float`。

这两部分——字段编号和 wire type——被组合成一个称为**标签（tag）**的单元。Protobuf 使用这个标签来识别消息中引用的是哪个字段。wire type 占据最低的 3 个比特位（最右边），而字段编号则占据其余部分：

```go
tag = (field_number << 3) | wire_type
```

然后，这个标签编号将使用一种称为可变长度编码（variable-length encoding）或 varint 编码的技术进行编码。由于我们示例中的数字足够小，它们会直接按其二进制形式编码。因此，示例中这些字段的标签值将是：

![Protobuf 如何为消息字段分配标签](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/4bd3ceaeed01c262702e.webp)

<sub>Protobuf 如何为消息字段分配标签</sub>

### 值编码

Protobuf 对每种类型的值并不都使用同一种编码。相反，它将它们分为三类：varint 编码、长度分隔编码（length-delimited encoding）和固定宽度编码（fixed-width encoding）。

#### Wire Type 0 的 Varint 编码

像 1、2 或 3 这样的小数字，如果用完整的 4 字节（`int32`）或 8 字节（`int64`）格式来存储会很浪费——这些字节大部分都会是零。相反，Protobuf 使用 varint 编码，这种技术的字节数会根据值的大小进行调整。数字越小，占用的字节就越少。

不过，这也有一个代价。每个字节的最左边一位被保留为 continuation 位（continuation bit），用来指示数字是否延续：

- 如果最高有效位（MSB）是 1，表示后面还有更多字节。
- 如果 MSB 是 0，表示这是最后一个字节，数字到此结束。

![数字 300 的 Protobuf varint 编码过程](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/5a0f248ef21199ac2733.webp)

<sub>数字 300 的 Protobuf varint 编码过程</sub>

对于更大的数字，需要更多字节——一个完整的 64 位整数最多需要 10 个字节。但在大多数情况下，数字往往很小，所以节省的空间非常可观。这使得 varint 在处理通常保持在较低范围内的值时是个不错的选择。

这里有一个问题：编码负数，比如 -1。在 32 位整数中，-1 表示为：

```go
11111111111111111111111111111111  // 32 bits
```

使用 varint 编码，那意味着需要 5 个字节。使用 64 位整数，则需要 10 个字节：

```go
// 32-bit integer varint
11111111 11111111 11111111 11111111 00001111

// 64-bit integer varint
11111111 11111111 11111111 11111111 11111111
11111111 11111111 11111111 11111111 00000001
```

发生这种情况是因为 varint 将数字视为无符号数，意味着负值最终会消耗额外空间。更糟糕的是，虽然你的 `int32` 通常只占用大约 4-6 个字节，但 `-1` 会让它像 `int64` 一样占用 10 个字节。这是因为 Protobuf 不知道你的确切类型——它只知道 wire type，而在 wire level 上，`int32` 和 `int64` 之间是没有区别的。

`int32` 和 `int64` 使用相同的 wire type，并且在二进制层面上两者没有区别。因此，`-1` 将被编码为 10 个字节。

为了避免这个问题，Protobuf 对带符号整数（`sint32`、`sint64`）采取了一种不同的方式——它使用 zig-zag varint 编码。

顾名思义，它在正负数字之间来回曲折（zigzag）：

- 正数 `n` 编码为 `2 * n`。
- 负数 `n` 编码为 `2 * |n| - 1`。

这意味着：

- `-1` 编码为 `1`
- `1` 编码为 `2`
- `-2` 编码为 `3`
- `2` 编码为 `4`

转换后，数字照常使用 varint 进行编码。这避免了将负数存储为大多字节值的低效问题。

在 Go 中，你可以使用 `google.golang.org/protobuf` 中的 `protowire` 包，甚至标准库的 `encoding/binary` 包亲自尝试。Go 确实同时支持常规 varint 和 zig-zag varint 编码。`encoding/binary` 包提供了两组函数：

- 无符号整数：`binary.PutUvarint` 和 `binary.Uvarint`。
- 带符号整数：`binary.PutVarint` 和 `binary.Varint`。

下面是一个对 `-1` 的快速测试：

```go
func main() {
  var num int64 = -1

  fmt.Printf("- Binary representation of %d in varint: ", num)

  buf := make([]byte, binary.MaxVarintLen64)
  binary.PutUvarint(buf, uint64(num))
  for _, b := range buf {
    fmt.Printf("%08b ", b)
  }
  fmt.Println()

  fmt.Printf("- Binary representation of %d in zigzag varint: ", num)
  bufZigzag := make([]byte, 1)
  binary.PutVarint(bufZigzag, num)
  for _, b := range bufZigzag {
    fmt.Printf("%08b ", b)
  }
}
```

输出如下：

```go
- Binary representation of -1 in varint: 11111111 11111111 11111111
11111111 11111111 11111111 11111111 11111111 11111111 00000001
- Binary representation of -1 in zigzag varint: 00000001
```

至此，值为 300 的 `id` 字段可以完整地用 3 个字节表示：

![Protobuf 对 ID 字段的 varint 编码](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/cb7e4171b4384fee1a16.webp)

<sub>Protobuf 对 ID 字段的 varint 编码</sub>

#### Wire Type 2 的长度分隔编码

长度分隔编码用于**没有固定大小**的数据类型。这包括字符串、字节数组、嵌套消息和 packed repeated 字段。

其思路很直接：将值分解为两部分：首先是一个前缀，告诉你接下来数据的长度（以字节为单位），然后是实际数据。在二进制格式中，它看起来像这样：`<length><data>`。

例如，在我们的例子中，`name` 字段包含 `"Phuong Le"`，以 UTF-8 编码后长度为 9 个字节。这意味着编码后的值将是：

![Protobuf 对字符串字段的长度分隔编码](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/d525cd8a73b11d53c618.webp)

<sub>Protobuf 对字符串字段的长度分隔编码</sub>

注意，字节的长度同样使用 varint 编码进行编码。

我们不在这里深入讲解 UTF-8 编码的工作原理，但就像 varint 一样，它有自己处理多字节字符和 continuation 位的方式。这就是总体的思路。

#### Wire Type 1 和 5 的固定宽度编码

固定宽度编码用于具有固定大小的字段，如 `fixed32`、`sfixed32`、`fixed64`、`sfixed64` 以及浮点数（`float`、`double`）。这里没什么新内容——这些值以简单的方式存储，没有额外的长度前缀或 varint 技巧。

这意味着 height 字段照常使用 IEEE 754 32 位浮点表示法进行编码：

![Protobuf 对 float 字段的固定宽度编码](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/0453f7d8a35724689ef1.webp)

<sub>Protobuf 对 float 字段的固定宽度编码</sub>

现在，把所有部分组合起来，最终编码后的消息看起来像这样：

```go
protobuf.encode(person) = [10 9 80 104 117 111 110 103 32 76 101 16 172 2 29 0 0 224 63]
```

最后一点，如果一个字段具有默认值（`""`、`0`、`false` 等），它根本不会被编码。这类似于 JSON 中的 `omitempty`。

有关 Protobuf 如何编码和解码数据的更多详细信息，请参阅 [Protobuf 文档](https://protobuf.dev/programming-guides/encoding/)。

#### Repeated 字段

`repeated` 字段中的元素使用我们之前介绍的技术进行编码。然而，整个 `repeated` 字段的序列化方式取决于其 wire type。

对于包含**原始数值类型**的 `repeated` 字段，Protobuf 使用 packed 模式（在 `proto3` 中默认启用）：

![Protobuf packed repeated 字段](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/4a6169e4f2b68a4f2278.webp)

<sub>Protobuf packed repeated 字段</sub>

在 packed 模式下，标签编号在序列化数据中只出现一次。`repeated` 字段中的所有元素共享这一个标签编号，使得编码更加紧凑。

相反，在 unpacked 模式下，标签编号在序列化数据中会为每个元素重复出现：

![Protobuf unpacked repeated 字段](../../../attachments/snapshots/victoriametrics.com/5050c6aa6366/deef2bae7766a82aeb3d.webp)

<sub>Protobuf unpacked repeated 字段</sub>

## 反序列化（在 Go 中）

Protobuf 的设计同时考虑了向后兼容性（较新的系统仍然可以读取旧的消息）和向前兼容性（较旧的系统仍然可以处理新的消息）。

为了了解这在实际中是如何工作的，我们来看看在 Go 中反序列化是如何进行的。

解码消息时，Protobuf 逐字节读取数据。对于每个字段，它首先读取一个标签，该标签包含两样东西。你可能已经从编码部分知道了：

- **wire type**，它告诉解码器如何解释接下来的几个字节。
- **字段编号（field number）**，它帮助解码器在消息定义中找到相应的字段。

如果字段编号与当前消息定义中的某个字段匹配，解码器会根据字段的类型正常处理它。然而，当解码器遇到一个不在消息定义中的字段编号时会发生什么？

Protobuf 不会失败，它有一种内置的方式来处理这种情况。它将此字段视为**未知字段（unknown field）**，并利用 wire type 信息来确定需要跳过多少字节，从而跳过它。这些未知字段并不会被简单地丢弃——它们实际上被存储在消息的一个单独部分中。

这就是为什么你会在解组（unmarshal）函数中看到一个名为 `DiscardUnknown` 的选项，它让你可以选择是保留这些未知字段，还是完全丢弃它们。

_“为什么不直接丢弃未知字段？”_

如果消息被传递给能理解这些字段的较新代码，数据仍然在那里，并且可以被正确解释：

```go
func main() {
	p := &Person{
		Name:   "Phuong Le",
		Id:    300,
		Height: 1.75,
	}
	bytes, _ := proto.Marshal(p)

	// unmarshal but keep the unknown fields
	p2 := &PersonWithoutHeight{}
	_ = proto.Unmarshal(bytes, p2)

	// unmarshal but discard the unknown fields
	p3 := &PersonWithoutHeight{}
	opts := proto.UnmarshalOptions{DiscardUnknown: true}
	_ = opts.Unmarshal(bytes, p3)

	fmt.Println(proto.Marshal(p2))
	fmt.Println(proto.Marshal(p3))
}
```

尽管我们将消息反序列化到了新版本 `PersonWithoutHeight` 中，`Height` 字段并没有丢失。当重新编码时，它仍然存在：

```bash
[10 9 80 104 117 111 110 103 32 76 101 16 172 2 29 0 0 224 63]
[10 9 80 104 117 111 110 103 32 76 101 16 172 2]
```

现在，如果我们反转这种情况：一个字段存在于当前消息定义中，但在接收到的消息中并不存在，那么该字段将直接取用其默认值。这与 Protobuf 编码数据的方式相符：具有默认值的字段一开始就不会被存储。

那么，我们从这次讨论中应该学到什么呢？

- 字段的顺序无关紧要。重要的是**字段编号（tag number）**（以及 **wire type**）。
- 为保持兼容性，不要重用或更改字段编号，也不要更改字段的类型。
- 如果删除一个字段，请用 `reserved 1, 2, 3;` 保留其**字段编号**，以防止将来被重用。

_“如果我更改了字段的类型但保留了相同的 wire type 会怎样？”_

即使两种类型使用相同的 wire type，它们对字节的解释方式也不一定相同。几个例子可以说明这一点：

- `int32` 和 `bool` 都使用 varint 编码，但非零的 `int32` 值如果被解释为布尔值，可能会被误读为 true。
- `int32` 和 `uint32` 也使用 varint 编码，但 `int32` 将字节视为带符号数，而 `uint32` 将它们视为无符号数。这意味着，一个负的 `int32`，如果被读取为 `uint32`，将会显示为一个巨大的正数。

## .pb.go 文件中的消息

让我们看看 Person struct，感受一下我们讨论过的所有内容是如何变得熟悉起来的：

```go
type Person struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Name          string                 `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Id            int32                  `protobuf:"varint,2,opt,name=id,proto3" json:"id,omitempty"`
	Height        float32                `protobuf:"fixed32,3,opt,name=height,proto3" json:"height,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}
```

每个字段都精确地符合我们基于其编码方式的预期：

- `Name` 使用 bytes 编码（长度分隔），字段编号为 1。
- `Id` 使用 varint 编码，字段编号为 2。
- `Height` 使用 fixed32 编码，字段编号为 3。

然后，我们还有 `unknownFields`，它——毫不意外——存储了反序列化过程中出现的任何**未知**字段。这只是一个 `[]byte`，用于保存当前消息定义无法识别的字段数据。

当你第一次对消息调用 `Marshal()` 时，Protobuf 会计算消息的大小并将其保存在 `sizeCache` 中。之后，如果你没有修改消息就再次调用 `Marshal()`，并启用了 `UseCachedSize` 选项，它就会重用缓存的大小，而不是重新计算所有内容。

`UseCachedSize` 是做什么的？

这个选项告诉 Protobuf：“我们之前已经计算过这个消息的大小了，所以直接使用那个缓存的大小，不用重新计算”。要让它正确工作，必须满足两个条件：大小此前已经计算过，并且消息（以及任何子消息）完全没有改变。如果有任何疑问，就不要使用它——Protobuf 会自行正确地处理大小计算。

缓存消息的大小在两种情况下是有益的：

1. 对于嵌套在其他消息内部的消息字段，Protocol Buffers 在写入实际消息内容之前，需要先写入一个长度前缀。
2. 提前知道大小，能让 Protocol Buffers 为输出缓冲区分配恰好足够的内存。如果不知道大小，它就需要不停地扩展缓冲区。

_“那个 `state` 字段呢？”_

每当 Protocol Buffers 需要对你的消息进行操作（比如将其转换为字节）时，它都会使用 `state` 字段来找出如何处理该消息。Go 中的每个 Protobuf 消息都需要支持**反射（reflection）**（在运行时对其结构进行内省）。

`state` 字段通过利用 `unsafe` 包，提供了一种零分配的方式来实现这一点——这种技术虽然存在风险，但通过直接操作内存来提升性能。

当你写 `p := Message{}` 时，`state` 字段并不存在；它是在你编码或解码时被延迟设置和初始化的。因此，第一次编码或解码时，可能会有轻微的性能开销。

并且……这也是理解 Protobuf 工作原理的讨论的最后一部分。

## 关于我们

如果你想要监控你的服务、跟踪指标并查看所有内容的性能，你可能会想了解 [VictoriaMetrics](https://docs.victoriametrics.com/)。它是一种快速、**开源**且节省成本的方式来监控你的基础设施。

我们是 Gophers，热衷于研究、实验和分享关于 Go 及其生态系统的知识。如果你发现任何过时的内容或有疑问，请随时联系我们。你可以通过 [X(@func25)](https://twitter.com/func25) 给我发私信。

相关文章：

- [Golang Series at VictoriaMetrics](https://victoriametrics.com/categories/go-@-victoriametrics)
- [How Go Arrays Work and Get Tricky with For-Range](https://victoriametrics.com/blog/go-array/)
- [Slices in Go: Grow Big or Go Home](https://victoriametrics.com/blog/go-slice/)
- [Go Maps Explained: How Key-Value Pairs Are Actually Stored](https://victoriametrics.com/blog/go-map/)
- [Golang Defer: From Basic To Traps](https://victoriametrics.com/blog/defer-in-go/)
- [Vendoring, or go mod vendor: What is it?](https://victoriametrics.com/blog/vendoring-go-mod-vendor/)
