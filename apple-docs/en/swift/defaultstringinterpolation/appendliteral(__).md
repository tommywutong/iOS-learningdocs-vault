---
title: 'appendLiteral(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/defaultstringinterpolation/appendliteral(_:)'
source_url: 'https://developer.apple.com/documentation/swift/defaultstringinterpolation/appendliteral(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultstringinterpolation/appendliteral%28_%3A%29.json'
content_hash: 'sha256:ddebe07ab177e766'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DefaultStringInterpolation](../defaultstringinterpolation.md)

# appendLiteral(_:)

<sub>Instance Method</sub>

Appends a literal segment of a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendLiteral(_ literal: String)
```

## Discussion

You don’t need to call this method directly. It’s used by the compiler when interpreting string interpolations.
