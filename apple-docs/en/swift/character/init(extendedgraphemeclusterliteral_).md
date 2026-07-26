---
title: 'init(extendedGraphemeClusterLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/character/init(extendedgraphemeclusterliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/character/init(extendedgraphemeclusterliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character/init%28extendedgraphemeclusterliteral%3A%29.json'
content_hash: 'sha256:6ffb06bba91e0a22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Character](../character.md)

# init(extendedGraphemeClusterLiteral:)

<sub>Initializer</sub>

Creates a character with the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(extendedGraphemeClusterLiteral value: Character)
```

## Discussion

Do not call this initializer directly. It is used by the compiler when you use a string literal to initialize a `Character` instance. For example:

```swift
let oBreve: Character = "o\u{306}"
print(oBreve)
// Prints "ŏ"
```

The assignment to the `oBreve` constant calls this initializer behind the scenes.

## See Also

### Infrequently Used Functionality

- [init(unicodeScalarLiteral:)](<init(unicodescalarliteral_).md>)
