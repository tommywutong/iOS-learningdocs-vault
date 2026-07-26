---
title: 编码、解码与序列化
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/encoding-decoding-and-serialization
source_url: 'https://developer.apple.com/documentation/swift/encoding-decoding-and-serialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/encoding-decoding-and-serialization.json'
content_hash: 'sha256:e1a7f1eaf1d12e5a'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# 编码、解码与序列化

<sub>API 集合</sub>

通过隐式或自定义的编码方式，对你的类型的实例进行序列化和反序列化。

## 主题

### 自定义编码与解码

- [Encoding and Decoding Custom Types](../foundation/encoding-and-decoding-custom-types.md) — 让你的数据类型可编码、可解码，以便与 JSON 等外部表示形式兼容。
- [Codable](codable.md) — 一种可以与外部表示形式相互转换的类型。
- [Encodable](encodable.md) — 一种可以将自身编码为外部表示形式的类型。
- [Decodable](decodable.md) — 一种可以从外部表示形式解码出自身的类型。
- [CodingKey](codingkey.md) — 一种可用作编码和解码键的类型。
- [CodingKeyRepresentable](codingkeyrepresentable.md) — 一种可以与编码键相互转换的类型。
- [CodingUserInfoKey](codinguserinfokey.md) — 一个用户定义的键，用于在编码和解码期间提供上下文。

### 编码器与解码器

- [Encoder](encoder.md) — 一种可以将值编码为外部表示形式所用的原生格式的类型。
- [Decoder](decoder.md) — 一种可以将值从原生格式解码为内存中表示形式的类型。
- [EncodingError](encodingerror.md) — 编码某个值的过程中发生的错误。
- [DecodingError](decodingerror.md) — 解码某个值的过程中发生的错误。

### 编码容器

- [SingleValueEncodingContainer](singlevalueencodingcontainer.md) — 一种容器，支持存储和直接编码单个非键控值。
- [KeyedEncodingContainer](keyedencodingcontainer.md) — 一个具体的容器，提供进入编码器存储区的视图，使可编码类型的已编码属性可以通过键来访问。
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md) — 一种类型，提供进入编码器存储区的视图，用于以键控方式保存可编码类型的已编码属性。
- [UnkeyedEncodingContainer](unkeyedencodingcontainer.md) — 一种类型，提供进入编码器存储区的视图，用于按顺序、不使用键地保存可编码类型的已编码属性。

### 解码容器

- [KeyedDecodingContainer](keyeddecodingcontainer.md) — 一个具体的容器，提供进入解码器存储区的视图，使可解码类型的已编码属性可以通过键来访问。
- [SingleValueDecodingContainer](singlevaluedecodingcontainer.md) — 一种容器，支持存储和直接解码单个非键控值。
- [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md) — 一种类型，提供进入解码器存储区的视图，用于以键控方式保存可解码类型的已编码属性。
- [UnkeyedDecodingContainer](unkeyeddecodingcontainer.md) — 一种类型，提供进入解码器存储区的视图，用于按顺序、不使用键地保存可解码类型的已编码属性。

## 另请参阅

### 你的类型可用的工具

- [Basic Behaviors](basic-behaviors.md) — 在依赖相等性或顺序判断的操作中使用你的自定义类型，并将其用作集合与字典的成员。
- [Initialization with Literals](initialization-with-literals.md) — 允许使用不同种类的字面量来表达你的类型的值。
