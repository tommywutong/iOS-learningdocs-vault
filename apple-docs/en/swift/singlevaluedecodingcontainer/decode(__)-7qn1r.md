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
doc_path: '/documentation/swift/singlevaluedecodingcontainer/decode(_:)-7qn1r'
source_url: 'https://developer.apple.com/documentation/swift/singlevaluedecodingcontainer/decode(_:)-7qn1r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevaluedecodingcontainer/decode%28_%3A%29-7qn1r.json'
content_hash: 'sha256:5eaf42fbf58fd317'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SingleValueDecodingContainer](../singlevaluedecodingcontainer.md)

# decode(_:)

<sub>Instance Method</sub>

Decodes a single value of the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode(_ type: Int32.Type) throws -> Int32
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

## Default Implementations

### SingleValueDecodingContainer Implementations

- [decode(_:)](<decode(__)-1rz83.md>) — Decodes a single value of the given type.
- [decode(_:)](<decode(__)-5f6dc.md>) — Decodes a single value of the given type.
- [decode(_:)](<decode(__)-5i4ec.md>) — Decodes a single value of the given type.
- [decode(_:)](<decode(__)-6vzg2.md>) — Decodes a single value of the given type.
