---
title: prefix()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/unicodescalariterator/prefix()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/prefix()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/prefix%28%29.json'
content_hash: 'sha256:5890e7a69d05b522'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# prefix()

<sub>Instance Method</sub>

Returns the UTF8Span containing all the content up to the iterator’s current position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefix() -> UTF8Span
```

## Discussion

The resultant `UTF8Span` has the same lifetime constraints as `self`.

> [!abstract] Complexity
> O(1)
