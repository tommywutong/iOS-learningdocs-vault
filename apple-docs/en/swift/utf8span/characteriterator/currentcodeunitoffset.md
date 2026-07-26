---
title: currentCodeUnitOffset
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/characteriterator/currentcodeunitoffset
source_url: 'https://developer.apple.com/documentation/swift/utf8span/characteriterator/currentcodeunitoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/characteriterator/currentcodeunitoffset.json'
content_hash: 'sha256:64bfa534ee8ada2e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [CharacterIterator](../characteriterator.md)

# currentCodeUnitOffset

<sub>Instance Property</sub>

The byte offset of the start of the next `Character`. This is always scalar-aligned. It is always `Character`-aligned relative to the last call to `reset` (or the start of the span if not called).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentCodeUnitOffset: Int { get }
```
