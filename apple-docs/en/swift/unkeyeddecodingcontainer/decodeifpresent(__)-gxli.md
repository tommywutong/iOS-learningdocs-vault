---
title: 'decodeIfPresent(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-gxli'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-gxli'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodeifpresent%28_%3A%29-gxli.json'
content_hash: 'sha256:fc468e0efb306b5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodeIfPresent(_:)

<sub>Instance Method</sub>

Decodes a value of the given type, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeIfPresent(_ type: Int128.Type) throws -> Int128?
```

## Parameters

- `type` — The type of value to decode.

## Return Value

A decoded value of the requested type, or `nil` if the value is a null value, or if there are no more elements to decode.

## Discussion

This method returns `nil` if the container has no elements left to decode, or if the value is null. The difference between these states can be distinguished by checking `isAtEnd`.

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Default Implementations

### UnkeyedDecodingContainer Implementations

- [decodeIfPresent(_:)](<decodeifpresent(__)-11drn.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-1mzxv.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-33p27.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-3hokf.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-3tuys.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-4b7tu.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-4bqkd.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-5mgpl.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-5zug7.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-64o4m.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-6k5py.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-6snuc.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-87qsg.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-8nfu7.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-8we74.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-9tk6h.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<decodeifpresent(__)-o708.md>) — Decodes a value of the given type, if present.
