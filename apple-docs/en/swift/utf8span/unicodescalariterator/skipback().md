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
doc_path: /documentation/swift/utf8span/unicodescalariterator/skipback()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipback()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/skipback%28%29.json'
content_hash: 'sha256:c9b2b27077c1fce7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# skipBack()

<sub>Instance Method</sub>

Move `currentCodeUnitOffset` to the start of the previous scalar, without decoding it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func skipBack() -> Int
```

## Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be 0 if at the start of the UTF8Span.

> [!abstract] Complexity
> O(1)
