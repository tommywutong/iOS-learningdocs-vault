---
title: JSONEncoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder.json'
content_hash: 'sha256:af16185c40e3712b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# JSONEncoder

<sub>Class</sub>

An object that encodes instances of a data type as JSON objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class JSONEncoder
```

## Overview

The example below shows how to encode an instance of a simple `GroceryProduct` type from a JSON object. The type adopts [Codable](../swift/codable.md) so that it’s encodable as JSON using a [JSONEncoder](jsonencoder.md) instance.

```swift
struct GroceryProduct: Codable {
    var name: String
    var points: Int
    var description: String?
}

let pear = GroceryProduct(name: "Pear", points: 250, description: "A ripe pear.")

let encoder = JSONEncoder()
encoder.outputFormatting = .prettyPrinted

let data = try encoder.encode(pear)
print(String(data: data, encoding: .utf8)!)

/* Prints:
 {
   "name" : "Pear",
   "points" : 250,
   "description" : "A ripe pear."
 }
*/
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [NetworkEncoder](../network/networkencoder.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TopLevelEncoder](../combine/toplevelencoder.md)

## Topics

### First Steps

- [init()](<jsonencoder/init().md>) — Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.
- [encode(_:)](<jsonencoder/encode(__).md>) — Returns a JSON-encoded representation of the value you supply.

### Customizing Encoding

- [outputFormatting](jsonencoder/outputformatting-swift.property.md) — A value that determines the readability, size, and element order of the encoded JSON object.
- [OutputFormatting](jsonencoder/outputformatting-swift.struct.md) — The output formatting options that determine the readability, size, and element order of an encoded JSON object.
- [keyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.property.md) — A value that determines how to encode a  type’s coding keys as JSON keys.
- [KeyEncodingStrategy](jsonencoder/keyencodingstrategy-swift.enum.md) — The values that determine how to encode a type’s coding keys as JSON keys.
- [userInfo](jsonencoder/userinfo.md) — A dictionary you use to customize the encoding process by providing contextual information.

### Encoding Dates

- [dateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.property.md) — The strategy used when encoding dates as part of a JSON object.
- [DateEncodingStrategy](jsonencoder/dateencodingstrategy-swift.enum.md) — The formatting strategies available for formatting dates when encoding a date as JSON.

### Encoding Raw Data

- [dataEncodingStrategy](jsonencoder/dataencodingstrategy-swift.property.md) — The strategy that an encoder uses to encode raw data.
- [DataEncodingStrategy](jsonencoder/dataencodingstrategy-swift.enum.md) — The strategies for encoding raw data.

### Encoding Exceptional Numbers

- [nonConformingFloatEncodingStrategy](jsonencoder/nonconformingfloatencodingstrategy-swift.property.md) — The strategy used by an encoder when it encounters exceptional floating-point values.
- [NonConformingFloatEncodingStrategy](jsonencoder/nonconformingfloatencodingstrategy-swift.enum.md) — The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.

### Instance Methods

- [encode(_:configuration:)](<jsonencoder/encode(__configuration_)-721tx.md>)
- [encode(_:configuration:)](<jsonencoder/encode(__configuration_)-8l39i.md>)

## See Also

### JSON

- [Using JSON with custom types](using-json-with-custom-types.md) — Encode and decode JSON data, regardless of its structure, using Swift’s JSON support.
- [JSONDecoder](jsondecoder.md) — An object that decodes instances of a data type from JSON objects.
- [JSONSerialization](jsonserialization.md) — An object that converts between JSON and the equivalent Foundation objects.
