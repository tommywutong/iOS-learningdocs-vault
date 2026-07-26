---
title: encodeNil()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyedencodingcontainer/encodenil()
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodenil()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encodenil%28%29.json'
content_hash: 'sha256:4bb9afad16a466b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encodeNil()

<sub>Instance Method</sub>

Encodes a null value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeNil() throws
```

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if a null value is invalid in the current context for this format.
