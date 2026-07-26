---
title: 'decode(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decode(_:)-5eszo'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decode(_:)-5eszo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decode%28_%3A%29-5eszo.json'
content_hash: 'sha256:a5430336fc51796a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decode(_:)

<sub>Instance Method</sub>

Decodes a value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decode(_ type: Int32.Type) throws -> Int32
```

## Parameters

- `type` — The type of value to decode.

## Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> [!danger] Throws
> `DecodingError.valueNotFound` if the encountered encoded value is null, or of there are no more values to decode.

## Default Implementations

### UnkeyedDecodingContainer Implementations

- [decode(_:)](<decode(__)-4c0se.md>) — Decodes a value of the given type.
- [decode(_:)](<decode(__)-6k8gu.md>) — Decodes a value of the given type.
