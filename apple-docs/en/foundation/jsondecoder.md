---
title: JSONDecoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder.json'
content_hash: 'sha256:e4008d6cba580721'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# JSONDecoder

<sub>Class</sub>

An object that decodes instances of a data type from JSON objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class JSONDecoder
```

## Overview

The example below shows how to decode an instance of a simple `GroceryProduct` type from a JSON object. The type adopts [Codable](../swift/codable.md) so that it’s decodable using a [JSONDecoder](jsondecoder.md) instance.

```swift
struct GroceryProduct: Codable {
    var name: String
    var points: Int
    var description: String?
}

let json = """
{
    "name": "Durian",
    "points": 600,
    "description": "A fruit with a distinctive scent."
}
""".data(using: .utf8)!

let decoder = JSONDecoder()
let product = try decoder.decode(GroceryProduct.self, from: json)

print(product.name) // Prints "Durian"
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [NetworkDecoder](../network/networkdecoder.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TopLevelDecoder](../combine/topleveldecoder.md)

## Topics

### Creating a Decoder

- [init()](<jsondecoder/init().md>) — Creates a new, reusable JSON decoder with the default formatting settings and decoding strategies.

### Decoding

- [decode(_:from:)](<jsondecoder/decode(__from_).md>) — Returns a value of the type you specify, decoded from a JSON object.

### Customizing Decoding

- [keyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.property.md) — A value that determines how to decode a type’s coding keys from JSON keys.
- [KeyDecodingStrategy](jsondecoder/keydecodingstrategy-swift.enum.md) — The values that determine how to decode a type’s coding keys from JSON keys.
- [userInfo](jsondecoder/userinfo.md) — A dictionary you use to customize the decoding process by providing contextual information.
- [allowsJSON5](jsondecoder/allowsjson5.md) — Specifies that decoding supports the JSON5 syntax.
- [assumesTopLevelDictionary](jsondecoder/assumestopleveldictionary.md) — Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.

### Decoding Dates

- [dateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.property.md) — The strategy used when decoding dates from part of a JSON object.
- [DateDecodingStrategy](jsondecoder/datedecodingstrategy-swift.enum.md) — The strategies available for formatting dates when decoding them from JSON.

### Decoding Raw Data

- [dataDecodingStrategy](jsondecoder/datadecodingstrategy-swift.property.md) — The strategy that a decoder uses to decode raw data.
- [DataDecodingStrategy](jsondecoder/datadecodingstrategy-swift.enum.md) — The strategies for decoding raw data.

### Decoding Exceptional Numbers

- [nonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.property.md) — The strategy used by a decoder when it encounters exceptional floating-point values.
- [NonConformingFloatDecodingStrategy](jsondecoder/nonconformingfloatdecodingstrategy-swift.enum.md) — The strategies for encoding nonconforming floating-point numbers, also known as IEEE 754 exceptional values.

### Instance Methods

- [decode(_:from:configuration:)](<jsondecoder/decode(__from_configuration_)-22lge.md>)
- [decode(_:from:configuration:)](<jsondecoder/decode(__from_configuration_)-xsq1.md>)

## See Also

### JSON

- [Using JSON with custom types](using-json-with-custom-types.md) — Encode and decode JSON data, regardless of its structure, using Swift’s JSON support.
- [JSONEncoder](jsonencoder.md) — An object that encodes instances of a data type as JSON objects.
- [JSONSerialization](jsonserialization.md) — An object that converts between JSON and the equivalent Foundation objects.
