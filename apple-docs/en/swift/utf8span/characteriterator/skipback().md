---
title: skipBack()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/characteriterator/skipback()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/characteriterator/skipback()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/characteriterator/skipback%28%29.json'
content_hash: 'sha256:a8ddde174b163c6a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [CharacterIterator](../characteriterator.md)

# skipBack()

<sub>Instance Method</sub>

Move `currentCodeUnitOffset` to the start of the previous `Character`, without constructing it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func skipBack() -> Int
```

## Discussion

Returns the number of `Character`s skipped over, which can be 0 if at the start of the UTF8Span.
