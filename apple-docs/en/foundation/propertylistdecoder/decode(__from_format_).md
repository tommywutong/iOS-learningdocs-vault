---
title: 'decode(_:from:format:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistdecoder/decode(_:from:format:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder/decode(_:from:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder/decode%28_%3Afrom%3Aformat%3A%29.json'
content_hash: 'sha256:e27d4e25c299c206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListDecoder](../propertylistdecoder.md)

# decode(_:from:format:)

<sub>Instance Method</sub>

Returns a value of the specified type by decoding a property list using the supplied format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<T>(_ type: T.Type, from data: Data, format: inout PropertyListDecoder.PropertyListFormat) throws -> T where T : Decodable
```

## Discussion

If the data is not a valid property list, this method throws the [DecodingError.dataCorrupted(_:)](<../../swift/decodingerror/datacorrupted(__).md>) error. If a value within the property list fails to decode, this method throws the corresponding error.

## See Also

### Customizing Decoding

- [userInfo](userinfo.md) — A dictionary you use to customize decoding by providing contextual information.
