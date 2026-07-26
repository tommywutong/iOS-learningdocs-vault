---
title: 'skipBack(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/unicodescalariterator/skipback(by:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipback(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/skipback%28by%3A%29.json'
content_hash: 'sha256:c6e26c3c42d29200'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# skipBack(by:)

<sub>Instance Method</sub>

Move `currentCodeUnitOffset` to the start of the previous `n` scalars, without decoding them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func skipBack(by n: Int) -> Int
```

## Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be fewer than `n` if at the start of the UTF8Span.

> [!abstract] Complexity
> O(n)
