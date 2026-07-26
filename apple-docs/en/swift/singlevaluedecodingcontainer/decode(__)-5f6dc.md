---
title: 'decode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/singlevaluedecodingcontainer/decode(_:)-5f6dc'
source_url: 'https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer/decode(_:)-5f6dc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevaluedecodingcontainer/decode%28_%3A%29-5f6dc.json'
content_hash: 'sha256:2712c186bb592563'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SingleValueDecodingContainer](../singlevaluedecodingcontainer.md)

# decode(_:)

<sub>Instance Method</sub>

Decodes a single value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode(_ type: Int128.Type) throws -> Int128
```

## Parameters

- `type` — The type to decode as.

## Return Value

A value of the requested type.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value cannot be converted to the requested type.

> [!danger] Throws
> `DecodingError.valueNotFound` if the encountered encoded value is null.
