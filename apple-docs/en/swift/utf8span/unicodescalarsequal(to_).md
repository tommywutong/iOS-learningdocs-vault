---
title: 'unicodeScalarsEqual(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/unicodescalarsequal(to:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/unicodescalarsequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/unicodescalarsequal%28to%3A%29.json'
content_hash: 'sha256:0aa439e886822553'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# unicodeScalarsEqual(to:)

<sub>Instance Method</sub>

Whether this span has the same `Unicode.Scalar`s as `other`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unicodeScalarsEqual(to other: some Sequence<Unicode.Scalar>) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(n)
