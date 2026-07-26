---
title: encodedReplacementCharacter
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/ascii/encodedreplacementcharacter
source_url: 'https://developer.apple.com/documentation/swift/unicode/ascii/encodedreplacementcharacter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/ascii/encodedreplacementcharacter.json'
content_hash: 'sha256:0758ae790454cd8c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [ASCII](../ascii.md)

# encodedReplacementCharacter

<sub>Type Property</sub>

A unicode scalar value to be used when repairing encoding/decoding errors, as represented in this encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var encodedReplacementCharacter: Unicode.ASCII.EncodedScalar { get }
```

## Discussion

If the Unicode replacement character U+FFFD is representable in this encoding, `encodedReplacementCharacter` encodes that scalar value.
