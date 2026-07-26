---
title: 'isCanonicallyEquivalent(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/iscanonicallyequivalent(to:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/iscanonicallyequivalent(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/iscanonicallyequivalent%28to%3A%29.json'
content_hash: 'sha256:b8f912087173f023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# isCanonicallyEquivalent(to:)

<sub>Instance Method</sub>

Whether `self` is equivalent to `other` under Unicode Canonical Equivalence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isCanonicallyEquivalent(to other: UTF8Span) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(n)
