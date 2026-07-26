---
title: makeUnicodeScalarIterator()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/makeunicodescalariterator()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/makeunicodescalariterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/makeunicodescalariterator%28%29.json'
content_hash: 'sha256:4c35a28426cd1d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# makeUnicodeScalarIterator()

<sub>Instance Method</sub>

Returns an iterator that will decode the code units into `Unicode.Scalar`s.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeUnicodeScalarIterator() -> UTF8Span.UnicodeScalarIterator
```

## Discussion

The resulting iterator has the same lifetime constraints as `self`.
