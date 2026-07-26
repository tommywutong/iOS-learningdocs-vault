---
title: Dictionary.Keys.Index
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/dictionary/keys-swift.struct/index
source_url: 'https://developer.apple.com/documentation/swift/dictionary/keys-swift.struct/index'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/keys-swift.struct/index.json'
content_hash: 'sha256:6f00132726069004'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Keys](../keys-swift.struct.md)

# Dictionary.Keys.Index

<sub>Type Alias</sub>

A type that represents a position in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Index = Dictionary<Key, Value>.Index
```

## Discussion

Valid indices consist of the position of every element and a “past the end” position that’s not valid for use as a subscript argument.
