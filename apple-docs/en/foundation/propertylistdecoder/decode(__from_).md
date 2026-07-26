---
title: 'decode(_:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistdecoder/decode(_:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder/decode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:b6eb50db5581f7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListDecoder](../propertylistdecoder.md)

# decode(_:from:)

<sub>Instance Method</sub>

Returns a value of the specified type by decoding a property list using the default property list format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from data: Data) throws -> T where T : Decodable
```

## Parameters

- `type` — The type of the value to decode from the supplied property list.

- `data` — The property list to decode.

## Discussion

If the data is not a valid property list, this method throws the [DecodingError.dataCorrupted(_:)](<../../swift/decodingerror/datacorrupted(__).md>) error. If a value within the property list fails to decode, this method throws the corresponding error.

## See Also

### Decoding

- [init()](<init().md>) — Creates a new, reusable property list decoder.
