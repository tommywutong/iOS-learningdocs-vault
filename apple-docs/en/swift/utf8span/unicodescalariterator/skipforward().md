---
title: skipForward()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/unicodescalariterator/skipforward()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/skipforward()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/skipforward%28%29.json'
content_hash: 'sha256:662b3f51c752c99b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# skipForward()

<sub>Instance Method</sub>

Advance `currentCodeUnitOffset` to the end of the current scalar, without decoding it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func skipForward() -> Int
```

## Discussion

Returns the number of `Unicode.Scalar`s skipped over, which can be 0 if at the end of the UTF8Span.

> [!abstract] Complexity
> O(1)
