---
title: 'init(copying:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(copying:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(copying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28copying%3A%29.json'
content_hash: 'sha256:3694746e9ff2cff5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(copying:)

<sub>Initializer</sub>

Creates a new string, copying the specified code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(copying codeUnits: UTF8Span)
```

## Discussion

This initializer skips UTF-8 validation because `codeUnits` must contain valid UTF-8.

> [!abstract] Complexity
> O(n)
