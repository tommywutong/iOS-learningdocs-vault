---
title: 'init(dictionaryLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/init(dictionaryliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/init(dictionaryliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/init%28dictionaryliteral%3A%29.json'
content_hash: 'sha256:a6fcc5edb91e0e97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# init(dictionaryLiteral:)

<sub>Initializer</sub>

Creates a dictionary initialized with a dictionary literal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(dictionaryLiteral elements: (Key, Value)...)
```

## Parameters

- `elements` — The key-value pairs that will make up the new dictionary. Each key in `elements` must be unique.

## Discussion

Do not call this initializer directly. It is called by the compiler to handle dictionary literals. To use a dictionary literal as the initial value of a dictionary, enclose a comma-separated list of key-value pairs in square brackets.

For example, the code sample below creates a dictionary with string keys and values.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
print(countryCodes)
// Prints "["BR": "Brazil", "JP": "Japan", "GH": "Ghana"]"
```

## See Also

### Infrequently Used Functionality

- [hashValue](hashvalue.md) — The hash value.
