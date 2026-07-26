---
title: Int128.Words
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/words-swift.typealias
source_url: 'https://developer.apple.com/documentation/swift/int128/words-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/words-swift.typealias.json'
content_hash: 'sha256:19ec3cf3d97ed549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# Int128.Words

<sub>Type Alias</sub>

A type that represents the words of a binary integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Words = UInt128.Words
```

## Discussion

The `Words` type must conform to the `RandomAccessCollection` protocol with an `Element` type of `UInt` and `Index` type of `Int`.
