---
title: singleValueContainer()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decoder/singlevaluecontainer()
source_url: 'https://developer.apple.com/documentation/swift/decoder/singlevaluecontainer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decoder/singlevaluecontainer%28%29.json'
content_hash: 'sha256:dd3d2094a216a4b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Decoder](../decoder.md)

# singleValueContainer()

<sub>Instance Method</sub>

Returns the data stored in this decoder as represented in a container appropriate for holding a single primitive value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func singleValueContainer() throws -> any SingleValueDecodingContainer
```

## Return Value

A single value container view into this decoder.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not a single value container.
