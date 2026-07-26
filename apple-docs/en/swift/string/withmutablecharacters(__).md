---
title: 'withMutableCharacters(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/withmutablecharacters(_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/withmutablecharacters(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/withmutablecharacters%28_%3A%29.json'
content_hash: 'sha256:43a2e684939e1a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# withMutableCharacters(_:)

<sub>Instance Method</sub>

Applies the given closure to a mutable view of the string’s characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func withMutableCharacters<R>(_ body: (inout String) -> R) -> R
```

## Discussion

Previous versions of Swift provided this view since String itself was not a collection. String is now a collection of characters, so this type is now just an alias for String.
