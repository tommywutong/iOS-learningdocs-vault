---
title: unkeyedContainer()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decoder/unkeyedcontainer()
source_url: 'https://developer.apple.com/documentation/swift/decoder/unkeyedcontainer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decoder/unkeyedcontainer%28%29.json'
content_hash: 'sha256:0e558837ba699cb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Decoder](../decoder.md)

# unkeyedContainer()

<sub>Instance Method</sub>

Returns the data stored in this decoder as represented in a container appropriate for holding values with no keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unkeyedContainer() throws -> any UnkeyedDecodingContainer
```

## Return Value

An unkeyed container view into this decoder.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not an unkeyed container.
