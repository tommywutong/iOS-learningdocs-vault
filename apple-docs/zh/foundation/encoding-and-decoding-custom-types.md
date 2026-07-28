---
title: 对自定义类型进行编码和解码
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/encoding-and-decoding-custom-types
source_url: 'https://developer.apple.com/documentation/foundation/encoding-and-decoding-custom-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encoding-and-decoding-custom-types.json'
content_hash: 'sha256:cdc201f651cbaf7c'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [归档与序列化](archives-and-serialization.md)

# 对自定义类型进行编码和解码

<sub>文章</sub>

让你的数据类型能够编码和解码，以兼容 JSON 等外部表示。

## 概述

许多编程任务涉及通过网络连接发送数据、将数据保存到磁盘，或向 API 和服务提交数据。这些任务通常要求在传输数据时，将数据编码为中间格式或从中间格式解码。

Swift 标准库定义了一种标准化的数据编码和解码方式。你可以通过在自定义类型上实现 [Encodable](../swift/encodable.md) 和 [Decodable](../swift/decodable.md) 协议来采用这种方式。采用这些协议后，[Encoder](../swift/encoder.md) 和 [Decoder](../swift/decoder.md) 协议的实现就能取得你的数据，并在数据与 JSON 或属性列表等外部表示之间进行编码或解码。若要同时支持编码和解码，请声明符合 [Codable](../swift/codable.md)；该协议结合了 [Encodable](../swift/encodable.md) 和 [Decodable](../swift/decodable.md) 协议。这个过程称为让类型_可编码（codable）_。

### 自动编码和解码

让类型可编码的最简单方式，是使用已经符合 [Codable](../swift/codable.md) 的类型声明其属性。这些类型包括 [String](../swift/string.md)、[Int](../swift/int.md) 和 [Double](../swift/double.md) 等标准库类型，以及 [Date](date.md)、[Data](data.md) 和 [URL](url.md) 等 Foundation 类型。只要类型的所有属性都可编码，在声明符合 [Codable](../swift/codable.md) 后，该类型就会自动符合此协议。

以一个存储地标名称和建立年份的 `Landmark` 结构体为例：

```swift
struct Landmark {
    var name: String
    var foundingYear: Int
}
```

将 [Codable](../swift/codable.md) 添加到 `Landmark` 的继承列表，会触发自动符合机制，从而满足 [Encodable](../swift/encodable.md) 和 [Decodable](../swift/decodable.md) 的所有协议要求：

```swift
struct Landmark: Codable {
    var name: String
    var foundingYear: Int
    
    // Landmark 现在支持 Codable 方法 init(from:) 和 encode(to:)，
    // 即使其声明中没有编写这些方法。
}
```

让自己的类型采用 [Codable](../swift/codable.md) 后，你就可以使用任何内建数据格式，以及自定义编码器和解码器提供的格式，对这些类型进行序列化和反序列化。例如，即使 `Landmark` 本身不包含专门处理属性列表或 JSON 的代码，也可以使用 [PropertyListEncoder](propertylistencoder.md) 和 [JSONEncoder](jsonencoder.md) 类对 `Landmark` 结构体进行编码。

同样的原则也适用于由其他可编码自定义类型组成的自定义类型。只要所有属性都符合 [Codable](../swift/codable.md)，任何自定义类型也都可以符合 [Codable](../swift/codable.md)。

以下示例展示了向 `Landmark` 结构体添加 `location` 属性时，自动符合 [Codable](../swift/codable.md) 的机制如何应用：

```swift
struct Coordinate: Codable {
    var latitude: Double
    var longitude: Double
}

struct Landmark: Codable {
    // Double、String 和 Int 都符合 Codable。
    var name: String
    var foundingYear: Int
    
    // 添加自定义 Codable 类型的属性后，整体仍符合 Codable。
    var location: Coordinate
}
```

[Array](../swift/array.md)、[Dictionary](../swift/dictionary.md) 和 [Optional](../swift/optional.md) 等内建类型只要包含可编码类型，也会符合 [Codable](../swift/codable.md)。你可以向 `Landmark` 添加一个 `Coordinate` 实例数组，整个结构体仍会满足 [Codable](../swift/codable.md)。

以下示例展示了在 `Landmark` 中使用内建可编码类型添加多个属性时，自动符合机制仍然适用：

```swift
struct Landmark: Codable {
    var name: String
    var foundingYear: Int
    var location: Coordinate
    
    // 添加这些属性后，Landmark 仍然可编码。
    var vantagePoints: [Coordinate]
    var metadata: [String: String]
    var website: URL?
}
```

### 仅编码或仅解码

在某些情况下，你可能不需要 [Codable](../swift/codable.md) 对双向编码和解码的支持。例如，有些 App 只需调用远程网络 API，无需解码包含相同类型的响应。如果只需支持数据编码，请声明符合 [Encodable](../swift/encodable.md)。反之，如果只需读取给定类型的数据，请声明符合 [Decodable](../swift/decodable.md)。

以下示例展示了 `Landmark` 结构体仅编码或仅解码数据的替代声明：

```swift
struct Landmark: Encodable {
    var name: String
    var foundingYear: Int
}
```

