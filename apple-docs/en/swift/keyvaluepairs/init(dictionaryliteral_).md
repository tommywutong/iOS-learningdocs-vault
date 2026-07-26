---
title: 'init(dictionaryLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyvaluepairs/init(dictionaryliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/keyvaluepairs/init(dictionaryliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyvaluepairs/init%28dictionaryliteral%3A%29.json'
content_hash: 'sha256:69ae91207aca18b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyValuePairs](../keyvaluepairs.md)

# init(dictionaryLiteral:)

<sub>Initializer</sub>

Creates a new `KeyValuePairs` instance from the given dictionary literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(dictionaryLiteral elements: (Key, Value)...)
```

## Discussion

The order of the key-value pairs is kept intact in the resulting `KeyValuePairs` instance.
