---
title: 'reset(toUnchecked:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/unicodescalariterator/reset(tounchecked:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/reset(tounchecked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalariterator/reset%28tounchecked%3A%29.json'
content_hash: 'sha256:b0996ada3f5c5667'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UTF8Span](../../utf8span.md) · [UnicodeScalarIterator](../unicodescalariterator.md)

# reset(toUnchecked:)

<sub>Instance Method</sub>

Reset this iterator to `codeUnitOffset`, skipping _all_ safety checks (including bounds checks).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reset(toUnchecked codeUnitOffset: Int)
```

## Discussion

Note: This is only for very specific, low-level use cases. If `codeUnitOffset` is not properly scalar-aligned, this function can result in undefined behavior when, e.g., `next()` is called.

For example, this could be used by a regex engine to backtrack to a known-valid previous position.

> [!abstract] Complexity
> O(1)
