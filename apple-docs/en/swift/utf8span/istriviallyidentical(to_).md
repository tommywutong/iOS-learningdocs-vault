---
title: 'isTriviallyIdentical(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/utf8span/istriviallyidentical(to:)'
source_url: 'https://developer.apple.com/documentation/swift/utf8span/istriviallyidentical(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/istriviallyidentical%28to%3A%29.json'
content_hash: 'sha256:0149d801e042a067'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# isTriviallyIdentical(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether two instances refer to the same memory region, and have the same flags (such as [isKnownASCII](isknownascii.md)).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isTriviallyIdentical(to other: UTF8Span) -> Bool
```

## Discussion

> [!abstract] Complexity
> O(1)
