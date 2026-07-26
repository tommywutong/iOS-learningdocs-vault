---
title: characters
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncsequence/characters
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/characters.json'
content_hash: 'sha256:f93c6c237b46f57c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# characters

<sub>Instance Property</sub>

A non-blocking sequence of `Characters` created by decoding the elements of `self` as UTF8.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var characters: AsyncCharacterSequence<Self> { get }
```

## See Also

### Adapting Textual Sequences

- [AsyncCharacterSequence](../../foundation/asynccharactersequence.md) — An asynchronous sequence of characters.
- [unicodeScalars](unicodescalars.md) — A non-blocking sequence of `UnicodeScalars` created by decoding the elements of `self` as UTF8.
- [AsyncUnicodeScalarSequence](../../foundation/asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [lines](lines.md) — A non-blocking sequence of newline-separated `Strings` created by decoding the elements of `self` as UTF8.
- [AsyncLineSequence](../../foundation/asynclinesequence.md) — An asynchronous sequence of lines of text.
