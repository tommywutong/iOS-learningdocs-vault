---
title: makeCharacterIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/makecharacteriterator()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/makecharacteriterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/makecharacteriterator%28%29.json'
content_hash: 'sha256:2b81ea4f11cd4051'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# makeCharacterIterator()

<sub>Instance Method</sub>

Returns an iterator that will construct `Character`s from the underlying UTF-8 content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeCharacterIterator() -> UTF8Span.CharacterIterator
```

## Discussion

The resulting iterator has the same lifetime constraints as `self`.
