---
title: previous()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/characteriterator/previous()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/characteriterator/previous()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/characteriterator/previous%28%29.json'
content_hash: 'sha256:ce80aa18b2f8714b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [CharacterIterator](../characteriterator.md)

# previous()

<sub>Instance Method</sub>

Return the `Character` ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned `Character`, which is also the end of the previous `Character`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func previous() -> Character?
```

## Discussion

Returns `nil` if at the start of the `UTF8Span`.