```swift
struct Landmark: Decodable {
    var name: String
    var foundingYear: Int
}
```

### 使用编码键选择要编码和解码的属性

Codable 类型可以声明名为 `CodingKeys` 的特殊嵌套枚举，该枚举符合 [CodingKey](../swift/codingkey.md) 协议。当存在此枚举时，它的 case 会作为编码或解码可编码类型实例时必须包含的权威属性列表。枚举 case 的名称应与类型中对应属性的名称相匹配。

如果在解码实例时不会出现某些属性，或某些属性不应包含在编码表示中，请从 `CodingKeys` 枚举中省略这些属性。若要让包含某个属性的类型自动符合 [Decodable](../swift/decodable.md) 或 [Codable](../swift/codable.md)，从 `CodingKeys` 中省略的属性需要具备默认值。

如果序列化数据格式中使用的键与数据类型的属性名称不匹配，请通过将 [String](../swift/string.md) 指定为 `CodingKeys` 枚举的原始值类型（raw-value type）来提供替代键。每个枚举 case 使用的字符串原始值就是编码和解码期间使用的键名。case 名称与其原始值之间的关联，让你能够按照 Swift [API 设计指南](https://swift.org/documentation/api-design-guidelines/)为数据结构命名，而不必匹配所建模序列化格式的名称、标点和大小写。

以下示例在编码和解码时为 `Landmark` 结构体的 `name` 和 `foundingYear` 属性使用替代键：

```swift
struct Landmark: Codable {
    var name: String
    var foundingYear: Int
    var location: Coordinate
    var vantagePoints: [Coordinate]
    
    enum CodingKeys: String, CodingKey {
        case name = "title"
        case foundingYear = "founding_date"
        
        case location
        case vantagePoints
    }
}
```

### 手动编码和解码

如果 Swift 类型的结构与其编码形式的结构不同，你可以提供 [Encodable](../swift/encodable.md) 和 [Decodable](../swift/decodable.md) 的自定义实现，以定义自己的编码和解码逻辑。

在以下示例中，`Coordinate` 结构体进行了扩展，以支持嵌套在 `additionalInfo` 容器中的 `elevation` 属性：

```swift
struct Coordinate {
    var latitude: Double
    var longitude: Double
    var elevation: Double

    enum CodingKeys: String, CodingKey {
        case latitude
        case longitude
        case additionalInfo
    }
    
    enum AdditionalInfoKeys: String, CodingKey {
        case elevation
    }
}
```

由于 `Coordinate` 类型的编码形式包含第二层嵌套信息，该类型采用 [Encodable](../swift/encodable.md) 和 [Decodable](../swift/decodable.md) 协议时，会使用两个枚举分别列出特定层级所使用的完整编码键集合。

在以下示例中，通过实现 [Decodable](../swift/decodable.md) 的必需初始化方法 [init(from:)](<../swift/decodable/init(from_).md>)，扩展 `Coordinate` 结构体以符合该协议：

```swift
extension Coordinate: Decodable {
    init(from decoder: Decoder) throws {
        let values = try decoder.container(keyedBy: CodingKeys.self)
        latitude = try values.decode(Double.self, forKey: .latitude)
        longitude = try values.decode(Double.self, forKey: .longitude)
        
        let additionalInfo = try values.nestedContainer(keyedBy: AdditionalInfoKeys.self, forKey: .additionalInfo)
        elevation = try additionalInfo.decode(Double.self, forKey: .elevation)
    }
}
```

该初始化方法使用作为参数接收的 [Decoder](../swift/decoder.md) 实例上的方法填充 `Coordinate` 实例。`Coordinate` 实例的两个属性使用 Swift 标准库提供的键控容器 API 进行初始化。

以下示例展示了如何通过实现 [Encodable](../swift/encodable.md) 的必需方法 [encode(to:)](<../swift/encodable/encode(to_).md>)，扩展 `Coordinate` 结构体以符合该协议：

```swift
extension Coordinate: Encodable {
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(latitude, forKey: .latitude)
        try container.encode(longitude, forKey: .longitude)
        
        var additionalInfo = container.nestedContainer(keyedBy: AdditionalInfoKeys.self, forKey: .additionalInfo)
        try additionalInfo.encode(elevation, forKey: .elevation)
    }
}
```

[encode(to:)](<../swift/encodable/encode(to_).md>) 方法的此实现会反向执行上一示例中的解码操作。

有关自定义编码和解码过程时所用容器类型的更多信息，请参阅 [KeyedEncodingContainerProtocol](../swift/keyedencodingcontainerprotocol.md) 和 [UnkeyedEncodingContainer](../swift/unkeyedencodingcontainer.md)。

## 另请参阅

### 相关文档

- [将 JSON 与自定义类型配合使用](using-json-with-custom-types.md) — 使用 Swift 的 JSON 支持对任意结构的 JSON 数据进行编码和解码。

### 采用可编码性

- [Codable](../swift/codable.md) — 可以在自身与外部表示之间进行转换的类型。
- [NSCoding](nscoding.md) — 让对象能够为归档（archiving）和分发进行编码与解码的协议。
- [NSSecureCoding](nssecurecoding.md) — 让对象能够以抵御对象替换攻击的可靠方式进行编码和解码的协议。
