---
title: suffix()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/unicodescalariterator/suffix()
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/suffix()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/suffix%28%29.json'
content_hash: 'sha256:20b82ea2b7ccbf5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# suffix()

<sub>Instance Method</sub>

Returns the UTF8Span containing all the content after the iterator’s current position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suffix() -> UTF8Span
```

## Discussion

The resultant `UTF8Span` has the same lifetime constraints as `self`.

> [!abstract] Complexity
> O(1)
