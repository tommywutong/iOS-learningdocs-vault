---
title: 'isCanonicallyLessThan(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/iscanonicallylessthan(_:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/iscanonicallylessthan(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/iscanonicallylessthan%28_%3A%29.json'
content_hash: 'sha256:b0f410041321a64d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# isCanonicallyLessThan(_:)

<sub>Instance Method</sub>

Whether `self` orders less than `other` under Unicode Canonical Equivalence using normalized code-unit order (in NFC).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isCanonicallyLessThan(_ other: UTF8Span) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(n)
