---
title: String.CharacterView
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/characterview
source_url: 'https://developer.apple.com/documentation/swift/string/characterview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/characterview.json'
content_hash: 'sha256:be9a87a143cd231e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# String.CharacterView

<sub>Type Alias</sub>

A view of a string’s contents as a collection of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CharacterView = String
```

## Discussion

Previous versions of Swift provided this view since String itself was not a collection. String is now a collection of characters, so this type is now just an alias for String.
