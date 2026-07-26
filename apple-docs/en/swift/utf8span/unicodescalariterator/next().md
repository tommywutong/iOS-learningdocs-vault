---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/unicodescalariterator/next()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/next%28%29.json'
content_hash: 'sha256:b196d69616bc6b8f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# next()

<sub>Instance Method</sub>

Decode and return the scalar starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the returned scalar, which is also the start of the next scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> Unicode.Scalar?
```

## Discussion

Returns `nil` if at the end of the `UTF8Span`.

> [!abstract] Complexity
> O(1)
